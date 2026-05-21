import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import type { AgentMessage } from "@mariozechner/pi-agent-core";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

/**
 * Env Mask — 脱敏消息中的技术凭证
 *
 * 核心机制：before_message_write（同步）
 * 在消息写入 session 之前，递归扫描所有文本字段，把密钥/密码/token 替换为 ***。
 *
 * 覆盖范围：
 * - 环境变量赋值: KEY=xxxxx / KEY: xxxxx
 * - JSON 字段: "apiKey": "xxxxx"
 * - Bearer token
 * - OpenAI sk-xxx / Groq gsk_xxx / Gemini AIza...
 * - 阿里云 AccessKey
 * - GIL_ 前缀变量
 * - 动态环境变量实际值（process.env）
 */

const SKIP_ENV_KEYS = new Set([
  "PATH", "HOME", "USER", "SHELL", "PWD", "OLDPWD", "PS1", "PS2",
  "LANG", "TERM", "DISPLAY", "XDG_SESSION_TYPE", "XDG_CURRENT_DESKTOP",
  "SSH_AGENT_LAUNCHER", "GNOME_DESKTOP_SESSION_ID", "GTK_IM_MODULE",
  "QT_IM_MODULE", "XMODIFIERS", "DBUS_SESSION_BUS_ADDRESS", "DESKTOP_SESSION",
  "GNOME_SHELL_SESSION_MODE", "USERNAME", "LOGNAME", "HOSTNAME", "MAIL",
  "TMPDIR", "XDG_CONFIG_DIRS", "XDG_DATA_DIRS", "SESSION_MANAGER", "WINDOWPATH",
]);

/** 动态环境变量值白名单 — 排除通用布尔值、协议值等，避免大面积误伤 */
const COMMON_VALUE_WHITELIST = new Set([
  'true', 'false', 'yes', 'no', 'on', 'off',
  'null', 'undefined', 'none', 'nil', 'default',
  'localhost', '127.0.0.1', '0.0.0.0', '::1',
]);

/** 环境变量值最小长度 — 低于此长度的值不会被全局替换 */
const MIN_SENSITIVE_VALUE_LENGTH = 8;

