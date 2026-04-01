# LC_STIBDividendObject

**中文名**: 科创板分红附表-分红对象

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBDividendObject` |
| MySQL表名 | `lc_stibdividendobject` |
| 中文名 | 科创板分红附表-分红对象 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

内容说明：此表为“科创板分红（LC_STIBDividend）”的衍生附表，记录分红事项中涉及到的具体多个分红对象的名单，比如自行发放对象、特定分红对象等。
数据范围：2018年至今
信息来源：分红实施公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 分红表ID | number(19) | ✗ | 100.0% | 分红表ID（RID）：与“科创板分红(LC_STIBDividend)”的“ID”关联使用。 |
| 3 | `ObjectTypeCode` | 对象类型 | number(10) | ✗ | 100.0% | 对象类型(ObjectTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2287，得到... |
| 4 | `SHList` | 股东名单 | varchar2(200) | ✗ | 100.0% |  |
| 5 | `SHAttribute` | 股东属性 | number(10) | ✓ | 88.68% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属... |
| 6 | `SHID` | 股东ID | number(10) | ✓ | 53.36% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (分红表ID)

分红表ID（RID）：与“科创板分红(LC_STIBDividend)”的“ID”关联使用。

### ObjectTypeCode (对象类型)

对象类型(ObjectTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2287，得到对象类型的具体描述：1-自行发放对象，2-特定分红对象。

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 科创板分红附表-分红对象 数据
SELECT *
FROM lc_stibdividendobject
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
