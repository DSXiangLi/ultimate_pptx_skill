# MF_GradedFundFT

**中文名**: 公募基金_分级基金附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_GradedFundFT` |
| MySQL表名 | `mf_gradedfundft` |
| 中文名 | 公募基金_分级基金附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 分级基金 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.本表记录分级基金的份额配比数据。
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。
4.数据未更新原因：公募分级基金业务已终止。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 4 | `DataType` | 数据类别 | number(10) | ✗ | 100.0% | 数据类别(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1770 AND DM =... |
| 5 | `DataValue` | 数值 | float | ✗ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### DataType (数据类别)

数据类别(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1770 AND DM = 20，得到数据类别的具体描述：20-份额配对转换比例。

## SQL示例

```sql
-- 查询 公募基金_分级基金附表 数据
SELECT *
FROM mf_gradedfundft
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
