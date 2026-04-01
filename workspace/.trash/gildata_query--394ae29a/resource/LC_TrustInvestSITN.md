# LC_TrustInvestSITN

**中文名**: 上市公司投资理财明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_TrustInvestSITN` |
| MySQL表名 | `lc_trustinvestsitn` |
| 中文名 | 上市公司投资理财明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 定报：季更新(披露的少)/半年更新 |
| 字段数量 | 27 |
| 版本 | 1 |

## 表描述

1.董事会同意公司拟使用闲置自有资金或闲置募集资金通过商业银行理财、信托理财及其他理财工具进行运作和管理。该表收录了上市公司购买理财产品情况,包括委托理财产品名称,委托理财金额,委托理财起始日期,委托理财终止日期等内容。
2.数据范围：2016年年报至今
3.信息来源：上市公司定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 7 | `TrusteeName` | 受托人\合作方 | varchar2(200) | ✓ | 99.81% |  |
| 8 | `TrusteeCode` | 受托人编码 | number(10) | ✓ | 0.0% | 受托人编码(TrusteeCode)和机构基本资料表（LC_InstiArchive）中企业编号（CompanyCode... |
| 9 | `TrustInvestName` | 委托理财产品名称 | varchar2(200) | ✓ | 99.68% |  |
| 10 | `TrustInvestCode` | 理财产品编码 | number(10) | ✓ | 0.0% | 理财产品编码：与理财产品主表（SF_PlanMain）中的“理财产品内部编码(InnerCode)”关联，得到“中文名称... |
| 11 | `CurrencyUnit` | 投资及收益币种 | number(10) | ✓ | 100.0% | 投资及收益币种 ：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，“LB=1068”，得到  ... |
| 12 | `TrustInvestSum` | 委托理财金额(元) | number(19,4) | ✓ | 99.75% |  |
| 13 | `TrustInvestBeginDate` | 委托理财起始日期 | date | ✓ | 99.32% |  |
| 14 | `TrustInvestEndDate` | 委托理财终止日期 | date | ✓ | 94.33% |  |
| 15 | `PromisedIncome` | 报酬确定方式 | varchar2(1000) | ✓ | 91.49% |  |
| 16 | `EstimateProfit` | 预计收益(元) | number(19,4) | ✓ | 43.6% |  |
| 17 | `RealRecoveryPrincipal` | 实际收回本金金额(元) | number(19,4) | ✓ | 14.68% |  |
| 18 | `RealGetProfit` | 实际获得收益(元) | number(19,4) | ✓ | 18.92% |  |
| 19 | `PLActualSum` | 报告期实际损益金额(元) | number(19,4) | ✓ | 59.05% |  |
| 20 | `PLActualRecovery` | 报告期损益实际收回情况(元) | number(19,4) | ✓ | 27.34% |  |
| 21 | `Relationship` | 关联关系 | varchar2(200) | ✓ | 2.83% |  |
| 22 | `IfConnectTransaction` | 是否关联交易 | number(10) | ✓ | 15.16% | 是否关联交易（IfConnectTransaction），该字段固定以下常量：1-是；2-否 |
| 23 | `FundSource` | 资金来源 | varchar2(200) | ✓ | 93.27% |  |
| 24 | `Remark` | 备注 | varchar2(500) | ✓ | 0.08% |  |
| 25 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到股票的交易代码、简称等。

### TrusteeCode (受托人编码)

受托人编码(TrusteeCode)和机构基本资料表（LC_InstiArchive）中企业编号（CompanyCode）关联（该字段暂不维护。）

### TrustInvestCode (理财产品编码)

理财产品编码：与理财产品主表（SF_PlanMain）中的“理财产品内部编码(InnerCode)”关联，得到“中文名称、产品简称”等（该字段暂不维护。）

### CurrencyUnit (投资及收益币种)

投资及收益币种 ：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，“LB=1068”，得到
      “货币单位”描述。
      1000-美元，1100-港元，1420-人民币元，3000-欧元，9900-其他货币

### IfConnectTransaction (是否关联交易)

是否关联交易（IfConnectTransaction），该字段固定以下常量：1-是；2-否

## SQL示例

```sql
-- 查询 上市公司投资理财明细 数据
SELECT *
FROM lc_trustinvestsitn
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
