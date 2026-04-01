# CS_HKSMBasicInfo

**中文名**: 港股股东大会基本信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_HKSMBasicInfo` |
| MySQL表名 | `cs_hksmbasicinfo` |
| 中文名 | 港股股东大会基本信息 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：记录港股股东大会召开时间，召开地点和具体议案等基本信息
2.数据范围：2007年6月至今。
3.信息来源：港交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `MeetingDate` | 股东大会召开日 | date | ✗ | 100.0% |  |
| 5 | `SHMeetingTime` | 股东大会召开时间 | varchar2(100) | ✓ | 97.78% |  |
| 6 | `MeetingType` | 股东大会类别 | number(10) | ✗ | 100.0% | 股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND... |
| 7 | `SHSerialNumber` | 股东大会召开顺序 | number(10) | ✗ | 100.0% |  |
| 8 | `SMRegDate` | 股东大会股权登记日 | date | ✓ | 81.59% |  |
| 9 | `MeetingName` | 会议标题 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `StopTranStartDate` | 暂停过户起始日 | date | ✓ | 76.29% |  |
| 11 | `StopTranEndDate` | 暂停过户截止日 | date | ✓ | 76.29% |  |
| 12 | `Address` | 会议召开地址 | varchar2(100) | ✓ | 99.28% |  |
| 13 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效（IfEffected）的具体描述：1-是（代表此次股东大会数据为最新），2-否（代表此次股东大会已延期、取消或... |
| 14 | `ProposalContent` | 议案内容 | clob | ✓ | 99.92% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### MeetingType (股东大会类别)

股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND DM IN (1,3)，得到股东大会类别的具体描述：1-年度股东大会，3-临时股东大会。

### IfEffected (是否有效)

是否有效（IfEffected）的具体描述：1-是（代表此次股东大会数据为最新），2-否（代表此次股东大会已延期、取消或有相关信息的变更）。

## SQL示例

```sql
-- 查询 港股股东大会基本信息 数据
SELECT *
FROM cs_hksmbasicinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
