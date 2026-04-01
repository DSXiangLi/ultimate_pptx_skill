# LC_InvestorDetail

**中文名**: 投资者关系活动调研明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_InvestorDetail` |
| MySQL表名 | `lc_investordetail` |
| 中文名 | 投资者关系活动调研明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 不定时更新 |
| 字段数量 | 12 |
| 版本 | 1.02 |

## 表描述

1、收录参与上市公司调研活动的调研机构明细数据，包括调研单位、调研人员等指标。
2、数据范围：2016-至今
3、信息来源：交易所，上交所互动易和深交所互动易

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 投资者关系活动ID | number(19) | ✗ | 100.0% |  |
| 3 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 4 | `Participant` | 调研机构 | varchar2(140) | ✓ | 100.0% |  |
| 5 | `ParticipantID` | 调研机构编码 | number(10) | ✓ | 95.51% | 调研机构编码（ParticipantID）：与企业码表（EP_CompanyMain）中的企业编号（CompanyCod... |
| 6 | `PersonalName` | 调研人员 | varchar2(50) | ✓ | 62.07% |  |
| 7 | `PersonalID` | 调研人员编码 | number(10) | ✓ | 0.0% | 调研人员编码（PersonalID）：该字段暂不维护。 |
| 8 | `PostName` | 职位名称 | varchar2(50) | ✓ | 1.47% |  |
| 9 | `PostCode` | 职位代码 | number(10) | ✓ |  | 职位代码(PostCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2092，得到职位代码的具... |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ParticipantID (调研机构编码)

调研机构编码（ParticipantID）：与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联，可取得调研机构详细信息。


### PersonalID (调研人员编码)

调研人员编码（PersonalID）：该字段暂不维护。

### PostCode (职位代码)

职位代码(PostCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2092，得到职位代码的具体描述：1-分析师，2-研究员，3-总经理，4-副总经理，5-经理，6-董事长，7-总裁，8-主管，9-总监，10-顾问，11-助理，12-董事，13-证券事务代表，14-组长，15-负责人，16-首席，17-CEO，18-合伙人，19-保荐代表人，20-监事会主席，21-董事会秘书，22-记者，23-基金经理，24-投资经理，25-副总裁，27-副总监，99-其他。

## SQL示例

```sql
-- 查询 投资者关系活动调研明细 数据
SELECT *
FROM lc_investordetail
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
