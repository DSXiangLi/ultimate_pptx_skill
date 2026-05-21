---
name: mars-fund-context-injector
description: "Inject Mars Fund context and execute session startup workflow on /new, /reset commands"
metadata:
  openclaw:
    emoji: "🚀"
    events:
      - message:received
      - command:new
      - command:reset
      - command:clear
      - command:compact
    requires:
      bins: ["node"]
---

# Mars Fund Context Injector

This hook injects Mars Fund context information into sessions and executes the session startup workflow.

## What it does

1. **On `message` event**: Updates USER.md with user permission info (with cache interval)
2. **On `command:new/reset`**: Forces USER.md update

## Files affected

- `USER.md` - User permission info

## Configuration

The hook reads configuration from:
- Workspace directory: `<workspace>/`
- Cache directory: `<workspace>/.cache/`
- Log file: `<workspace>/.cache/mars-fund-hook.log`
