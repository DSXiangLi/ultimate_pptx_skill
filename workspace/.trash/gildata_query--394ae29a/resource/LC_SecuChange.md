# LC_SecuChange

**中文名**: 证券简称更名

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SecuChange` |
| MySQL表名 | `lc_secuchange` |
| 中文名 | 证券简称更名 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

收录了证券简称的历次变更情况，包括：股东大会决议公告日期、是否否决、简称更改日期、证券简称、简称变更原因等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 2.34% |  |
| 5 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 0.25% |  |
| 6 | `IfPassed` | 是否否决 | number(10) | ✓ | 100.0% | 是否否决(IfPassed)，该字段固定以下常量：1-是；0-否 |
| 7 | `ChangeDate` | 简称更改日期 | date | ✓ | 3.6% |  |
| 8 | `SecurityAbbr` | 证券简称 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `ChiSpelling` | 拼音证券简称 | varchar2(50) | ✓ | 99.98% |  |
| 10 | `ExtendedAbbr` | 扩位简称 | varchar2(100) | ✓ | 0.02% |  |
| 11 | `ExtendedSpelling` | 拼音扩位简称 | varchar2(50) | ✓ | 0.02% |  |
| 12 | `ChangeReason` | 简称变更原因 | number(10) | ✓ | 0.63% | 简称变更原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1185，得到... |
| 13 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfPassed (是否否决)

是否否决(IfPassed)，该字段固定以下常量：1-是；0-否

### ChangeReason (简称变更原因)

简称变更原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1185，得到简称变更原因的具体描述：1-ST，2-撤销ST，3-PT，4-撤销PT，5-*ST，6-撤销*ST，7-撤消*ST并实行ST，8-从ST变为*ST，9-退市整理期，10-高风险警示，11-撤销高风险警示，12-叠加ST，13-撤销叠加ST，14-叠加*ST，15-撤销叠加*ST。

## SQL示例

```sql
-- 查询 证券简称更名 数据
SELECT *
FROM lc_secuchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
