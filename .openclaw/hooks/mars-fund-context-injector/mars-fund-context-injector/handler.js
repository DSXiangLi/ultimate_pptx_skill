/**
 * Mars Fund Context Injector Hook
 *
 * 在收到用户消息时,将 OpenClaw context 信息写入临时文件
 * 供 Mars Mars Fund MCP 技能的 http_client.py 读取
 *
 * 在执行 reset/clear/compact 命令时,更新用户信息
 *
 * 触发事件: message, command:new, command:reset, command:clear, command:compact
 *
 * 写入目录策略:
 * - 全局目录: ~/.openclaw/.cache/openclaw_context.json
 * - 所有工作空间: <workspace>/.cache/openclaw_context.json
 * - USER.md: 写入所有工作空间的 USER.md
 */

const http = require('http');
const https = require('https');
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const os = require('os');

// 默认工作空间目录
const DEFAULT_WORKSPACE_DIR = '/home/claw/小弘同学的工作空间';

// 缓存更新间隔：6 小时（21600000 毫秒）
const USER_INFO_UPDATE_INTERVAL = 6 * 60 * 60 * 1000;

// 日志文件路径（全局）
const LOG_FILE = path.join(os.homedir(), '.openclaw', '.cache', 'mars-fund-hook.log');

/**
 * 清理 OSS 路径中的非法字符
 * 将 ':' 替换为 '-'，避免作为 OSS bucket 前缀时报错
 */
function sanitizeOssPath(value) {
  if (!value) return value;
  return String(value).replace(/:/g, '_');
}

/**
 * 获取全局缓存目录 ~/.openclaw/.cache
 */
function getGlobalCacheDir() {
  return path.join(os.homedir(), '.openclaw', '.cache');
}

/**
 * 获取所有工作空间目录
 * 从 openclaw.json 的 agents.list 读取
 */
function getAllWorkspaceDirs() {
  const workspaces = [];
  
  try {
    const configPath = path.join(os.homedir(), '.openclaw', 'openclaw.json');
    const configContent = fs.readFileSync(configPath, 'utf-8');
    const config = JSON.parse(configContent);
    
    // 从 agents.list 提取 workspace
    if (config.agents && config.agents.list) {
      for (const agent of config.agents.list) {
        if (agent.workspace) {
          // 解析 ~ 为 home 目录
          const workspaceDir = agent.workspace.replace(/^~/, os.homedir());
          if (!workspaces.includes(workspaceDir)) {
            workspaces.push(workspaceDir);
            log(`从配置发现工作空间: ${workspaceDir} (agent: ${agent.id})`, 'DEBUG');
          }
        }
      }
    }
    
    // 如果配置中没有工作空间，使用默认值
    if (workspaces.length === 0) {
      workspaces.push(DEFAULT_WORKSPACE_DIR);
      log('未在配置中找到工作空间，使用默认值', 'WARN');
    }
  } catch (error) {
    logError('读取 openclaw.json 失败，回退到扫描目录', error);
    // 回退到旧的扫描方式
    return getAllWorkspaceDirsFallback();
  }
  
  return workspaces;
}

/**\ * 获取所有工作空间目录（回退方案：扫描目录）
 */
function getAllWorkspaceDirsFallback() {
  const homeDir = os.homedir();
  const workspaces = [];
  
  try {
    const entries = fs.readdirSync(homeDir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isDirectory()) {
        const dirPath = path.join(homeDir, entry.name);
        const agentsMdPath = path.join(dirPath, 'AGENTS.md');
        if (fs.existsSync(agentsMdPath)) {
          workspaces.push(dirPath);
          log(`扫描发现工作空间: ${dirPath}`, 'DEBUG');
        }
      }
    }
  } catch (error) {
    logError('扫描工作空间目录失败', error);
  }
  
  // 确保默认工作空间在列表中
  if (!workspaces.includes(DEFAULT_WORKSPACE_DIR)) {
    workspaces.push(DEFAULT_WORKSPACE_DIR);
  }
  
  return workspaces;
}

