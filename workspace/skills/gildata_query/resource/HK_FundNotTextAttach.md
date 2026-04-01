# HK_FundNotTextAttach

**中文名**: 香港基金公告原文非文本附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundNotTextAttach` |
| MySQL表名 | `hk_fundnottextattach` |
| 中文名 | 香港基金公告原文非文本附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 6 |
| 版本 | 1 |

## 表描述

1.内容说明：本表为HK_FundNotTextAnnounce的附表，用于获取同一公告对应的涉及基金代码。
2.信息来源：证监会、港交所、基金公司
3.数据范围：1999年至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与HK_FundNotTextAnnounce的ID关联，获取公告的相关信息，包含公告格式、媒体出处、信息标题等... |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码(InnerCode): 与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode... |
| 4 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 5 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 6 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与HK_FundNotTextAnnounce的ID关联，获取公告的相关信息，包含公告格式、媒体出处、信息标题等。

### InnerCode (基金内部编码)

基金内部编码(InnerCode): 与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的证券代码、基金简称等。

## SQL示例

```sql
-- 查询 香港基金公告原文非文本附表 数据
SELECT *
FROM hk_fundnottextattach
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
