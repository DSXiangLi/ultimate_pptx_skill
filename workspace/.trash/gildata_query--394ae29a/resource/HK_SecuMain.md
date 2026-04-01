# HK_SecuMain

**中文名**: 港股证券主表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SecuMain` |
| MySQL表名 | `hk_secumain` |
| 中文名 | 港股证券主表 |
| 路径 | 聚源新版数据库 > 常量库 |
| 更新频率 | 日处理，不定时更新 |
| 字段数量 | 23 |
| 版本 | 1.02 |

## 表描述

本表收录港股单个证券品种的简称、上市交易所等基础信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `SecuCode` | 证券代码 | varchar2(10) | ✓ | 100.0% |  |
| 5 | `ChiName` | 中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `ChiNameAbbr` | 中文名称缩写 | varchar2(100) | ✓ | 0.7% |  |
| 7 | `EngName` | 英文名称 | varchar2(200) | ✓ | 99.78% |  |
| 8 | `EngNameAbbr` | 英文名称缩写 | varchar2(50) | ✓ | 99.58% |  |
| 9 | `SecuAbbr` | 证券简称 | varchar2(20) | ✓ | 100.0% |  |
| 10 | `ChiSpelling` | 拼音证券简称 | varchar2(50) | ✓ | 100.0% |  |
| 11 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 12 | `SecuCategory` | 证券类别 | number(10) | ✓ | 100.0% | 证券类别(SecuCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 and ... |
| 13 | `ListedDate` | 上市日期 | date | ✓ | 99.71% |  |
| 14 | `ListedSector` | 上市板块 | number(10) | ✓ | 100.0% | 上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207 AND D... |
| 15 | `ListedState` | 上市状态 | number(10) | ✓ | 100.0% | 上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND D... |
| 16 | `FormerName` | 曾用名 | varchar2(200) | ✓ | 0.31% |  |
| 17 | `DelistingDate` | 退市日期 | date | ✓ | 96.21% |  |
| 18 | `TradingUnit` | 买卖单位(股/手) | number(18,4) | ✓ | 99.59% |  |
| 19 | `TraCurrUnit` | 交易货币类别 | number(10) | ✓ | 99.96% | 交易货币类别（TraCurrUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB... |
| 20 | `ISIN` | ISIN代码 | varchar2(20) | ✓ | 68.47% |  |
| 21 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 22 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (72)，得到证券市场的具体描述：72-香港联交所。

### SecuCategory (证券类别)

证券类别(SecuCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 and DM in (3,4,10,20,21,25,51,52,53,55,60,61,62,63,64,65,68,69,71,72,78,81,82)，得到证券类别的具体描述：3-H股，4-大盘，10-其他，20-衍生权证，21-股本权证，25-牛熊证，51-港股，52-合订证券，53-红筹股，55-优先股，60-基金，61-信托基金，62-ETF基金，63-参与证书，64-杠杆及反向产品，65-债务证券，68-界内证，69-美国证券(交易试验计划)，71-普通预托证券，72-优先预托证券，78-临时证券(Temporary)，81-SPAC股份，82-SPAC权证。

### ListedSector (上市板块)

上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207 AND DM IN (1,4,6)，得到上市板块的具体描述：1-主板，4-其他，6-创业板。

### ListedState (上市状态)

上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,5,9)，得到上市状态的具体描述：1-上市，5-终止，9-其他。

### TraCurrUnit (交易货币类别)

交易货币类别（TraCurrUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“交易货币”描述：1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。

## SQL示例

```sql
-- 查询 港股证券主表 数据
SELECT *
FROM hk_secumain
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
