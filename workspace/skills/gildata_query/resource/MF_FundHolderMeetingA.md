# MF_FundHolderMeetingA

**中文名**: 公募基金持有人大会附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundHolderMeetingA` |
| MySQL表名 | `mf_fundholdermeetinga` |
| 中文名 | 公募基金持有人大会附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录公募基金持有人大会议案中的议题情况，包括议题类型以及通过与否等。
2.数据范围：1998年3月起-至今。
3.信息来源：基金公司披露的临时报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  | 注：可根据NoticeDate和InnerCode关联附表【MF_FundHolderMeeting】，获取大会相关信息 |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `NoticeDate` | 首次会议通知公告日 | date | ✗ | 100.0% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `MeetingTopic` | 大会议题 | varchar2(200) | ✗ | 100.0% |  |
| 7 | `IfPassed` | 是否通过 | number(10) | ✓ | 80.38% | 是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN... |
| 8 | `SharesApproved` | 同意份额数 | number(19,2) | ✓ | 84.38% |  |
| 9 | `RatioApproved` | 同意份额占比(%) | number(10,6) | ✓ | 84.56% |  |
| 10 | `SharesOpposed` | 反对份额数 | number(19,2) | ✓ | 84.38% |  |
| 11 | `RatioOpposed` | 反对份额占比(%) | number(10,6) | ✓ | 84.56% |  |
| 12 | `SharesDisclaimed` | 弃权份额数 | number(19,2) | ✓ | 84.38% |  |
| 13 | `RatioDisclaimed` | 弃权份额占比(%) | number(10,6) | ✓ | 84.56% |  |
| 14 | `ReasonDesc` | 未通过原因描述 | varchar2(2000) | ✓ | 17.9% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |
| 18 | `EventType` | 事项类型 | number(10) | ✓ | 0.0% |  |

## 字段说明

### ID (ID)

注：可根据NoticeDate和InnerCode关联附表【MF_FundHolderMeeting】，获取大会相关信息

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfPassed (是否通过)

是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否通过的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金持有人大会附表 数据
SELECT *
FROM mf_fundholdermeetinga
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
