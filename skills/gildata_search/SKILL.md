---
name: gildata_search
description: "金融数据库查询工具。**优先用于：**查询股票/基金财务数据(营收/利润/ROE/毛利率)、财务报表(三大表)、行情数据、估值指标。提供一手原始数据，比研报更准确及时。**典型场景：**写公司分析报告、财报点评、估值分析、财务分析时需要具体数字和数据。"
metadata:
  {
    "category": "data-query",
    "database": "gildata",
    "tables": 1372,
    "fields": 37218,
  }
---

# 恒生聚源数据库查询技能

根据用户自然语言问题，智能检索恒生聚源数据库相关表和字段，辅助LLM生成SQL查询和数据分析代码。

## ⭐ 优先使用原则

**当用户需要以下数据时，应优先使用本技能而非搜索研报：**
- 股票财务报表数据（资产负债表、利润表、现金流量表）
- 财务指标（ROE、毛利率、净利率、EPS等）
- 股票/指数行情数据
- 基金净值、持仓数据
- 债券、期货数据

**原因**：聚源数据库提供原始、准确、及时的一手数据，而研报中的数据是二手整理，可能存在滞后或偏差。

## 执行流程（决策树）

> **注意**：以下命令均在 `gildata_search` 目录下执行。如果路径不同，请相应调整。

```
用户需要股票/基金/债券/指数数据
│
├─ 是标准查询场景？（如查股票财务、行情、估值）
│   │
│   ├─ ✅ 先用【快捷查询脚本】（见下方列表）
│   │   │
│   │   ├─ 脚本执行成功 → 完成
│   │   └─ 报错（如 Table doesn't exist）→ 记录缺失的表
│   │
│   └─ 搜索替代表 → python scripts/search.py "缺失的数据"
│       │
│       ├─ 找到可用表 → 修改脚本使用该表
│       └─ 仍找不到 → 用 search 自定义查询（见下文）
│
└─ 是非标准/复杂查询？
    │
    └─ 直接用【表搜索工具】
        Step 1: 检索相关表 → python scripts/search.py "用户问题"
        Step 2: 筛选核心表 → 检查 path 字段，忽略空path
        Step 3: 查看表结构 → python scripts/search.py --table {表名}
        Step 4: 创建脚本 → 使用下方模板
        Step 5: 执行测试 → python xxx.py
```

**核心原则：快捷脚本是首选，失败时才搜索表结构！**

## ⚠️ 脚本存放位置

**生成的Python脚本应存放在用户当前工作目录，而非skill目录下！**

```
✅ 正确: ./my_analysis/xxx.py  (用户工作目录)
❌ 错误: ./gildata_search/scripts/xxx.py  (技能目录内部)
```

**原因**：脚本属于用户的工作产出，应放在用户可见和管理的目录中。

---

## ⚠️ 重要提醒

### 表不存在错误

如果执行时出现 **"Table 'gildata.xxx' doesn't exist"** 错误：

```
原因: 该表需要额外权限，当前账号无访问权限
解决: 联系恒生聚源开通相应表的访问权限
```

**常见需要额外权限的表**：
- 期货相关表 (`fut_*`)
- 高频数据表
- 部分衍生指标表

---

## 核心速查表

### 常用表一览

| 表名 | MySQL表名 | 用途 | 日期字段 | ID字段 |
|------|-----------|------|----------|--------|
| SecuMain | secumain | 证券主表 | - | InnerCode |
| QT_IndexQuote | qt_indexquote | 交易所指数行情 | TradingDay | InnerCode |
| QT_CSIIndexQuote | qt_csiindexquote | 中证指数行情(含PE) | TradingDay | IndexCode |
| MF_NetValue | mf_netvalue | 基金净值 | **EndDate** | InnerCode |
| LC_DIndicesForValuation | lc_dindicesforvaluation | **股票**估值 | TradingDay | InnerCode |
| QT_StockPerformance | qt_stockperformance | 股票行情表现 | TradingDay | InnerCode |
| Index_RiskAnalysis | index_riskanalysis | 指数风险指标 | TradingDay | IndexCode |
| LC_IndexComponentsWeight | lc_indexcomponentsweight | 指数成分股权重 | EndDate | IndexCode |

