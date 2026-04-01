# gildata_query vs gildata_search 测试用例对比

## 测试用例设计

### Case 1: 查询单只股票财务指标
**需求**: 查询贵州茅台(600519)最近5年的ROE和毛利率

**gildata_query 执行方式**:
```bash
# Step 1: 搜索相关表
python scripts/search_tables.py "ROE 毛利率 贵州茅台"

# Step 2: 查看表结构
# 需要查看 resource/LC_MainIndexNew.md

# Step 3: 编写自定义脚本执行
```

**gildata_search 执行方式**:
```bash
# 直接使用快捷脚本
python scripts/stock_finance.py 600519 --type index
```

---

### Case 2: 查询指数估值数据
**需求**: 查询沪深300指数(000300)的历史PE和PB数据

**gildata_query 执行方式**:
```bash
# Step 1: 搜索相关表
python scripts/search_tables.py "沪深300 PE PB 估值"

# Step 2: 查看表结构
# 需要查看 resource/qt_csiindexquote.md

# Step 3: 编写自定义脚本执行
```

**gildata_search 执行方式**:
```bash
# 直接使用快捷脚本
python scripts/index_query.py 000300 --pe --history
```

---

### Case 3: 查询基金持仓信息
**需求**: 查询某只基金(008263)的最新持仓和行业分布

**gildata_query 执行方式**:
```bash
# Step 1: 搜索相关表
python scripts/search_tables.py "基金持仓 行业分布"

# Step 2: 查看表结构
# 需要查看 resource/MF_StockPortfolioDetail.md

# Step 3: 编写自定义脚本执行
```

**gildata_search 执行方式**:
```bash
# 直接使用快捷脚本
python scripts/fund_portfolio.py 008263 --allocation --industry
```

---

### Case 4: 查询股票技术指标
**需求**: 查询宁德时代(300750)的30日均线和成交量数据

**gildata_query 执行方式**:
```bash
# Step 1: 搜索相关表
python scripts/search_tables.py "均线 MA 成交量 行情"

# Step 2: 查看表结构
# 需要查看 resource/qt_stockperformance.md

# Step 3: 编写自定义脚本执行
```

**gildata_search 执行方式**:
```bash
# 直接使用快捷脚本
python scripts/stock_technical.py 300750 --ma --volume --days 30
```

---

### Case 5: 查询同行对比数据
**需求**: 对比白酒行业头部公司(茅台、五粮液、泸州老窖)的营收和净利润

**gildata_query 执行方式**:
```bash
# Step 1: 搜索相关表
python scripts/search_tables.py "同行对比 行业排名 营收"

# Step 2: 查看表结构
# 需要查看 resource/LC_IncomeStatementAll.md

# Step 3: 编写自定义脚本，手动查询多只股票数据并对比
```

**gildata_search 执行方式**:
```bash
# 直接使用快捷脚本
python scripts/stock_peer.py 600519 --rank --avg
# 或查询多只股票
python scripts/stock_finance.py 600519,000858,000568 --type income
```

---

## 预期对比结果

| 测试维度 | gildata_query | gildata_search |
|---------|---------------|----------------|
| **执行步骤** | 3-5步 | 1-2步 |
| **代码编写** | 需要编写完整脚本 | 直接调用现成脚本 |
| **执行时间** | 较长（搜索+编写+调试） | 较短（直接运行） |
| **出错概率** | 较高（自定义SQL可能出错） | 较低（脚本已测试） |
| **灵活性** | 高（可自定义任意查询） | 中（受脚本功能限制） |
| **学习成本** | 高（需了解表结构） | 低（只需知道脚本参数） |