/**
 * 格式化本地时间为 YYYY-MM-DD HH:mm:ss
 */
function formatLocalTime() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

/**
 * 写入日志到文件和控制台
 */
function log(message, level = 'INFO') {
  const timestamp = formatLocalTime();
  const logEntry = `[${timestamp}] [${level}] ${message}\n`;

  // 写入控制台
  console.log(`[mars-fund-context-injector] ${message}`);

  // 写入日志文件（确保目录存在）
  try {
    const logDir = path.dirname(LOG_FILE);
    if (!fs.existsSync(logDir)) {
      fs.mkdirSync(logDir, { recursive: true });
    }
    fs.appendFileSync(LOG_FILE, logEntry, 'utf-8');
  } catch (error) {
    console.error(`[mars-fund-context-injector] Failed to write to log file: ${error.message}`);
  }
}

/**
 * 记录错误
 */
function logError(message, error) {
  log(message, 'ERROR');
  if (error) {
    log(`Error details: ${error.message}`, 'ERROR');
    if (error.stack) {
      log(`Stack trace: ${error.stack}`, 'ERROR');
    }
  }
}

/**
 * 记录对象摘要(只记录类型和大小，不打印完整内容)
 */
function logObject(message, obj) {
  log(message, 'DEBUG');
  try {
    const type = Array.isArray(obj) ? 'Array' : typeof obj;
    const size = JSON.stringify(obj).length;
    const keys = obj && typeof obj === 'object' ? Object.keys(obj).slice(0, 5).join(', ') : 'N/A';
    const moreKeys = obj && typeof obj === 'object' && Object.keys(obj).length > 5 ? '...' : '';
    log(`Object type: ${type}, size: ${size} bytes, keys: [${keys}${moreKeys}]`, 'DEBUG');
  } catch (error) {
    log(`Failed to analyze object: ${error.message}`, 'ERROR');
  }
}

/**
 * 写入 context 文件到多个目录
 * - 全局目录: ~/.openclaw/.cache
 * - 所有工作空间: <workspace>/.cache
 */
function writeContextFile(context) {
  const filename = 'openclaw_context.json';
  const content = JSON.stringify(context, null, 2);
  
  // 1. 写入全局目录
  const globalCacheDir = getGlobalCacheDir();
  const globalPath = path.join(globalCacheDir, filename);
  try {
    if (!fs.existsSync(globalCacheDir)) {
      fs.mkdirSync(globalCacheDir, { recursive: true });
    }
    fs.writeFileSync(globalPath, content, 'utf-8');
    log(`Context written to global: ${globalPath}`, 'INFO');
  } catch (error) {
    logError(`Failed to write to global: ${globalPath}`, error);
  }
  
  // 2. 写入所有工作空间
  const workspaces = getAllWorkspaceDirs();
  for (const workspaceDir of workspaces) {
    const cacheDir = path.join(workspaceDir, '.cache');
    const filePath = path.join(cacheDir, filename);
    try {
      if (!fs.existsSync(cacheDir)) {
        fs.mkdirSync(cacheDir, { recursive: true });
      }
      fs.writeFileSync(filePath, content, 'utf-8');
      log(`Context written to workspace: ${filePath}`, 'INFO');
    } catch (error) {
      logError(`Failed to write to workspace: ${filePath}`, error);
    }
  }
}

/**
 * 获取默认的 USER.md 内容
 */
function getDefaultUserMdContent() {
  return `# USER.md - 关于你的人类

_了解你在帮助的人。随着交流不断更新。_

- **名字：**
- **怎么称呼：**
- **代词：** _（可选）_
- **时区：**
- **备注：**

## 上下文

_他们在乎什么？在做什么项目？什么让他们烦躁？什么让他们发笑？随着时间积累这些认知。_

<!-- AUTO_UPDATE_START -->
<!-- AUTO_UPDATE_END -->
`;
}