### 📊 财务报表与指标表（查询公司基本面必用）

| 表名 | MySQL表名 | 用途 | 日期字段 | ID字段 |
|------|-----------|------|----------|--------|
| **LC_MainIndexNew** | lc_mainindexnew | **公司主要财务分析指标**（273个字段） | EndDate | CompanyCode |
| LC_BalanceSheetAll | lc_balancesheetall | 资产负债表（全部科目） | EndDate | CompanyCode |
| LC_IncomeStatementAll | lc_incomestatementall | 利润表（全部科目） | EndDate | CompanyCode |
| LC_CashFlowStatementAll | lc_cashflowstatementall | 现金流量表（全部科目） | EndDate | CompanyCode |
| LC_FinancialIndicator | lc_financialindicator | 财务指标（精选） | EndDate | CompanyCode |
| LC_DerivativeData | lc_derivativedata | 财务衍生数据 | EndDate | CompanyCode |

**LC_MainIndexNew 核心字段（最常用）：**
- **每股指标**: BasicEPS(基本每股收益), NetAssetPS(每股净资产), OperCashFlowPS(每股经营现金流)
- **盈利能力**: ROEAvg(净资产收益率), GrossIncomeRatio(销售毛利率), NetProfitRatio(销售净利率)
- **偿债能力**: CurrentRatio(流动比率), QuickRatio(速动比率), DebtAssetsRatio(资产负债率)
- **成长能力**: OperatingRevenueGrowRate(营收增速), NetProfitGrowRate(净利润增速)
- **现金流**: NetOperateCashFlow(经营现金流净额)
- **分红**: DividendPS(每股股利), DividendPaidRatio(股利支付率)

### ⚠️ 日期字段对照（易错！）

| 表类型 | 日期字段 | 示例 |
|--------|----------|------|
| 指数/股票行情 | `TradingDay` | qt_indexquote |
| **基金净值** | `EndDate` ⚠️ | mf_netvalue |
| 期货行情 | `TradingDay` | fut_dailyquote |

### 指数代码与表对应

| 指数代码 | 指数名称 | 使用表 | ID字段 |
|----------|----------|--------|--------|
| 000001 | 上证指数 | qt_indexquote | InnerCode |
| 000300 | 沪深300 | qt_csiindexquote | IndexCode |
| 399006 | 创业板指 | qt_indexquote | InnerCode |
| 000905 | 中证500 | qt_csiindexquote | IndexCode |
| 000688 | 科创50 | qt_csiindexquote | IndexCode |
| 931643 | 双创50 | qt_csiindexquote | IndexCode |

**重要提示**:
- `qt_csiindexquote` 包含指数PE(`IndexPERatio1`)、股息率(`IndexDYRatio1`)等估值数据
- 查询指数估值时优先使用 `qt_csiindexquote`
- `IndexCode` 实际是指数的 `InnerCode`，需要先从 `secumain` 获取

### IndicatorType 指标类型

**Index_RiskAnalysis (风险指标)**: 10=贝塔, 11=最大回撤, 13=VaR, 15=波动率, 21=下行标准差

**Index_ReturnAnalysis (收益指标)**: 1=夏普比率, 3=信息比率, 4=特雷诺, 5=詹森, 28=阿尔法

### SecuCategory 证券类别

1=A股, 4=指数, 8=开放式基金, 10=其他(含期货)

---

## 脚本模板

