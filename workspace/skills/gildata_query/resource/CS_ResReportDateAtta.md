# CS_ResReportDateAtta

**中文名**: 境内财务报告预约披露日附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_ResReportDateAtta` |
| MySQL表名 | `cs_resreportdateatta` |
| 中文名 | 境内财务报告预约披露日附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表 |
| 更新频率 | 不定期更新 |
| 字段数量 | 6 |
| 版本 | 1 |

## 表描述

1、内容说明：收录沪深京上市公司定期报告的更正公告披露日期，本表为CS_ReserveReportDate的附表。
2、数据范围：1990-12-28至今
3、信息来源：上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 与境内财务报告预约披露日（CS_ReserveReportDate） 表的ID关联，得到对应更正公告披露日期的详细信息。 |
| 3 | `CorrectIssuingDate` | 更正公告披露日期 | date | ✗ | 100.0% |  |
| 4 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

与境内财务报告预约披露日（CS_ReserveReportDate）
表的ID关联，得到对应更正公告披露日期的详细信息。

## SQL示例

```sql
-- 查询 境内财务报告预约披露日附表 数据
SELECT *
FROM cs_resreportdateatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
