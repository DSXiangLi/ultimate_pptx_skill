# Fut_MemberRankByContract

**中文名**: 期货会员交易排名_按交易合约

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_MemberRankByContract` |
| MySQL表名 | `fut_memberrankbycontract` |
| 中文名 | 期货会员交易排名_按交易合约 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国内期货交易所会员以交易合约为维度，日度的按照成交量统计、持买单量统计和持卖单量统计三种统计方式统计的会员成交持仓排名数据。
2.数据范围：2002年至今
3.信息来源：上海期货交易所、大连商品交易所、郑州商品交易所和中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `ExchangeCode` | 交易所 | number(10) | ✗ | 100.0% | 交易所(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND D... |
| 4 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：当为期货合约时，与期货合约（Fut_ContractMain）表中的... |
| 5 | `ContractCode` | 合约代码 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `ReportPeriod` | 数据统计期间 | number(10) | ✗ | 100.0% | 数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AN... |
| 7 | `RankNumber` | 名次 | number(10) | ✓ | 99.63% |  |
| 8 | `MemberInnerCode` | 会员内部编码 | number(10) | ✓ | 100.0% | 会员内部编码(MemberInnerCode)：与(LC_InstiArchive)表中的CompanyCode字段关联... |
| 9 | `MemberCode` | 会员号 | varchar2(20) | ✓ | 100.0% |  |
| 10 | `MemberAbbr` | 会员简称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `IndicatorCode` | 指标代码 | number(10) | ✗ | 100.0% | 指标代码（IndicatorCode）：与系统常量表（CT_SystemConst）中的代码（DM）字段进行关联，令LB... |
| 12 | `IndicatorName` | 指标名称 | varchar2(50) | ✓ | 100.0% |  |
| 13 | `IndicatorVolume` | 指标数量(手) | number(18,4) | ✓ | 100.0% |  |
| 14 | `ChangeVolume` | 较上期增减量(手) | number(18,4) | ✓ | 100.0% |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ExchangeCode (交易所)

交易所(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,11,13,15,17,20)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所，20-中国金融期货交易所。

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：当为期货合约时，与期货合约（Fut_ContractMain）表中的合约内部编码（ContractInnerCode）字段进行关联，得到该期货合约的基础信息；当为期货品种时，与
期货品种 (Fut_FuturesContract)表中的合约内部编码（ContractInnerCode）字段进行关联，得到该期货品种的基础信息。

### ReportPeriod (数据统计期间)

数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM = 5，得到数据统计期间的具体描述：5-日。

### MemberInnerCode (会员内部编码)

会员内部编码(MemberInnerCode)：与(LC_InstiArchive)表中的CompanyCode字段关联，令IfExisted = 1，得到会员内部编码的具体描述。

### IndicatorCode (指标代码)

指标代码（IndicatorCode）：与系统常量表（CT_SystemConst）中的代码（DM）字段进行关联，令LB=1580，得到统计指标的具体描述。1-成交量统计、3-持买仓量统计、4-持卖仓量统计。

## SQL示例

```sql
-- 查询 期货会员交易排名_按交易合约 数据
SELECT *
FROM fut_memberrankbycontract
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
