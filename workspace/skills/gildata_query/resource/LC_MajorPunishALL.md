# LC_MajorPunishALL

**中文名**: 重大事项处罚全表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_MajorPunishALL` |
| MySQL表名 | `lc_majorpunishall` |
| 中文名 | 重大事项处罚全表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1、本表记录机构违规处罚的内容信息,通过【非文本记录ID】字段关联公告表LC_NotTextAnnouncement可获得公告详情。
2、数据范围：2001年-至今
3、信息来源：交易所、上市公司公告、证监会等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 3 | `PublTitle` | 公告标题 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `IssuanceOrg` | 发布机构 | number(10) | ✗ | 100.0% | 发布机构（IssuanceOrg）：与机构基本资料表（LC_InstiArchive）中的“企业编号（CompanyCo... |
| 5 | `AdminNumber` | 行政文号 | varchar2(100) | ✓ | 49.72% |  |
| 6 | `AdminState` | 行政状态 | number(10) | ✗ | 100.0% | 行政状态(AdminState)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得到行政状态... |
| 7 | `IllegalType` | 违规类型 | number(10) | ✓ |  |  |
| 8 | `AdminReconN` | 行政复议文号 | varchar2(100) | ✓ | 0.0% |  |
| 9 | `EventContent` | 事项内容 | clob | ✓ | 1.01% |  |
| 10 | `ManageResolve` | 处理决定 | varchar2(2000) | ✓ | 100.0% |  |
| 11 | `InvolveStock` | 涉及股票 | number(10) | ✓ |  |  |
| 12 | `RID` | 非文本记录ID | number(19) | ✓ | 100.0% | 非文本记录ID（RID）：与“公司公告原文非文本 LC_NotTextAnnouncement”的【ID】字段关联，可获... |
| 13 | `AdminType` | 行政类别 | number(10) | ✓ |  |  |
| 14 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IssuanceOrg (发布机构)

发布机构（IssuanceOrg）：与机构基本资料表（LC_InstiArchive）中的“企业编号（CompanyCode）”关联，得到处罚机构的具体详情。

### AdminState (行政状态)

行政状态(AdminState)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得到行政状态的具体描述：1-正常，2-维持，3-立案调查，4-送达公告，5-举行听证，6-提起诉讼，7-审理终结，8-延期回复，9-已回复，98-不予受理，99-撤消。

### RID (非文本记录ID)

非文本记录ID（RID）：与“公司公告原文非文本 LC_NotTextAnnouncement”的【ID】字段关联，可获得公告详情

## SQL示例

```sql
-- 查询 重大事项处罚全表 数据
SELECT *
FROM lc_majorpunishall
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
