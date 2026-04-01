# HK_LoanClassification

**中文名**: 港股贷款分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_LoanClassification` |
| MySQL表名 | `hk_loanclassification` |
| 中文名 | 港股贷款分类表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 不定期更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股贷款分类表，记录港股上市银行贷款按行业、按地区、按产品、按担保方式等分类方式的分部情况。
2.数据范围：2011年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 7 | `LoanCla` | 贷款分类 | varchar2(50) | ✓ | 100.0% |  |
| 8 | `LoanClaCode` | 贷款分类代码 | number(10) | ✗ | 100.0% | 贷款分类代码(LoanClaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2131 AND... |
| 9 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 10 | `ItemName` | 科目名称 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `ItemCode` | 科目代码 | number(10) | ✗ | 100.0% | 科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2131 AND DM N... |
| 12 | `ProjectName` | 项目名称 | varchar2(100) | ✗ | 100.0% |  |
| 13 | `ProjectCode` | 项目代码 | number(10) | ✓ | 35.77% | 项目代码(ProjectCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2132，得到项目代... |
| 14 | `LoanAmount` | 贷款金额 | number(19,4) | ✓ | 98.1% |  |
| 15 | `PercOfTotalLoans` | 占贷款总额比例(%) | number(19,4) | ✓ | 65.1% |  |
| 16 | `NonPerformingLoans` | 不良贷款金额 | number(19,4) | ✓ | 56.75% |  |
| 17 | `BadLoanRatio` | 不良贷款率(%) | number(19,4) | ✓ | 52.88% |  |
| 18 | `PreLoanAmount` | 上期贷款金额 | number(19,4) | ✓ | 86.01% |  |
| 19 | `PrPercOfTotalLoans` | 上期占贷款总额比例(%) | number(19,4) | ✓ | 59.37% |  |
| 20 | `PreNonPerformingLoans` | 上期不良贷款金额 | number(19,4) | ✓ | 47.41% |  |
| 21 | `PreBadLoanRatio` | 上期不良贷款率(%) | number(19,4) | ✓ | 43.42% |  |
| 22 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.0% |  |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM in (2,3,4,5,10,11,12)，得到信息来源的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，10-申请版本，11-聆讯后资料集，12-招股章程。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM in (1000,1100,1420)，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### LoanClaCode (贷款分类代码)

贷款分类代码(LoanClaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2131 AND DM in (10,20,30,40)，得到贷款分类代码的具体描述：10-按行业，20-按产品，30-按地区，40-按担保方式。

### ItemCode (科目代码)

科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2131 AND DM NOT IN (10,20,30,40)，得到科目代码的具体描述：50-公司类贷款和垫款，60-个人贷款和垫款，70-票据贴现，80-海外和子公司，90-总行，100-境内，110-境外及其他，120-抵押贷款，130-质押贷款，140-保证贷款，150-信用贷款，160-附担保物贷款，170-其他，180-合计。

### ProjectCode (项目代码)

项目代码(ProjectCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2132，得到项目代码的具体描述：100000-公司类贷款和垫款，110000-个人贷款和垫款，120000-票据贴现，130000-海外和子公司，140000-总行，150000-境内，160000-境外及其他，170000-抵押贷款，180000-质押贷款，190000-保证贷款，200000-信用贷款，210000-附担保物贷款，220000-其他，999998-非运算项目，999999-总额。

## SQL示例

```sql
-- 查询 港股贷款分类表 数据
SELECT *
FROM hk_loanclassification
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