/**
 * 写入 USER.md 到所有工作空间
 * 包含兜底策略：如果 API 失败或内容有问题，保留旧内容
 */
async function writeUserMdToAllWorkspaces(deptInstruction, userInfo) {
  const workspaces = getAllWorkspaceDirs();
  const timestamp = formatLocalTime();
  
  // 检查 API 返回是否有效
  const hasValidData = deptInstruction && userInfo && 
    !JSON.stringify(deptInstruction).includes('error') && 
    !JSON.stringify(userInfo).includes('error');
  
  // 检查是否包含"失败"文字
  const deptStr = JSON.stringify(deptInstruction || {});
  const userStr = JSON.stringify(userInfo || {});
  const hasFailureText = deptStr.includes('失败') || userStr.includes('失败');
  
  if (!hasValidData || hasFailureText) {
    log('API 返回数据无效或包含失败信息，写入无权限提示', 'WARN');
    log(`hasValidData: ${hasValidData}, hasFailureText: ${hasFailureText}`, 'WARN');
    
    // 写入无权限提示
    const errorContent = `<!-- AUTO_UPDATE_START -->

## 权限提示

用户无CRM系统权限，暂时无法使用\`thfund-sales-assistant\`技能查询销售域数据。

---

**更新时间**: ${timestamp}

<!-- AUTO_UPDATE_END -->`;
    
    // 写入所有工作空间
    for (const workspaceDir of workspaces) {
      const userMdPath = path.join(workspaceDir, 'USER.md');
      try {
        let content = fs.existsSync(userMdPath) ? fs.readFileSync(userMdPath, 'utf-8') : getDefaultUserMdContent();
        
        // 检查并追加标记
        const startMarker = '<!-- AUTO_UPDATE_START -->';
        const endMarker = '<!-- AUTO_UPDATE_END -->';
        let startIndex = content.indexOf(startMarker);
        let endIndex = content.indexOf(endMarker);
        
        if (startIndex === -1 || endIndex === -1) {
          content += '\n\n<!-- AUTO_UPDATE_START -->\n<!-- AUTO_UPDATE_END -->\n';
          startIndex = content.indexOf(startMarker);
          endIndex = content.indexOf(endMarker);
          fs.writeFileSync(userMdPath, content, 'utf-8');
        }
        
        const before = content.substring(0, startIndex);
        const after = content.substring(endIndex + endMarker.length);
        const finalContent = before + errorContent + after;
        
        fs.writeFileSync(userMdPath, finalContent, 'utf-8');
        log(`USER.md updated (no permission): ${userMdPath}`, 'INFO');
      } catch (error) {
        logError(`Failed to update USER.md: ${userMdPath}`, error);
      }
    }
    return;
  }
  
  // 提取内容
  const deptPrompt = deptInstruction.tool_prompt || deptInstruction.answer_prompt || '无数据权限信息';
  const userPrompt = userInfo.prompt || userInfo.tool_prompt || '无用户信息';
  const adjustedDeptPrompt = adjustSystemTitle(deptPrompt);
  
  // 构建新的自动更新内容
  const newContent = `<!-- AUTO_UPDATE_START -->

${userPrompt}

---

${adjustedDeptPrompt}

---

**更新时间**: ${timestamp}

<!-- AUTO_UPDATE_END -->`;

  // 写入所有工作空间
  for (const workspaceDir of workspaces) {
    const userMdPath = path.join(workspaceDir, 'USER.md');
    try {
      // 读取现有内容
      let content = '';
      if (fs.existsSync(userMdPath)) {
        content = fs.readFileSync(userMdPath, 'utf-8');
      } else {
        // 如果文件不存在，创建默认内容
        content = getDefaultUserMdContent();
      }
      
      // 检查标记是否存在
      const startMarker = '<!-- AUTO_UPDATE_START -->';
      const endMarker = '<!-- AUTO_UPDATE_END -->';
      let startIndex = content.indexOf(startMarker);
      let endIndex = content.indexOf(endMarker);
      
      // 如果标记不存在，在文件末尾追加标记区域
      if (startIndex === -1 || endIndex === -1) {
        log(`USER.md 缺少 AUTO_UPDATE 标记，自动追加: ${userMdPath}`, 'INFO');
        // 在文件末尾追加标记区域
        content += '\n\n<!-- AUTO_UPDATE_START -->\n<!-- AUTO_UPDATE_END -->\n';
        startIndex = content.indexOf(startMarker);
        endIndex = content.indexOf(endMarker);
        // 先写入带标记的内容，确保文件有标记
        fs.writeFileSync(userMdPath, content, 'utf-8');
      }
      
      // 替换内容
      const before = content.substring(0, startIndex);
      const after = content.substring(endIndex + endMarker.length);
      const finalContent = before + newContent + after;
      
      fs.writeFileSync(userMdPath, finalContent, 'utf-8');
      log(`USER.md updated: ${userMdPath}`, 'INFO');
      
    } catch (error) {
      logError(`Failed to update USER.md: ${userMdPath}`, error);
    }
  }
}

