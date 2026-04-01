# HK_LeaderIntroduce

**中文名**: 港股领导人背景介绍

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_LeaderIntroduce` |
| MySQL表名 | `hk_leaderintroduce` |
| 中文名 | 港股领导人背景介绍 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股人力资源 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

1.介绍港股领导人的个人资料、职称和背景，包含的主要字段有：信息发布日期、姓名、年龄、最高学历、背景介绍等。
2.数据范围：2003年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `LeaderID` | 领导人ID | number(10) | ✓ | 100.0% |  |
| 5 | `LeaderName` | 姓名 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `LeaderGender` | 性别 | number(10) | ✓ | 99.67% | 性别(LeaderGender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具... |
| 7 | `BirthYM` | 出生年月 | date | ✓ | 92.78% |  |
| 8 | `BirthYMInfo` | 出生年月(文本) | varchar2(20) | ✓ | 0.26% |  |
| 9 | `Age` | 年龄(岁) | number(10) | ✓ | 92.78% |  |
| 10 | `LeaderDegree` | 最高学历 | number(10) | ✓ | 84.77% | 最高学历(LeaderDegree)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到最高... |
| 11 | `LeaderTitle` | 职称 | number(10) | ✓ |  |  |
| 12 | `EarliestInDate` | 最早任职年月 | date | ✓ | 3.5% |  |
| 13 | `Background` | 背景介绍 | clob | ✓ | 0.25% |  |
| 14 | `SerialNumber` | 排序标识 | number(10) | ✓ | 100.0% |  |
| 15 | `Statement` | 备注 | varchar2(500) | ✓ | 0.88% |  |
| 16 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### LeaderGender (性别)

性别(LeaderGender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-男，2-女。

### LeaderDegree (最高学历)

最高学历(LeaderDegree)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到最高学历的具体描述：1-博士后，2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他，9-初中及以下。

## SQL示例

```sql
-- 查询 港股领导人背景介绍 数据
SELECT *
FROM hk_leaderintroduce
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
