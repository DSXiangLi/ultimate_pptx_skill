import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import path from "node:path";
import os from "node:os";
import fs from "node:fs";
import type { AgentMessage } from "@mariozechner/pi-agent-core";

/**
 * Config Guard — 拦截敏感配置文件的读取
 *
 * 只在 before_tool_call 层拦截敏感路径访问。
 * 工具输出中的密钥脱敏由 openclaw-env-mask 负责。
 */

const DEFAULT_SENSITIVE_PATHS = [
  "~/.ssh",
  "~/.git-credentials",
  "~/.aws",
  "~/.kube",
  "~/.docker",
  "~/.openclaw/openclaw.json",
];

const FILE_TOOLS = new Set([
  "read_file", "write_file", "edit_file", "apply_diff",
  "list_files", "search_files", "glob", "grep", "gateway",
]);

const SHELL_TOOLS = new Set(["bash", "exec", "shell", "sh"]);

const SENSITIVE_COMMAND_PATTERNS = [
  /\becho\s+\$[A-Za-z_][A-Za-z0-9_]*/i,
  /\becho\s+\$\{[A-Za-z_][A-Za-z0-9_]*\}/i,
  /\bprintenv\b/i,
  /\benv\s*(?:\||$)/i,
  /^set\s*$/i,
];

function expandHome(p: string): string {
  if (p.startsWith("~/") || p === "~") return path.join(os.homedir(), p.slice(1));
  return p;
}

function isSensitivePath(candidate: string, extraPaths: string[]): boolean {
  const expanded = expandHome(candidate);
  const normalized = path.normalize(expanded);
  const allSensitive = [...DEFAULT_SENSITIVE_PATHS, ...extraPaths];
  for (const sp of allSensitive) {
    const expandedSp = expandHome(sp);
    const normalizedSp = path.normalize(expandedSp);
    if (normalized === normalizedSp || normalized.startsWith(normalizedSp + path.sep)) return true;
  }
  const basename = path.basename(normalized);
  if (basename === ".env" || basename.startsWith(".env.")) return true;
  return false;
}

function hasSensitivePathInCommand(cmd: string, extraPaths: string[]): boolean {
  const allSensitive = [...DEFAULT_SENSITIVE_PATHS, ...extraPaths];
  for (const sp of allSensitive) {
    const expandedSp = expandHome(sp);
    const basenameSp = path.basename(expandedSp);
    if (cmd.includes(sp) || cmd.includes(expandedSp) || cmd.includes(basenameSp)) return true;
  }
  if (/\b(?:cat|less|head|tail|more)\s+\S*\.env/i.test(cmd)) return true;
  return false;
}

function getPathCandidates(params: Record<string, unknown>): string[] {
  const candidates: unknown[] = [];
  for (const key of ["path", "file_path", "file", "paths", "files", "directory", "dir"]) {
    if (key in params) {
      const val = params[key];
      if (typeof val === "string") candidates.push(val);
      else if (Array.isArray(val)) candidates.push(...val);
    }
  }
  return candidates.filter((c): c is string => typeof c === "string");
}

export default definePluginEntry({
  id: "openclaw-config-guard",
  name: "Config Guard",
  description: "Block sensitive file access before tool calls",
  register(api) {
    const pluginConfig = (api.pluginConfig ?? {}) as { extraPaths?: string[] };
    const extraPaths = Array.isArray(pluginConfig.extraPaths) ? pluginConfig.extraPaths : [];

    api.logger.info?.(`[Config Guard] Loaded.`);

    // 1. before_tool_call：拦截文件/网关工具的敏感路径访问
    api.on(
      "before_tool_call",
      (event) => {
        if (FILE_TOOLS.has(event.toolName)) {
          const candidates = getPathCandidates(event.params);
          for (const candidate of candidates) {
            if (isSensitivePath(candidate, extraPaths)) {
              api.logger.info?.(`[Config Guard] BLOCKED file tool: ${event.toolName} -> ${candidate}`);
              return {
                block: true,
                blockReason: `[Config Guard] Blocked access to sensitive path: ${candidate}`,
              };
            }
          }
        }
        if (SHELL_TOOLS.has(event.toolName)) {
          const cmd = String(event.params.command ?? "");
          for (const pattern of SENSITIVE_COMMAND_PATTERNS) {
            if (pattern.test(cmd)) {
              api.logger.info?.(`[Config Guard] BLOCKED shell pattern: ${event.toolName} -> ${cmd.slice(0, 200)}`);
              return {
                block: true,
                blockReason: `[Config Guard] Blocked command that may leak env vars: ${cmd.slice(0, 200)}`,
              };
            }
          }
          if (hasSensitivePathInCommand(cmd, extraPaths)) {
            api.logger.info?.(`[Config Guard] BLOCKED shell path: ${event.toolName} -> ${cmd.slice(0, 200)}`);
            return {
              block: true,
              blockReason: `[Config Guard] Blocked command referencing sensitive path: ${cmd.slice(0, 200)}`,
            };
          }
        }
      },
    );

    // before_message_write 已移除：消息输出层的路径名替换功能已下线。
    // 原因：模型输出不需要替换路径名，before_tool_call 拦截 + env-mask 脱敏已足够。
  },
});
