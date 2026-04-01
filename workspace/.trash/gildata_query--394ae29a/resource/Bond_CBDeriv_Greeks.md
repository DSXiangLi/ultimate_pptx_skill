# Bond_CBDeriv_Greeks

**中文名**: 可转换债券敏感性指标表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDeriv_Greeks` |
| MySQL表名 | `bond_cbderiv_greeks` |
| 中文名 | 可转换债券敏感性指标表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.01 |

## 表描述

内容说明：收录可转换债券定价相关指标和敏感性指标，主要包括隐含波动率、可转债价值和希腊字母(Greeks)等。
数据范围：2008-08-21 至今
信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码(InnerCode)与“债券代码对照表(Bond_Code)”中的“债券内部编码(InnerCode)”关联，... |
| 3 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB =201 AND DM I... |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `SecuInnerCode` | 对应基础股票证券内码 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `StockClosePrice` | 对应基础股票收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `StockYVolatility` | 标的股票波动率(%) | number(19,10) | ✓ | 100.0% | 标的股票波动率(StockYVolatility)：采用历史波动率计算方法，即计算可转债对应标的股票连续复利的年收益率的... |
| 8 | `YearsToMaturity` | 剩余期限 | number(19,4) | ✓ | 100.0% |  |
| 9 | `ConvertPrice` | 转股价格(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `CloseDirtyPrice` | 可转债市场价格(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `ImpliedVolatility` | 隐含波动率(%) | number(19,10) | ✓ | 99.98% |  |
| 12 | `ModelType` | 计算模型类型 | number(10) | ✓ | 100.0% | 	 计算模型类型(ModelType)：1-基于Black-Scholes模型计算可转债敏感性指标；2-价格因素考虑赎回... |
| 13 | `CBPrice` | 可转债定价(元) | number(19,4) | ✓ | 99.52% |  |
| 14 | `CBOptionValue` | 可转债期权价值(元) | number(19,10) | ✓ | 99.52% |  |
| 15 | `Delta` | Delta | number(19,10) | ✓ | 99.54% |  |
| 16 | `Gamma` | Gamma | number(19,10) | ✓ | 99.54% |  |
| 17 | `Vega` | Vega | number(19,10) | ✓ | 99.52% |  |
| 18 | `Theta` | Theta | number(19,10) | ✓ | 99.52% |  |
| 19 | `Rho` | Rho | number(19,10) | ✓ | 99.52% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码(InnerCode)与“债券代码对照表(Bond_Code)”中的“债券内部编码(InnerCode)”关联，得到可转换债券的交易代码、债券简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB =201 AND DM IN(83,90) OR LB =1006 AND DM IN(12,18,21,22)，得到证券市场的具体描述：12-上交所固定收益平台，18-深交所综合收益平台，21-上交所大宗交易，22-上交所综合业务平台定转交易，83-上海证券交易所，90-深圳证券交易所。

### StockYVolatility (标的股票波动率(%))

标的股票波动率(StockYVolatility)：采用历史波动率计算方法，即计算可转债对应标的股票连续复利的年收益率的标准差。

### ModelType (计算模型类型)

	
计算模型类型(ModelType)：1-基于Black-Scholes模型计算可转债敏感性指标；2-价格因素考虑赎回权、回售权、向下修正权的影响，基于蒙特卡洛模拟计算可转债敏感性指标。若可转债公告未披露相关条款，则仅计算ModelType =1 的敏感性指标。

## SQL示例

```sql
-- 查询 可转换债券敏感性指标表 数据
SELECT *
FROM bond_cbderiv_greeks
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
