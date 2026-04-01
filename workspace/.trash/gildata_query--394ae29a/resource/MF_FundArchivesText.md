# MF_FundArchivesText

**中文名**: 公募基金文本类基本信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundArchivesText` |
| MySQL表名 | `mf_fundarchivestext` |
| 中文名 | 公募基金文本类基本信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 滚动更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金文本类的基本信息，如基金风险揭示，基金特有风险等
2.历史数据：1998年12月起-至今。
3.信息来源：基金公告披露的相关内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `InfoType` | 信息类别 | varchar2(12) | ✓ | 100.0% | 信息类别（InfoType）：FIC0000000W9-组合限制，FCC000000WAF-风险揭示，FIC000000... |
| 8 | `Content` | 信息内容 | clob | ✓ | 99.89% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### InfoType (信息类别)

信息类别（InfoType）：FIC0000000W9-组合限制，FCC000000WAF-风险揭示，FIC0000000W8-特有风险，FCC000000WAG-重要提示，FIC000000077-其他说明，FCC000000Y1U-基金收益分配原则，FCC000001E76-投资比例，FCC000001E77-投资范围，FCC000001EEZ-投资策略。

## SQL示例

```sql
-- 查询 公募基金文本类基本信息 数据
SELECT *
FROM mf_fundarchivestext
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
