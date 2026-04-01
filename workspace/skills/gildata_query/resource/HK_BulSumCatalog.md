# HK_BulSumCatalog

**中文名**: 港股公告摘要目录表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_BulSumCatalog` |
| MySQL表名 | `hk_bulsumcatalog` |
| 中文名 | 港股公告摘要目录表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股公告摘要目录表，记录港股公告摘要的基本信息，方便客户直观获取到重要的公告内容。
2.数据范围：2004年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `AnnouncementType` | 公告类型 | number(10) | ✗ | 100.0% | 公告类型(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 2140，... |
| 5 | `WebsiteF` | 网页地址一 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `WebsiteS` | 网页地址二 | varchar2(200) | ✓ | 7.19% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### AnnouncementType (公告类型)

公告类型(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 2140，得到公告类型的具体描述：10-股份权益过分集中，20-发行人延迟发表业绩公告，30-上市公司核数师变动，40-上市公司秘书变动，50-附带保留意见或说明段落的核数师报告，60-盈利警告，70-修正重大错误而做出的前期调整，80-修改已刊发财务报表及报告。

## SQL示例

```sql
-- 查询 港股公告摘要目录表 数据
SELECT *
FROM hk_bulsumcatalog
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
