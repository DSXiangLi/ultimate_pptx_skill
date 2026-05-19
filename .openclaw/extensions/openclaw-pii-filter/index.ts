import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";

/**
 * PII Filter — 在用户消息发送给 LLM 之前脱敏中国常见个人身份信息
 *
 * 覆盖范围：
 * - 18位 / 15位身份证号 → [ID_REDACTED]
 * - 中国大陆手机号 → [PHONE_REDACTED]
 * - 邮箱地址 → [EMAIL_REDACTED]
 * - 银行卡号(16-19位数字序列) → [CARD_REDACTED]
 */
export default definePluginEntry({
  id: "openclaw-pii-filter",
  name: "PII Filter",
  description:
    "Redact Chinese PII (ID card, phone, email, bank card) from messages before sending to LLM",
  register(api) {
    api.registerTextTransforms({
      input: [
        // 18位身份证号 (含最后一位校验码 X/x)
        {
          from: /\b\d{6}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]\b/g,
          to: "[ID_REDACTED]",
        },
        // 15位身份证号
        {
          from: /\b\d{6}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}\b/g,
          to: "[ID_REDACTED]",
        },
        // 中国大陆手机号
        {
          from: /\b1[3-9]\d{9}\b/g,
          to: "[PHONE_REDACTED]",
        },
        // 邮箱地址
        {
          from: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g,
          to: "[EMAIL_REDACTED]",
        },
        // 银行卡号 (16-19位连续数字序列)
        {
          from: /\b\d{16,19}\b/g,
          to: "[CARD_REDACTED]",
        },
      ],
      output: [],
    });
  },
});