```python
#!/usr/bin/env python3
"""
功能: [描述]
用法: python {脚本名}.py
数据表:
  - 表名1 (用途)
"""

import pymysql
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime, timedelta
import re

# ============ 中文字体设置 ============
def setup_chinese_font():
    """自动检测系统中可用的中文字体"""
    from matplotlib import font_manager
    chinese_fonts = ['Noto Sans CJK SC', 'Noto Sans CJK JP', 'SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
    available = [f.name for f in font_manager.fontManager.ttflist]
    for font in chinese_fonts:
        if font in available:
            plt.rcParams['font.sans-serif'] = [font]
            plt.rcParams['axes.unicode_minus'] = False
            return
    for f in font_manager.fontManager.ttflist:
        if any(k in f.name.lower() for k in ['cjk', 'chinese', 'noto sans', 'source han']):
            plt.rcParams['font.sans-serif'] = [f.name]
            plt.rcParams['axes.unicode_minus'] = False
            return

setup_chinese_font()

# ============ 配置 ============
SECURITY_CODE = '000300'  # 证券代码
SECUCATEGORY = 4          # 1=A股, 4=指数, 8=基金

# ============ 工具函数 ============
def load_config(config_path='config/config.yaml'):
    """加载配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def parse_env(value):
    """解析 ${VAR:-default} 格式"""
    if not isinstance(value, str): return value
    m = re.search(r'\$\{[^:]+:-([^}]+)\}', value)
    return m.group(1) if m else value

def get_conn(config):
    """从配置文件获取数据库连接"""
    m = config.get('mysql', {})
    return pymysql.connect(
        host=parse_env(m.get('host', os.environ.get('GIL_MYSQL_HOST', 'localhost'))),
        port=m.get('port', 3306),
        user=parse_env(m.get('user', 'root')),
        password=parse_env(m.get('password', '')),
        database=parse_env(m.get('database', 'gildata')),
        charset='utf8mb4'
    )

def safe_float(v):
    """安全转换Decimal为float"""
    return float(v) if v is not None else np.nan

def get_inner_code(conn, code, category=4):
    """获取InnerCode"""
    with conn.cursor() as cur:
        cur.execute("SELECT InnerCode,SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=%s LIMIT 1", (code, category))
        r = cur.fetchone()
    return {'InnerCode': r[0], 'Name': r[1]} if r else None

# ============ 主逻辑 ============
def main():
    config = load_config()
    conn = get_conn(config)
    try:
        info = get_inner_code(conn, SECURITY_CODE, SECUCATEGORY)
        if not info:
            print(f"未找到证券: {SECURITY_CODE}")
            return
        print(f"证券: {info['Name']} ({SECURITY_CODE}), InnerCode={info['InnerCode']}")
        # TODO: 在此添加查询逻辑
    finally:
        conn.close()

if __name__ == "__main__":
    main()
```

---

## 快捷脚本故障排查

当快捷脚本报错时，按以下流程处理：

### 场景1：Table doesn't exist（表不存在）

```bash
# 1. 查看脚本源码，找到报错的表名
# 例如报错: Table 'gildata.lc_mainindexnew' doesn't exist

# 2. 搜索该表的替代表
python scripts/search.py "公司财务指标 ROE EPS" --available

# 3. 查看替代表结构，确认字段是否匹配
python scripts/search.py --table LC_FinancialIndicator

# 4. 复制脚本到工作目录，修改表名
# 修改后重新执行
```

### 场景2：Unknown column（字段不存在）

```bash
# 例如报错: Unknown column 'TotalOperatingRevenue'

# 1. 搜索该字段的正确名称
python scripts/search.py "营业总收入 营业收入" --available

# 2. 查看表结构，找到正确字段名
python scripts/search.py --table LC_IncomeStatementAll

# 3. 修改脚本中的字段名
```

### 场景3：快捷脚本完全无法满足需求

```bash
# 1. 直接用自然语言搜索
python scripts/search.py "用户原始需求"

# 2. 查看表结构
python scripts/search.py --table 找到的表名

# 3. 参考脚本模板写自定义查询
```

---

## 常见错误与解决方案

