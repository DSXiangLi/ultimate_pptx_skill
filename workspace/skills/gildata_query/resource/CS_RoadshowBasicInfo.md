# CS_RoadshowBasicInfo

**中文名**: 路演基本信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_RoadshowBasicInfo` |
| MySQL表名 | `cs_roadshowbasicinfo` |
| 中文名 | 路演基本信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上市公司路演、投资者交流活动的通知信息
2.数据范围：2020年至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码(InnerCode)：：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码(CompanyCode)：：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `RoadshowType` | 路演类型 | number(10) | ✗ | 100.0% | 路演类型(RoadshowType)与(CT_SystemConst)表中的DM字段关联，令LB = 2632，得到路演... |
| 6 | `RoadshowMethod` | 路演方式 | number(10) | ✗ | 100.0% | 路演方式(RoadshowMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2631，得到... |
| 7 | `RoadshowDate` | 路演日期 | date | ✗ | 100.0% |  |
| 8 | `RoadshowBeginTime` | 路演开始时间 | varchar2(100) | ✓ | 99.85% |  |
| 9 | `RoadshowEndTime` | 路演截止时间 | varchar2(100) | ✓ | 99.01% |  |
| 10 | `RoadshowAddress` | 路演地址 | varchar2(300) | ✓ | 99.99% |  |
| 11 | `RoadshowCity` | 线下路演城市 | number(10) | ✓ | 4.47% | 可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；也可关联国家城市代码表的“地区行政编码（... |
| 12 | `RoadshowWebsite` | 路演网址 | varchar2(300) | ✓ | 92.34% |  |
| 13 | `Participant` | 参与人员 | nvarchar2(500) | ✓ | 17.7% |  |
| 14 | `RoadshowBriefInfo` | 路演简介 | clob | ✓ | 17.81% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码(InnerCode)：：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码(CompanyCode)：：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### RoadshowType (路演类型)

路演类型(RoadshowType)与(CT_SystemConst)表中的DM字段关联，令LB = 2632，得到路演类型的具体描述：1-首发，2-增发，3-配股，4-可转债发行，5-业绩公布，6-重大事项，7-投资者接待日，99-其他。

### RoadshowMethod (路演方式)

路演方式(RoadshowMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2631，得到路演方式的具体描述：1-网上路演，2-现场路演，3-电话会议，4-视频会议，99-其他。

### RoadshowCity (线下路演城市)

可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；也可关联国家城市代码表的“地区行政编码（AreaCode）”关联，得到地区代码的具体描述。

## SQL示例

```sql
-- 查询 路演基本信息 数据
SELECT *
FROM cs_roadshowbasicinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