/**
 * 调整体系标题
 */
function adjustSystemTitle(text) {
  return text.replace(/^## 体系\(pdept\)和团队\(dept\)/gm, '## 数据查询权限体系\(pdept\)和团队\(dept\)');
}

module.exports = async function(event) {
  const startTime = Date.now();
  log('=== Hook triggered ===', 'INFO');

  // 记录完整的事件对象
  logObject('Event object', event);

  // OpenClaw 事件对象结构(参考 bundled hooks)
  const eventType = event.type;
  const action = event.action;
  const sessionKey = sanitizeOssPath(event.sessionKey);
  
  // 从 sessionKey 提取 sessionId，或使用 event.sessionId，或生成随机值
  // sessionKey 格式: "agent:main:session_1778725159537_mle5q6" -> sessionId: "session_1778725159537_mle5q6"
  let sessionId = sanitizeOssPath(event.sessionId);
  if (!sessionId && sessionKey) {
    // 从 sessionKey 提取最后一部分作为 sessionId
    const parts = sessionKey.split(':');
    if (parts.length > 0) {
      sessionId = parts[parts.length - 1];
    }
  }
  if (!sessionId) {
    sessionId = `session_${crypto.randomUUID()}`;
  }
  
  // runId 生成：优先使用 event.runId，否则基于 sessionId 生成
  let runId = sanitizeOssPath(event.runId);
  if (!runId) {
    // 从 sessionId 生成 runId（去掉 session_ 前缀）
    runId = `run_${sessionId.replace(/^session_/, '')}`;
  }
  
  // 从 event.context 获取工作空间目录，否则使用默认值
  const context = event.context || {};
  const WORKSPACE_DIR = context.workspaceDir || DEFAULT_WORKSPACE_DIR;
  
  // 用户信息缓存文件（使用全局目录）
  const USER_INFO_CACHE_FILE = path.join(getGlobalCacheDir(), 'mars-fund-user-info-last-update.json');
  
  log(`Workspace dir: ${WORKSPACE_DIR}`, 'INFO');
  log(`Global cache dir: ${getGlobalCacheDir()}`, 'INFO');

  log(`Event type: ${eventType}, action: ${action}`, 'INFO');
  log(`Session key: ${sessionKey}`, 'INFO');
  log(`Session ID: ${sessionId}`, 'INFO');
  log(`Run ID: ${runId}`, 'INFO');

  // 获取 accessToken（通过 get_latest_token API）
  // 只调用一次，后续复用
  let accessToken = '';
  try {
    accessToken = await getAccessToken();
    log(`Access token length: ${accessToken.length}`, 'INFO');
    log(`Access token preview: ${accessToken.substring(0, 50)}...`, 'DEBUG');
  } catch (error) {
    logError('Failed to get access token', error);
    // 继续执行，使用空 token
  }

  // 判断是否需要更新用户信息
  const shouldUpdateUserInfo =
    // command 事件:new, reset, clear, compact 总是更新
    (eventType === 'command' && ['new', 'reset', 'clear', 'compact'].includes(action)) ||
    // message 事件:检查是否超过更新间隔
    (eventType === 'message' && shouldUpdateUserInfoBasedOnCache(USER_INFO_CACHE_FILE));

  log(`Should update user info: ${shouldUpdateUserInfo}`, 'INFO');

  if (shouldUpdateUserInfo && accessToken) {
    log(`Updating user info (eventType: ${eventType}, action: ${action})...`, 'INFO');

    try {
      // 1. 调用 get_dept_instruction
      log('Calling get_dept_instruction API...', 'INFO');
      const deptStartTime = Date.now();
      const deptInstruction = await callHttpApi('/get_dept_instruction', accessToken, sessionId, runId);
      const deptDuration = Date.now() - deptStartTime;
      log(`get_dept_instruction completed in ${deptDuration}ms`, 'INFO');
      logObject('get_dept_instruction result', deptInstruction);

      // 2. 调用 get_user_info
      log('Calling get_user_info API...', 'INFO');
      const userStartTime = Date.now();
      const userInfo = await callHttpApi('/get_user_info', accessToken, sessionId, runId);
      const userDuration = Date.now() - userStartTime;
      log(`get_user_info completed in ${userDuration}ms`, 'INFO');
      logObject('get_user_info result', userInfo);

      // 3. 写入 USER.md 到所有工作空间（带兜底策略）
      log('Updating USER.md in all workspaces...', 'INFO');
      await writeUserMdToAllWorkspaces(deptInstruction, userInfo);
      log('USER.md updated in all workspaces', 'INFO');

      // 4. 更新缓存时间戳
      updateUserInfoCacheTimestamp(USER_INFO_CACHE_FILE);

    } catch (error) {
      logError('Error updating user info', error);
      // 不抛出错误,避免阻塞命令执行
    }
  }

  // 构建上下文信息
  // sessionId 和 runId 已在前面确保有值
  const openclawContext = {
    runId: runId,
    sessionId: sessionId,
    sessionKey: sessionKey || '',
    accessToken: accessToken || '',
    timestamp: formatLocalTime()
  };

  // 写入 context 文件到所有目录
  writeContextFile(openclawContext);
  logObject('Context content', openclawContext);

  const totalDuration = Date.now() - startTime;
  log(`=== Hook completed in ${totalDuration}ms ===`, 'INFO');

  return event;
};

/**
 * 获取 API 服务地址（默认使用生产环境）
 */
function getApiUrl() {
  const url = 'http://mars-fund-mcp.ai-assistant.svc.cluster.local';
  log(`Using production API URL: ${url}`, 'DEBUG');
  return url;
}

/**
 * 调用 get_latest_token 接口获取 access_token
 */
async function getLatestAccessToken() {
  log('Calling get_latest_token API...', 'INFO');
  
  const username = process.env.IAM_USERNAME || '';
  const code = process.env.IAM_CODE || '';
  const refreshToken = process.env.IAM_REFRESH_TOKEN || '';
  
  log(`IAM_USERNAME: ${username}`, 'DEBUG');
  log(`IAM_CODE: ${code.substring(0, 20)}...`, 'DEBUG');
  log(`IAM_REFRESH_TOKEN length: ${refreshToken.length}`, 'DEBUG');
  
  if (!username || !code || !refreshToken) {
    const error = new Error('Missing required environment variables: IAM_USERNAME, IAM_CODE, or IAM_REFRESH_TOKEN');
    logError('Missing required environment variables', error);
    throw error;
  }
  
  return new Promise((resolve, reject) => {
    const url = 'https://algoplatform.thfund.work/assistant/workspace-dispatcher/api/get_latest_token';
    
    const requestData = {
      username: username,
      code: code,
      refresh_token: refreshToken
    };
    
    const requestBody = JSON.stringify(requestData);
    
    log(`get_latest_token URL: ${url}`, 'DEBUG');
    log(`Request body length: ${requestBody.length} bytes`, 'DEBUG');
    
    // 解析 URL
    const urlObj = new URL(url);
    const isHttps = urlObj.protocol === 'https:';
    const httpModule = isHttps ? https : http;
    
    const options = {
      hostname: urlObj.hostname,
      port: urlObj.port || (isHttps ? 443 : 80),
      path: urlObj.pathname + urlObj.search,
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(requestBody)
      },
      timeout: 30000
    };
    
    const req = httpModule.request(options, (res) => {
      let data = '';
      
      log(`get_latest_token response status: ${res.statusCode} ${res.statusMessage}`, 'DEBUG');
      
      res.on('data', (chunk) => {
        data += chunk;
      });
      
      res.on('end', () => {
        try {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            const result = JSON.parse(data);
            log(`get_latest_token response parsed successfully`, 'DEBUG');
            
            if (result.access_token) {
              log(`Access token received, length: ${result.access_token.length}`, 'INFO');
              resolve(result.access_token);
            } else {
              const error = new Error('get_latest_token response missing access_token field');
              logError('get_latest_token response missing access_token', error);
              reject(error);
            }
          } else {
            const error = new Error(`get_latest_token HTTP ${res.statusCode}: ${res.statusMessage}`);
            error.statusCode = res.statusCode;
            error.response = data;
            logError('get_latest_token HTTP request failed', error);
            log(`Response body (first 500 chars): ${data.substring(0, 500)}...`, 'DEBUG');
            reject(error);
          }
        } catch (parseError) {
          logError('Failed to parse get_latest_token response', parseError);
          log(`Response data (first 500 chars): ${data.substring(0, 500)}...`, 'DEBUG');
          reject(parseError);
        }
      });
    });
    
    req.on('error', (error) => {
      logError('get_latest_token HTTP request error', error);
      reject(error);
    });
    
    req.on('timeout', () => {
      req.destroy();
      const timeoutError = new Error('get_latest_token request timeout after 30 seconds');
      logError('get_latest_token request timeout', timeoutError);
      reject(timeoutError);
    });
    
    req.write(requestBody);
    req.end();
  });
}