### 1. Table doesn't exist
```
错误: Table 'gildata.xxx' doesn't exist
原因: 该表需要额外权限
解决: 
  1. 搜索替代表: python scripts/search.py "相同功能的数据"
  2. 联系恒生聚源开通访问权限
```

### 2. Unknown column 'TradingDay'
```
错误: Unknown column 'TradingDay' in 'where clause'
原因: 基金净值表使用 EndDate
解决: 参考「日期字段对照表」
```

### 3. Decimal 计算错误
```
错误: TypeError: unsupported operand type(s) for /: 'decimal.Decimal'
解决: df['col'] = df['col'].apply(float) 或 safe_float()
```

### 4. 中文显示方框

**原因**: matplotlib默认使用英文字体，无法渲染中文字符

**解决方案**:

1. **安装中文字体** (推荐 Noto Sans CJK):
```bash
# Ubuntu/Debian
sudo apt install fonts-noto-cjk

# CentOS/RHEL
sudo yum install google-noto-sans-cjk-fonts
```

2. **清除matplotlib字体缓存**:
```bash
rm -rf ~/.cache/matplotlib
```

3. **在脚本中使用 setup_chinese_font()**:
```python
def setup_chinese_font():
    from matplotlib import font_manager
    # 注意: Noto CJK字体可能显示为 JP/SC/TC 等变体名称
    chinese_fonts = [
        'Noto Sans CJK SC', 'Noto Sans CJK JP',  # Noto CJK (最常见)
        'SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei',
        'Source Han Sans SC', 'PingFang SC'
    ]
    available = [f.name for f in font_manager.fontManager.ttflist]
    for font in chinese_fonts:
        if font in available:
            plt.rcParams['font.sans-serif'] = [font]
            plt.rcParams['axes.unicode_minus'] = False
            return font
    # 模糊匹配 (备用方案)
    for f in font_manager.fontManager.ttflist:
        if any(k in f.name.lower() for k in ['cjk', 'chinese', 'noto sans', 'source han']):
            plt.rcParams['font.sans-serif'] = [f.name]
            plt.rcParams['axes.unicode_minus'] = False
            return f.name
    return None

setup_chinese_font()
```

4. **可选: 配置全局matplotlibrc** (`~/.config/matplotlib/matplotlibrc`):
```
font.sans-serif: Noto Sans CJK SC, SimHei, DejaVu Sans
axes.unicode_minus: False
```

### 5. pandas 频率参数
```
错误: ValueError: 'M' is no longer supported
解决: 使用 'ME' 代替 'M'
```

### 6. 指数估值查询错误
```
错误: lc_dindicesforvaluation 无指数PE数据
原因: lc_dindicesforvaluation 是股票估值表，不是指数估值表
解决: 使用 qt_csiindexquote 的 IndexPERatio1 字段
示例:
  SELECT IndexPERatio1, IndexDYRatio1 FROM qt_csiindexquote
  WHERE IndexCode = (SELECT InnerCode FROM secumain WHERE SecuCode='000300')
```

### 7. 股票行情表不存在
```
错误: Table 'gildata.qt_stockquote' doesn't exist
原因: qt_stockquote 表不存在
解决: 使用 qt_stockperformance 代替
```

### 8. 成分股权重表字段理解
```
lc_indexcomponentsweight 表:
- IndexCode: 是指数的InnerCode，需要先从secumain获取
- EndDate: 是权重生效日期，不是调出日期
- 查询最新成分股: WHERE EndDate = (SELECT MAX(EndDate) FROM lc_indexcomponentsweight WHERE IndexCode = ?)
```

### 9. 风险指标表字段名
```
Index_RiskAnalysis 表:
- 值字段: DataValueRM (近1月), DataValueRY (近1年), DataValueRW (近1周)
- 不是 RiskValue 或 ReturnValue
```

---

## 干扰表识别

搜索结果通过 path 字段过滤干扰表：

```
✅ path = "聚源新版数据库 > 指数数据库 > ..."
❌ path = "" 或不相关
```

