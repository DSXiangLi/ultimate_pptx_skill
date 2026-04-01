# HK_FiveTierClaloans

**中文名**: 港股贷款五级分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FiveTierClaloans` |
| MySQL表名 | `hk_fivetierclaloans` |
| 中文名 | 港股贷款五级分类表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 不定期更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股贷款五级分类表，记录港股上市银行按依据借款人的实际还款能力进行的贷款质量分类。
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
| 7 | `FiveTierClaloans` | 贷款五级分类 | varchar2(50) | ✓ | 100.0% |  |
| 8 | `FiveTierClaloansCode` | 贷款五级分类代码 | number(10) | ✗ | 100.0% | 贷款五级分类代码(FiveTierClaloansCode)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 9 | `LoanAmount` | 本期贷款金额 | number(19,2) | ✓ | 97.67% |  |
| 10 | `PercOfTotalLoans` | 本期贷款比率(%) | number(19,4) | ✓ | 98.7% |  |
| 11 | `PreLoanAmount` | 上期贷款金额 | number(19,2) | ✓ | 86.63% |  |
| 12 | `PrPercOfTotalLoans` | 上期贷款比率(%) | number(19,4) | ✓ | 86.84% |  |
| 13 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM IN (2,3,4,5,10,11,12)，得到信息来源的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，10-申请版本，11-聆讯后资料集，12-招股章程。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1000,1100,1420)，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### FiveTierClaloansCode (贷款五级分类代码)

贷款五级分类代码(FiveTierClaloansCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2129 ，得到贷款五级分类代码的具体描述：1-正常类贷款，2-关注类贷款，3-次级类贷款，4-可疑类贷款，5-损失类贷款，10-不良贷款合计，20-贷款合计。

## SQL示例

```sql
-- 查询 港股贷款五级分类表 数据
SELECT *
FROM hk_fivetierclaloans
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
