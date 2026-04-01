# Fut_TradingQuote

**中文名**: 金融期货每日行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_TradingQuote` |
| MySQL表名 | `fut_tradingquote` |
| 中文名 | 金融期货每日行情 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货行情 |
| 更新频率 | 日更新 |
| 字段数量 | 34 |
| 版本 | 1.02 |

## 表描述

1.内容说明：本表收录股指期货、国债期货的日行情数据。包括高开低收、涨跌幅、持仓量、成交量、成交额、持仓量变化和基差等指标。
2.数据范围：2010年至今
3.信息来源：中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `ContractCode` | 合约代码 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `ExchangeCode` | 交易所代码 | number(10) | ✓ | 100.0% | 交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND... |
| 6 | `OptionCode` | 合约标的 | number(10) | ✓ | 100.0% | 当合约标的(OptionCode) in（46,3145,4978,39144）时，与证券主表（ SecuMain）的证... |
| 7 | `SeriesFlag` | 合约序列标志 | number(10) | ✓ | 61.72% | 合约序列标志（SeriesFlag），该字段固定以下常量：对于股指期货：1-当月合约；2-下月合约；3-隔季合约；4-下... |
| 8 | `PrevSettlePrice` | 前结算 | number(19,4) | ✓ | 100.0% |  |
| 9 | `PrevClosePrice` | 前收盘 | number(19,4) | ✓ | 99.36% |  |
| 10 | `OpenPrice` | 开盘价 | number(19,4) | ✓ | 98.85% |  |
| 11 | `HighPrice` | 最高价 | number(19,4) | ✓ | 98.85% |  |
| 12 | `LowPrice` | 最低价 | number(19,4) | ✓ | 98.85% |  |
| 13 | `ClosePrice` | 收盘价 | number(19,4) | ✓ | 100.0% |  |
| 14 | `ChangeOfCTPS` | 收盘较前结算涨跌 | number(19,4) | ✓ | 100.0% |  |
| 15 | `ChangePCTCTPS` | 收盘较前结算涨跌幅(%) | number(18,10) | ✓ | 99.36% |  |
| 16 | `ChangeOfClosePrice` | 收盘价涨跌 | number(19,4) | ✓ | 99.36% |  |
| 17 | `ChangePCTClosePrice` | 收盘价涨跌幅(%) | number(18,10) | ✓ | 99.36% |  |
| 18 | `SettlePrice` | 结算价 | number(19,4) | ✓ | 100.0% |  |
| 19 | `ChangeOfSettPrice` | 结算价涨跌 | number(19,4) | ✓ | 100.0% |  |
| 20 | `ChangePCTSettPrice` | 结算价涨跌幅(%) | number(18,10) | ✓ | 99.36% |  |
| 21 | `OpenInterest` | 持仓量(手) | number(18,4) | ✓ | 100.0% |  |
| 22 | `ChangeOfOpenInterest` | 持仓量变化(手) | number(18,4) | ✓ | 99.67% |  |
| 23 | `ChangePCTOpenInterest` | 持仓量变化幅度(%) | number(18,10) | ✓ | 98.55% |  |
| 24 | `TurnoverVolume` | 成交量(手) | number(18,4) | ✓ | 100.0% |  |
| 25 | `ChangeOfTurnoverVolume` | 成交量变化(手) | number(18,4) | ✓ | 99.36% |  |
| 26 | `ChangePCTTurnoverVolume` | 成交量变化幅度(%) | number(18,10) | ✓ | 98.27% |  |
| 27 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `ChangeOfTurnoverValue` | 成交金额变化(元) | number(19,4) | ✓ | 99.36% |  |
| 29 | `ChangePCTTurnoverValue` | 成交金额变化幅度(%) | number(18,10) | ✓ | 98.27% |  |
| 30 | `MainContractMark` | 主力标志 | number(10) | ✓ | 17.38% | 主力标志，该字段固定以下常量：1-是。同一交易日期，同一交易所，同一品种，优先选取持仓量最大的合约为主力标志；如果持仓量... |
| 31 | `BasisValue` | 基差 | number(18,4) | ✓ | 76.57% | 基差（BasisValue）：当“合约类型”为股指期货，基差=期货市场收盘价-现货市场收盘价 |
| 32 | `BasisAnnualYield` | 年化贴水率(%) | number(18,10) | ✓ | 75.63% | 年化贴水率（BasisAnnualYield）：基差/现货收盘价进行年化后的收益率 |
| 33 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 34 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### ExchangeCode (交易所代码)

交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = 20，得到交易所代码的具体描述：20-中国金融期货交易所。

### OptionCode (合约标的)

当合约标的(OptionCode) in（46,3145,4978,39144）时，与证券主表（ SecuMain）的证券内部编码（InnerCode）字段关联，得到合约标的的具体描述：46-上证50指数，3145-沪深300指数，4978-中证500指数, 39144-中证1000指数；当合约标的(OptionCode) in（501,502,503,504）时与产品表(CT_Product)中的产品代码（ProductCode）字段关联，令产品分类（ProductCategory）= 326，得到合约标的的具体描述：501-票面利率3%的5年期名义中期国债，502-票面利率3%的名义长期国债，503-票面利率3%的2年期名义中短期国债，504-票面利率3%的名义超长期国债。

### SeriesFlag (合约序列标志)

合约序列标志（SeriesFlag），该字段固定以下常量：对于股指期货：1-当月合约；2-下月合约；3-隔季合约；4-下季合约；对于国债期货：1-当季合约；2-下季合约；3-隔季合约。

### MainContractMark (主力标志)

主力标志，该字段固定以下常量：1-是。同一交易日期，同一交易所，同一品种，优先选取持仓量最大的合约为主力标志；如果持仓量存在相等的情况，则选择成交量最大的合约为主力标志；如果成交量也存在相等的情况，再选择交割时间离当下最近的合约为主力标志。

### BasisValue (基差)

基差（BasisValue）：当“合约类型”为股指期货，基差=期货市场收盘价-现货市场收盘价

### BasisAnnualYield (年化贴水率(%))

年化贴水率（BasisAnnualYield）：基差/现货收盘价进行年化后的收益率

## SQL示例

```sql
-- 查询 金融期货每日行情 数据
SELECT *
FROM fut_tradingquote
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