## 🚀 快捷查询脚本（首选）

以下脚本封装了**高频场景的快速查询**，**应优先尝试使用**。

### 使用原则

| 场景 | 推荐做法 | 示例 |
|------|----------|------|
| 查股票财务数据 | 先用 `stock_finance.py` | `python scripts/stock_finance.py 600519 --type index` |
| 查股票行情 | 先用 `stock_technical.py` | `python scripts/stock_technical.py 600519 --ma` |
| 查股票估值 | 先用 `stock_valuation.py` | `python scripts/stock_valuation.py 600519 --history` |
| 查指数数据 | 先用 `index_query.py` | `python scripts/index_query.py 000300 --pe` |
| 以上脚本都失败 | 再用 `search` 查表 | `python scripts/search.py "ROE财务指标"` |

| 脚本 | 功能 | 用法 |
|------|------|------|
| stock_overview.py | 综合概览 | `python scripts/stock_overview.py 600519` |
| stock_info.py | 公司基本信息 | `python scripts/stock_info.py 600519 --full` |
| stock_finance.py | 财务报表/指标 | `python scripts/stock_finance.py 600519 --type index` |
| stock_valuation.py | 估值/分红 | `python scripts/stock_valuation.py 600519 --history` |
| stock_peer.py | 同行对比 | `python scripts/stock_peer.py 600519 --rank` |
| stock_revenue.py | 分项收入 | `python scripts/stock_revenue.py 600519 --detail` |
| stock_technical.py | 技术指标 | `python scripts/stock_technical.py 600519 --ma` |
| stock_forecast.py | 业绩预告 | `python scripts/stock_forecast.py 600519` |
| index_query.py | 指数数据 | `python scripts/index_query.py 000300 --pe` |
| bond_query.py | 债券数据 | `python scripts/bond_query.py --treasury` |
| fund_info.py | 基金业绩 | `python scripts/fund_info.py 008263 --rating` |
| fund_portfolio.py | 基金持仓 | `python scripts/fund_portfolio.py 008263 --allocation` |
| fund_manager.py | 基金经理 | `python scripts/fund_manager.py --name 张坤` |

**通用参数**: `-o output.xlsx` 导出Excel

### 快捷脚本详细用法

```bash
# 股票
python scripts/stock_info.py 600519[,000858] [--full]
python scripts/stock_finance.py 600519 --type {balance|income|cash|index} [--quarter] [--dupont]
python scripts/stock_valuation.py 600519 [--history] [--percentile] [--dividend]
python scripts/stock_peer.py 600519 [--rank] [--avg]
python scripts/stock_revenue.py 600519 [--year 2024] [--detail]
python scripts/stock_technical.py 600519 [--ma] [--volume] [--days 30]
python scripts/stock_forecast.py 600519

# 指数
python scripts/index_query.py 000300 [--pe] [--components] [--top 50]
python scripts/index_query.py --list
python scripts/index_query.py --top 20  # 涨幅排名

# 债券
python scripts/bond_query.py 170015
python scripts/bond_query.py --list [--treasury] [--corporate]

# 基金
python scripts/fund_info.py 008263 [--rating] [--history]
python scripts/fund_info.py --type 灵活配置 --top 10
python scripts/fund_portfolio.py 008263 [--allocation] [--industry]
python scripts/fund_manager.py --name 张坤 [--funds]
python scripts/fund_manager.py --company 天弘 --top 20
```

## 🔍 表搜索工具

### 自然语言搜索表
```bash
python scripts/search.py "基金净值"
```

### 只显示有数据的表
```bash
python scripts/search.py "基金净值" --available
```

### 查询表详情
```bash
python scripts/search.py --table MF_NetValue
```

### JSON 输出
```bash
python scripts/search.py "ROE" --json
```

---

## 维护命令

```bash
# 检查数据可用性
python scripts/check_availability.py

# 构建ES索引
python scripts/build_index.py
```
