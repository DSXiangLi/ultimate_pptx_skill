# HK_LeaderSalary

**中文名**: 港股领导人薪酬表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_LeaderSalary` |
| MySQL表名 | `hk_leadersalary` |
| 中文名 | 港股领导人薪酬表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股人力资源 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1.02 |

## 表描述

1.内容说明：记录港股上市公司主要领导人领取薪酬及持有权益的情况。
2.数据范围：2007年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `InfoSourceCode` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 ... |
| 7 | `LeaderID` | 领导人ID | number(10) | ✓ | 100.0% |  |
| 8 | `LeaderName` | 领导人姓名 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `PositionType` | 职位类别 | number(10) | ✓ | 80.97% | 职位类别(PositionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1420，得到职位... |
| 10 | `PostName` | 职位名称 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `Position` | 职位 | number(10) | ✓ |  |  |
| 12 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 99.36% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 and ... |
| 13 | `SalaryAmount` | 薪酬金额(元) | number(19,2) | ✓ | 99.34% |  |
| 14 | `EquityVolume` | 权益总数(股) | number(18,2) | ✓ | 31.51% |  |
| 15 | `PersonalEquity` | 个人权益(股) | number(18,2) | ✓ | 16.35% |  |
| 16 | `Remark` | 备注 | varchar2(500) | ✓ | 12.82% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSourceCode (信息来源代码)

信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM IN (5,10,12)，得到信息来源代码的具体描述：5-年度报告，10-申请版本，12-招股章程。

### PositionType (职位类别)

职位类别(PositionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1420，得到职位类别的具体描述：10-董事会，20-监事会，30-经营层，40-集团，50-董事会专门委员会，60-监事会专门委员会，70-核心技术人员，90-其他。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 and DM in (1000,1100,1160,1210,1220,1320,1360,1420,1430,3000,3030,5010,6010)，得到货币单位的具体描述：1000-美元，1100-港元，1160-日本元，1210-澳门元，1220-马来西亚林吉特，1320-新加坡元，1360-泰国铢，1420-人民币元，1430-台湾元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。

## SQL示例

```sql
-- 查询 港股领导人薪酬表 数据
SELECT *
FROM hk_leadersalary
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