/**
 * 获取 access_token（每次都调用 API，不缓存）
 */
async function getAccessToken() {
  return await getLatestAccessToken();
}

/**
 * 获取 rootDir（默认使用生产环境）
 */
function getRootDir() {
  return '/mars/prod/agent/tool';
}

/**
 * 调用 HTTP API
 */
function callHttpApi(endpoint, accessToken, sessionId, runId) {
  return new Promise((resolve, reject) => {
    const baseUrl = getApiUrl();
    const url = baseUrl + endpoint;
    const rootDir = getRootDir();
    
    log(`API endpoint: ${endpoint}`, 'DEBUG');
    log(`Full API URL: ${url}`, 'DEBUG');
    
    // 构建请求 headers
    const headers = {
      'accessToken': accessToken,
      'sessionId': sessionId,
      'requestId': runId || crypto.randomUUID(),
      'rootDir': rootDir,
      'isiamtoken': 'True',
      'Content-Type': 'application/json'
    };
    
    log(`API Request: ${endpoint}`, 'DEBUG');
    log(`URL: ${url}`, 'DEBUG');
    log(`Method: POST`, 'DEBUG');
    log(`Headers count: ${Object.keys(headers).length}`, 'DEBUG');
    
    logObject('Request headers', {
      ...headers,
      'accessToken': previewToken(headers.accessToken)
    });
    
    // 解析 URL
    const urlObj = new URL(url);
    const isHttps = urlObj.protocol === 'https:';
    const httpModule = isHttps ? https : http;
    
    const options = {
      hostname: urlObj.hostname,
      port: urlObj.port || (isHttps ? 443 : 80),
      path: urlObj.pathname + urlObj.search,
      method: 'POST',
      headers: headers,
      timeout: 30000
    };

    logObject('HTTP request options', {
      ...options,
      headers: {
        ...options.headers,
        'accessToken': previewToken(options.headers.accessToken)
      }
    });

    const req = httpModule.request(options, (res) => {
      let data = '';

      log(`HTTP response status: ${res.statusCode} ${res.statusMessage}`, 'DEBUG');
      logObject('Response headers', res.headers);

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        log(`Response data length: ${data.length} bytes`, 'DEBUG');
        
        try {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            const result = JSON.parse(data);
            log(`Successfully parsed JSON response`, 'DEBUG');
            const resultSummary = { ...result };
            if (resultSummary.data) {
              delete resultSummary.data;
              log('Removed data field from response summary to reduce log size', 'DEBUG');
            }
            logObject('Response summary', resultSummary);
            resolve(result);
          } else {
            const error = new Error(`HTTP ${res.statusCode}: ${res.statusMessage}`);
            error.statusCode = res.statusCode;
            error.response = data;
            logError(`HTTP request failed with status ${res.statusCode}`, error);
            log(`Response body (first 500 chars): ${data.substring(0, 500)}...`, 'DEBUG');
            reject(error);
          }
        } catch (parseError) {
          logError('Failed to parse JSON response', parseError);
          log(`Response data (first 500 chars): ${data.substring(0, 500)}...`, 'DEBUG');
          reject(parseError);
        }
      });
    });

    req.on('error', (error) => {
      logError('HTTP request error', error);
      reject(error);
    });
    
    req.on('timeout', () => {
      req.destroy();
      const timeoutError = new Error('Request timeout after 30 seconds');
      logError('Request timeout', timeoutError);
      reject(timeoutError);
    });
    
    const requestBody = JSON.stringify({});
    log(`Request body: ${requestBody}`, 'DEBUG');
    log(`Request body length: ${requestBody.length} bytes`, 'DEBUG');
    req.write(requestBody);
    req.end();
  });
}

