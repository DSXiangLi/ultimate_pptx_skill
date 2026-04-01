# CS_AICRelationship

**中文名**: 公司股东一致行动人关系

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_AICRelationship` |
| MySQL表名 | `cs_aicrelationship` |
| 中文名 | 公司股东一致行动人关系 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明: 收录根据上市公司在招投说明书、定期报告及临时公告中披露的一致行动人信息。
2.数据范围：2019年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。
4.业务唯一性：CompanyCode,Constitute,ActInConcertMember

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 5 | `Constitute` | 组别 | number(10) | ✗ | 100.0% |  |
| 6 | `ActInConcertMember` | 一致行动人成员 | nvarchar2(200) | ✗ | 100.0% |  |
| 7 | `ActInConcertNature` | 一致行动人性质 | number(10) | ✓ | 100.0% |  |
| 8 | `ActInConcertID` | 一致行动人ID | number(10) | ✓ | 50.33% |  |
| 9 | `ActInConcertStatement` | 一致行动人说明 | nvarchar2(2000) | ✓ | 100.0% |  |
| 10 | `ActInConcert` | 一致行动人 | nvarchar2(1000) | ✓ | 100.0% |  |
| 11 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 12 | `ExpiryDate` | 失效日期 | date | ✓ | 36.56% |  |
| 13 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (1,2,3,4,5,6,8,9,10,17,23,25,99)，得到信息来源的具体描述：1-招股说明书，2-招股意向书，3-配股说明书，4-上市公告书，5-年度报告，6-中期报告，8-增发新股招股说明书，9-增发新股招股意向书，10-增发新股上市公告书，17-第一季度报告，23-第三季度报告，25-招股说明书(申报稿)，99-临时公告。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公司股东一致行动人关系 数据
SELECT *
FROM cs_aicrelationship
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