function escapeRegExp(string: string): string {
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function buildReplacements(): Array<{ from: RegExp; to: string }> {
  const reps: Array<{ from: RegExp; to: string }> = [
    // 环境变量赋值: ANYTHING_API_KEY=xxxxx / PASSWORD=xxxxx
    { from: /\b([A-Z_]*(?:API_KEY|SECRET|PASSWORD|TOKEN|PWD|PASS))=[^\s;]*/gi, to: "$1=***" },
    // 冒号分隔: ANYTHING_API_KEY: xxxxx
    { from: /\b([A-Z_]*(?:API_KEY|SECRET|PASSWORD|TOKEN|PWD|PASS)):\s*[^\s;]*/gi, to: "$1: ***" },
    // GIL_ 前缀变量赋值
    { from: /\b(GIL_[A-Z_]*(?:PASSWORD|KEY|SECRET|TOKEN|HOST|URL))=[^\s;]*/gi, to: "$1=***" },
    // GIL_ 前缀变量冒号分隔
    { from: /\b(GIL_[A-Z_]*(?:PASSWORD|KEY|SECRET|TOKEN|HOST|URL)):\s*[^\s;]*/gi, to: "$1: ***" },
    // JSON 通用字段
    { from: /"([a-zA-Z_]*(?:api_?)?(?:[Kk]ey|[Ss]ecret)|[Pp]assword|[Tt]oken|[Aa]uth)"\s*:\s*"[^"]*"/g, to: '"$1": "***"' },
    // JSON GIL_ 字段
    { from: /"(GIL_[A-Z_]*(?:PASSWORD|KEY|SECRET|TOKEN|HOST|URL))"\s*:\s*"[^"]*"/gi, to: '"$1": "***"' },
    // Bearer token
    { from: /\bBearer\s+[A-Za-z0-9_\-\.+=]*/g, to: "Bearer ***" },
    // OpenAI sk-xxx
    { from: /\bsk-[A-Za-z0-9]{20,}/g, to: "sk-***" },
    // Groq gsk_xxx
    { from: /\bgsk_[A-Za-z0-9]{20,}/g, to: "gsk_***" },
    // Gemini AIza...
    { from: /\bAIza[A-Za-z0-9_\-]{20,}/g, to: "AIza***" },
    // 阿里云 AccessKey
    { from: /\b(?:AK|LTAI)[A-Za-z0-9]{10,}/g, to: "***" },
  ];

  // 动态匹配：key 名看起来像敏感信息的环境变量
  const SENSITIVE_KEY_PATTERN = /(?:KEY|SECRET|TOKEN|PASSWORD|PASS|PWD|AUTH|CREDENTIAL|PRIVATE)/i;
  for (const [key, value] of Object.entries(process.env)) {
    if (!value || value.length < MIN_SENSITIVE_VALUE_LENGTH) continue;
    if (SKIP_ENV_KEYS.has(key)) continue;
    if (/^\d+$/.test(value)) continue;
    if (!SENSITIVE_KEY_PATTERN.test(key)) continue; // 只脱敏 key 名像敏感信息的变量
    if (COMMON_VALUE_WHITELIST.has(value.toLowerCase())) continue;
    try {
      const escaped = escapeRegExp(value);
      reps.push({ from: new RegExp(escaped, "g"), to: "***" });
    } catch {
      // ignore
    }
  }

  // 动态匹配：openclaw.json 中的敏感值
  try {
    const configPath = path.join(os.homedir(), '.openclaw', 'openclaw.json');
    if (fs.existsSync(configPath)) {
      const raw = fs.readFileSync(configPath, 'utf8');
      const cfg = JSON.parse(raw);
      function scanOpenClaw(obj: unknown) {
        if (!obj || typeof obj !== 'object') return;
        for (const [k, v] of Object.entries(obj)) {
          if (typeof v === 'string' && v.length >= MIN_SENSITIVE_VALUE_LENGTH) {
            if (SENSITIVE_KEY_PATTERN.test(k) && !COMMON_VALUE_WHITELIST.has(v.toLowerCase())) {
              try {
                const escaped = escapeRegExp(v);
                reps.push({ from: new RegExp(escaped, 'g'), to: '***' });
              } catch {
                // ignore
              }
            }
          } else if (typeof v === 'object' && v !== null) {
            scanOpenClaw(v);
          }
        }
      }
      scanOpenClaw(cfg);
    }
  } catch {
    // ignore
  }

  return reps;
}

function applyReplacements(text: string, reps: Array<{ from: RegExp; to: string }>): string {
  let result = text;
  for (const { from, to } of reps) {
    result = result.replace(from, to);
  }
  return result;
}

function redactValue(value: unknown, reps: Array<{ from: RegExp; to: string }>, visited = new WeakSet()): unknown {
  if (typeof value === "string") {
    return applyReplacements(value, reps);
  }
  if (Array.isArray(value)) {
    return value.map((v) => redactValue(v, reps, visited));
  }
  if (value && typeof value === "object" && !Array.isArray(value)) {
    if (visited.has(value)) return value; // 防循环引用
    visited.add(value);
    const next = { ...(value as Record<string, unknown>) };
    for (const key of Object.keys(next)) {
      next[key] = redactValue(next[key], reps, visited);
    }
    return next;
  }
  return value;
}

export default definePluginEntry({
  id: "openclaw-env-mask",
  name: "Env Mask",
  description: "Redact API keys, passwords, tokens from all messages before persistence",
  register(api) {
    const reps = buildReplacements();
    api.logger.info?.(`[Env Mask] Loaded with ${reps.length} replacement patterns.`);

    // 兜底：在消息写入 session 前脱敏（同步 hook）
    api.on(
      "before_message_write",
      (event) => {
        const msg = event.message as Record<string, unknown>;
        let changed = false;
        const nextMsg = { ...msg };

        if ("content" in msg) {
          const redacted = redactValue(msg.content, reps);
          if (redacted !== msg.content) {
            nextMsg.content = redacted;
            changed = true;
          }
        }
        if (typeof msg.text === "string") {
          const redacted = applyReplacements(msg.text, reps);
          if (redacted !== msg.text) {
            nextMsg.text = redacted;
            changed = true;
          }
        }
        if (typeof msg.errorMessage === "string") {
          const redacted = applyReplacements(msg.errorMessage, reps);
          if (redacted !== msg.errorMessage) {
            nextMsg.errorMessage = redacted;
            changed = true;
          }
        }

        if (changed) {
          return { message: nextMsg as AgentMessage };
        }
      },
    );
  },
});
