# CS_DelistingBasicInfo

**中文名**: 终止上市基本资料表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_DelistingBasicInfo` |
| MySQL表名 | `cs_delistingbasicinfo` |
| 中文名 | 终止上市基本资料表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 滚动更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

记录A股，B股终止上市代码的基本资料

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `DelistingDecisionEffectiveDate` | 终止上市决定日 | date | ✓ | 100.0% |  |
| 4 | `DelistingLastTradingDate` | 终止上市最后交易日 | date | ✓ | 98.87% |  |
| 5 | `DelistingDate` | 退市日期 | date | ✓ | 98.87% |  |
| 6 | `DelistingLastClosePrice` | 终止上市前最后收盘价 | number(19,4) | ✓ | 98.87% |  |
| 7 | `DelistingLastNetAssetPS` | 终止上市前每股净资产 | number(19,4) | ✓ | 98.59% |  |
| 8 | `DelistingCausation` | 终止上市原因 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `DelistingMajorContent` | 终止上市决定主要内容 | varchar2(2000) | ✓ | 100.0% |  |
| 10 | `DelistingType` | 终止上市类型 | number(10) | ✓ | 100.0% | 终止上市类型(DelistingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2598 A... |
| 11 | `TransferBoard` | 转入板块 | varchar2(50) | ✓ | 97.18% |  |
| 12 | `TransferInnerCode` | 转入内部编码 | varchar2(50) | ✓ | 97.18% | 转入内部编码(TransferInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCo... |
| 13 | `TransferBoardListedDate` | 转入板块上市日期 | varchar2(50) | ✓ | 92.96% |  |
| 14 | `IfEntryDelistingPeriod` | 是否进入退市整理期 | number(10) | ✓ | 98.87% | 是否进入退市整理期(IfEntryDelistingPeriod)与(CT_SystemConst)表中的DM字段关联，... |
| 15 | `DelistingPeriodStartDate` | 退市整理期起始日 | date | ✓ | 41.41% |  |
| 16 | `EstiDelistingPeriodEndDate` | 预计退市整理期截止日 | date | ✓ | 41.41% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### DelistingType (终止上市类型)

终止上市类型(DelistingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2598 AND DM IN (4,5,6,7,8,9)，得到终止上市类型的具体描述：4-交易类退市，5-主动退市，6-规范类退市，7-重大违法退市，8-财务类退市，9-其他退市事件。

### TransferInnerCode (转入内部编码)

转入内部编码(TransferInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### IfEntryDelistingPeriod (是否进入退市整理期)

是否进入退市整理期(IfEntryDelistingPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否进入退市整理期的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 终止上市基本资料表 数据
SELECT *
FROM cs_delistingbasicinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
