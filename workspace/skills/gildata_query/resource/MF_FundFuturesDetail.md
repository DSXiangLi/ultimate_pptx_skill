# MF_FundFuturesDetail

**中文名**: 公募基金期货投资明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundFuturesDetail` |
| MySQL表名 | `mf_fundfuturesdetail` |
| 中文名 | 公募基金期货投资明细 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季度更新 |
| 字段数量 | 18 |
| 版本 | 1.01 |

## 表描述

1. 本表记录基金季度报告公布的基金投资期货明细，包括期货合约内部编码、持仓量、合约市值、持仓性质等信息。
2. 数据范围：2012-06-30至今
3. 数据来源：基金定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）:与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 8 | `ContractInnerCode` | 期货合约内部编码 | number(10) | ✗ | 100.0% | 期货合约内部编码(ContractInnerCode):与“期货合约（Fut_ContractMain）”中“合约内部编... |
| 9 | `FutExchangeCode` | 期货合约交易代码 | varchar2(10) | ✗ | 100.0% |  |
| 10 | `ContractName` | 期货合约全称 | varchar2(100) | ✗ | 100.0% |  |
| 11 | `ContractType` | 期货合约类型 | number(10) | ✗ | 100.0% | 期货合约类型(ContractType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AN... |
| 12 | `SharesNature` | 持仓性质 | number(10) | ✗ | 100.0% | 持仓性质(SharesNature),该字段固定以下常量:1-多; 2-空 |
| 13 | `SharesHolding` | 持仓量(买/卖) | number(19,4) | ✗ | 100.0% |  |
| 14 | `MarketValue` | 合约市值(元) | number(19,4) | ✓ | 100.0% |  |
| 15 | `FutFairValueChange` | 公允价值变动(元) | number(19,4) | ✓ | 99.99% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）:与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### ContractInnerCode (期货合约内部编码)

期货合约内部编码(ContractInnerCode):与“期货合约（Fut_ContractMain）”中“合约内部编码（ContractInnerCode）”关联，得到期货合约的基本信息。

### ContractType (期货合约类型)

期货合约类型(ContractType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (22,76)，得到期货合约类型的具体描述：22-股指期货，76-国债期货。

### SharesNature (持仓性质)

持仓性质(SharesNature),该字段固定以下常量:1-多; 2-空

## SQL示例

```sql
-- 查询 公募基金期货投资明细 数据
SELECT *
FROM mf_fundfuturesdetail
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
