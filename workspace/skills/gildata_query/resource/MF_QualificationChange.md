# MF_QualificationChange

**中文名**: 基金资格成份变动表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_QualificationChange` |
| MySQL表名 | `mf_qualificationchange` |
| 中文名 | 基金资格成份变动表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.收录基金资格成份变动，包含如合格公募基金纳入个人养老金基金池的名单、南下互认基金名单等。
2.历史数据：2022年11月起-至今
3.数据来源：证监会等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `FundQuaCat` | 基金资格类别 | number(10) | ✗ | 100.0% | 基金资格类别(FundQuaCat)与(CT_SystemConst)表中的DM字段关联，令LB=2530，得到基金资格... |
| 3 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 86.4% |  |
| 6 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 7 | `OutDate` | 剔除日期 | date | ✓ | 0.6% |  |
| 8 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN... |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FundQuaCat (基金资格类别)

基金资格类别(FundQuaCat)与(CT_SystemConst)表中的DM字段关联，令LB=2530，得到基金资格类别的具体描述：1-个人养老金标的池，2-南下内地香港互认基金。

### InnerCode (基金内码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 基金资格成份变动表 数据
SELECT *
FROM mf_qualificationchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