/**
 * Token 预览(只显示前 50 个字符)
 */
function previewToken(token) {
  if (!token) return 'null';
  return `${token.substring(0, 50)}... (length: ${token.length})`;
}

/**
 * 检查是否需要更新用户信息(基于缓存时间戳)
 */
function shouldUpdateUserInfoBasedOnCache(userInfoCacheFile) {
  try {
    if (!fs.existsSync(userInfoCacheFile)) {
      log('Cache file not found, should update', 'INFO');
      return true;
    }

    const cacheData = JSON.parse(fs.readFileSync(userInfoCacheFile, 'utf-8'));
    const lastUpdate = new Date(cacheData.timestamp).getTime();
    const now = Date.now();
    const elapsed = now - lastUpdate;
    const elapsedMinutes = Math.round(elapsed / 1000 / 60);

    log(`Last update: ${cacheData.timestamp}`, 'INFO');
    log(`Elapsed time: ${elapsedMinutes} minutes`, 'INFO');

    if (elapsed > USER_INFO_UPDATE_INTERVAL) {
      log(`Cache expired (${elapsedMinutes} minutes > ${USER_INFO_UPDATE_INTERVAL / 1000 / 60} minutes), should update`, 'INFO');
      return true;
    }

    log('Cache still valid, skip update', 'INFO');
    return false;

  } catch (error) {
    logError('Error checking cache, will update', error);
    return true;
  }
}

/**
 * 更新用户信息缓存时间戳
 */
function updateUserInfoCacheTimestamp(userInfoCacheFile) {
  try {
    const cacheData = {
      timestamp: formatLocalTime()
    };
    
    const dir = path.dirname(userInfoCacheFile);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    
    fs.writeFileSync(userInfoCacheFile, JSON.stringify(cacheData, null, 2), 'utf-8');
    log(`Cache timestamp updated: ${cacheData.timestamp}`, 'INFO');
  } catch (error) {
    logError('Failed to update cache timestamp', error);
  }
}

