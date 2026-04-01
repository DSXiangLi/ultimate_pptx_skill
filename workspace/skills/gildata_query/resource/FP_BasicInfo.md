# FP_BasicInfo

**中文名**: 金融产品概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_BasicInfo` |
| MySQL表名 | `fp_basicinfo` |
| 中文名 | 金融产品概况 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 100 |
| 版本 | 1.09 |

## 表描述

1.内容说明：本表记录金融产品（银行理财、信托计划、券商资管、保险资管、养老金产品）发行情况、成立情况、业绩基准、投资目标等信息。
2.信息来源：银行、信托、证券、资产管理公司、保险公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `RiskLevelCode` | 风险等级 | varchar2(12) | ✓ | 60.18% | 风险等级（RiskLevelCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 5 | `RegistrationCode` | 登记编码 | varchar2(50) | ✓ | 69.89% | 登记编码(RegistrationCode)：针对银行理财，记录全国银行业理财信息登记系统的登记编码；针对券商资管，记录... |
| 6 | `IncomeType` | 收益类型 | varchar2(12) | ✓ | 74.45% | 收益类型（IncomeType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 7 | `IfInitialShare` | 是否初始份额 | varchar2(12) | ✓ | 52.86% | 是否初始份额(IfInitialShare)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 8 | `ParValue` | 产品面值 | number(10) | ✓ | 43.48% |  |
| 9 | `CurrencyUnit` | 货币单位 | varchar2(12) | ✓ | 96.86% | 货币单位（CurrencyUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 10 | `RaisingType` | 募集方式 | varchar2(12) | ✓ | 43.33% | 募集方式（RaisingType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode... |
| 11 | `IssueObject` | 发行对象 | varchar2(200) | ✓ | 44.54% | 发行对象(IssueObject)：指产品的发行对象。1.自然人：个人，个人养老金客户，VIP，高净值客户；2.非自然人... |
| 12 | `IssueRegion` | 发行地区 | varchar2(500) | ✓ | 48.5% |  |
| 13 | `PurchaseChannels` | 购买渠道 | varchar2(200) | ✓ | 38.41% |  |
| 14 | `PopularizeStDate` | 销售起始日 | date | ✓ | 74.25% |  |
| 15 | `PopularizeEdDate` | 销售截止日 | date | ✓ | 67.25% |  |
| 16 | `EstablishmentDate` | 产品成立日 | date | ✓ | 88.12% |  |
| 17 | `MaturityDate` | 产品到期日 | date | ✓ | 84.29% |  |
| 18 | `ActMaturityDate` | 实际到期日 | date | ✓ | 28.71% |  |
| 19 | `MinInvestTerm` | 最短持有期限 | number(10,2) | ✓ | 53.31% |  |
| 20 | `MinInvestTermUnit` | 最短持有期限单位 | varchar2(12) | ✓ | 53.31% | 最短持有期限单位(MinInvestTermUnit)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标... |
| 21 | `InvestTerm` | 投资期限 | number(19,8) | ✓ | 84.22% |  |
| 22 | `InvestTermUnit` | 投资期限单位 | varchar2(12) | ✓ | 84.22% | 投资期限单位（InvestTermUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 23 | `LeastBuySum` | 最低销售金额(万元) | number(19,6) | ✓ | 61.44% | 最低销售金额(万元)（LeastBuySum）：在金融产品认购期时，处理认购期限额；在金融产品申购期时，处理申购期限额。 |
| 24 | `IncreasingAmountPER` | 递增金额(万元) | number(19,6) | ✓ | 35.75% | 递增金额(万元)（IncreasingAmountPER）：在金融产品认购期时，处理认购期限额；在金融产品申购期时，处理... |
| 25 | `MaximumApplying` | 申购上限(万份) | number(19,6) | ✓ | 5.35% |  |
| 26 | `InitialIssueVolCeiling` | 首次发行规模上限(亿元) | number(21,8) | ✓ | 8.32% | 首次发行规模上限(亿元)(InitialIssueVolCeiling)：指产品募集时的发行规模上限。 |
| 27 | `IssueVolCeiling` | 发行规模上限(亿元) | number(21,8) | ✓ | 38.45% | 发行规模上限(亿元)(IssueVolCeiling)：指产品在成立后的最新发行规模上限。 |
| 28 | `IssueVolFloor` | 发行规模下限(亿元) | number(21,8) | ✓ | 35.13% |  |
| 29 | `ActRaisingAmount` | 实际募资金额(亿元) | number(19,10) | ✓ | 42.1% |  |
| 30 | `PublishDesc` | 募集说明 | varchar2(1000) | ✓ | 22.65% |  |
| 31 | `IfCancel` | 是否允许撤单 | varchar2(12) | ✓ | 30.59% | 是否允许撤单（IfCancel）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 32 | `CancelRegulation` | 撤单规则 | clob | ✓ | 33.41% |  |
| 33 | `ExpAnEnYield` | 预期收益率上限(%) | number(19,6) | ✓ | 20.4% |  |
| 34 | `ExpAnBeYield` | 预期收益率下限(%) | number(19,6) | ✓ | 19.05% |  |
| 35 | `BenchmarkMax` | 年化业绩比较基准上限(%) | number(19,6) | ✓ | 36.01% |  |
| 36 | `BenchmarkMin` | 年化业绩比较基准下限(%) | number(19,6) | ✓ | 36.29% |  |
| 37 | `AnnualDays` | 年化天数 | number(10) | ✓ | 38.34% |  |
| 38 | `DeliveryDays` | 资金到账日 | varchar2(100) | ✓ | 38.68% |  |
| 39 | `InvestAdvisorCode` | 管理人 | varchar2(12) | ✓ | 100.0% | 管理人（InvestAdvisorCode）：与“企业码表（EP_CompanyMain）”中的“企业编码（Enterp... |
| 40 | `TrusteeCode` | 托管人 | varchar2(12) | ✓ | 51.63% | 托管人（TrusteeCode）：与“企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCo... |
| 41 | `OperationType` | 运作方式 | varchar2(12) | ✓ | 54.47% | 运作方式（OperationType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 42 | `IfDiscloseDP` | 是否披露每万份收益 | varchar2(12) | ✓ | 100.0% | 是否披露每万份收益（IfDiscloseDP）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（G... |
| 43 | `InvestmentType` | 投资性质 | varchar2(12) | ✓ | 57.89% | 投资性质（InvestmentType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 44 | `LinkObject` | 挂钩标的 | varchar2(12) | ✓ | 0.19% | 挂钩标的(LinkObject)：结构化银行理财产品的挂钩标的，与“金融产品指标码表（FP_Indicator）”中的“... |
| 45 | `IfPledge` | 是否可质押 | varchar2(12) | ✓ | 7.11% | 是否可质押（IfPledge）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 46 | `IfStructure` | 是否结构化 | varchar2(12) | ✓ | 66.91% | 是否结构化(IfStructure)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 47 | `IfTermination` | 能否提前终止 | varchar2(12) | ✓ | 38.88% | 能否提前终止（IfTermination）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 48 | `TerminationConditions` | 提前终止条件 | clob | ✓ | 31.42% |  |
| 49 | `IfEarlyRedeem` | 是否可提前赎回 | varchar2(12) | ✓ | 0.67% | 是否可提前赎回(IfEarlyRedeem)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 50 | `EarlyRedeemCondition` | 提前赎回条件 | clob | ✓ | 0.67% |  |
| 51 | `ApplyFrequency` | 申购频率 | varchar2(12) | ✓ | 47.08% | 申购频率(ApplyFrequency)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 52 | `Applyconfirmationtime` | 申购确认时间 | varchar2(200) | ✓ | 8.53% |  |
| 53 | `RedeemFrequency` | 赎回频率 | varchar2(12) | ✓ | 47.14% | 赎回频率(RedeemFrequency)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 54 | `RedeemDeliverytime` | 赎回到账时间 | varchar2(200) | ✓ | 9.1% |  |
| 55 | `PRConditions` | 申购和赎回说明 | clob | ✓ | 29.87% |  |
| 56 | `ApplyStartTime` | 申购起始时间 | varchar2(50) | ✓ | 9.53% |  |
| 57 | `ApplyEndTime` | 申购截止时间 | varchar2(50) | ✓ | 10.54% |  |
| 58 | `RedeemStartTime` | 赎回起始时间 | varchar2(50) | ✓ | 4.86% |  |
| 59 | `RedeemEndTime` | 赎回截止时间 | varchar2(50) | ✓ | 5.21% |  |
| 60 | `ChargeRateDesc` | 费用说明 | clob | ✓ | 20.68% |  |
| 61 | `MaturityYieldDesc` | 收益说明 | clob | ✓ | 11.28% |  |
| 62 | `InvestmentDesc` | 投资标的说明 | clob | ✓ | 14.98% |  |
| 63 | `InvestRatio` | 投资比例 | clob | ✓ | 26.03% |  |
| 64 | `InvestRestrictions` | 其他投资限制 | clob | ✓ | 17.64% |  |
| 65 | `InvestStrategy` | 投资策略 | clob | ✓ | 17.68% |  |
| 66 | `ProfitDistribution` | 收益分配频率 | varchar2(12) | ✓ | 23.1% | 收益分配频率(ProfitDistribution)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代... |
| 67 | `ProfitDistType` | 收益分配类型 | varchar2(12) | ✓ | 6.28% | 收益分配类型(ProfitDistType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 68 | `ProfitDistDesc` | 收益分配说明 | clob | ✓ | 24.05% |  |
| 69 | `TrustFunction` | 信托功能 | varchar2(12) | ✓ | 27.98% | 信托功能(TrustFunction)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 70 | `TrustFundUse` | 信托资金运用方式 | varchar2(12) | ✓ | 24.11% | 信托资金运用方式(TrustFundUse)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 71 | `MaturityType` | 期限类型 | varchar2(12) | ✓ | 28.53% | 期限类型(MaturityType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 72 | `ProjectSite` | 项目所在地 | varchar2(100) | ✓ | 8.85% |  |
| 73 | `Counterparty` | 交易对手 | varchar2(12) | ✓ | 9.61% | 交易对手(Counterparty)：与“企业码表（EP_CompanyMain）”中的“企业编码（Enterprise... |
| 74 | `InvestAdviser` | 投资顾问 | varchar2(12) | ✓ | 1.61% | 投资顾问(InvestAdviser)：与“企业码表（EP_CompanyMain）”中的“企业编码（Enterpris... |
| 75 | `InvestScope` | 投资领域 | varchar2(12) | ✓ | 23.59% | 投资领域(InvestScope)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode... |
| 76 | `StrArrangement` | 结构化安排 | varchar2(2000) | ✓ | 0.48% |  |
| 77 | `IfHaveMortgage` | 是否有抵押 | varchar2(12) | ✓ | 3.18% | 是否有抵押(IfHaveMortgage)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 78 | `IfHavePledge` | 是否有质押 | varchar2(12) | ✓ | 2.57% | 是否有质押(IfHavePledge)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 79 | `IFHaveGuarantee` | 是否有担保 | varchar2(12) | ✓ | 6.99% | 是否有担保(IFHaveGuarantee)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 80 | `RiskControlDesc` | 风控措施 | clob | ✓ | 13.11% |  |
| 81 | `ProductHighlights` | 产品亮点 | clob | ✓ | 15.76% |  |
| 82 | `RepaySource` | 还款来源 | clob | ✓ | 15.81% |  |
| 83 | `PlanType` | 计划类型 | varchar2(12) | ✓ | 1.45% | 计划类型(PlanType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关... |
| 84 | `PlanNature` | 计划性质 | varchar2(12) | ✓ | 0.59% | 计划性质(PlanNature)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 85 | `InvestDirection` | 计划投资方向 | varchar2(12) | ✓ | 2.51% | 计划投资方向(InvestDirection)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（G... |
| 86 | `ExitType` | 退出方式 | varchar2(12) | ✓ | 2.16% | 退出方式(ExitType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关... |
| 87 | `LockupPeriod` | 封闭期 | number(19,4) | ✓ | 0.73% |  |
| 88 | `LockupPerUn` | 封闭期单位 | varchar2(12) | ✓ | 0.73% | 封闭期单位(LockupPerUn)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 89 | `DurationDesc` | 封闭期说明 | varchar2(200) | ✓ | 1.71% |  |
| 90 | `SubsNum` | 有效认购户数 | number(10) | ✓ | 1.53% |  |
| 91 | `ValueByManager` | 管理人参与金额(元) | number(19,4) | ✓ | 0.4% |  |
| 92 | `InvestTarget` | 投资目标 | varchar2(2000) | ✓ | 2.09% |  |
| 93 | `InvestConcept` | 投资理念 | clob | ✓ | 0.33% |  |
| 94 | `RegisteredName` | 注册登记人 | varchar2(12) | ✓ | 0.2% |  |
| 95 | `ProductCode` | 人社部登记代码 | varchar2(20) | ✓ | 0.19% |  |
| 96 | `ConfirmationNum` | 确认函号 | varchar2(50) | ✓ | 0.2% |  |
| 97 | `ConfirmationDate` | 确认函日期 | date | ✓ | 0.2% |  |
| 98 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 99 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 100 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### RiskLevelCode (风险等级)

风险等级（RiskLevelCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到风险等级的具体描述：FCC0000001ST-低，FCC0000001SU-中低，FCC0000001SV-中，FCC0000001SW-中高，FCC0000001SX高，未披露。

### RegistrationCode (登记编码)

登记编码(RegistrationCode)：针对银行理财，记录全国银行业理财信息登记系统的登记编码；针对券商资管，记录中国基金业协会的备案编码；针对信托产品，记录中信登的产品编码；针对保险资管，记录中保登的产品登记编码；针对养老金产品，记录人社部的产品登记号。

### IncomeType (收益类型)

收益类型（IncomeType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到收益类型的具体描述：FCC0000001SZ-保证收益，FCC0000001T0-保本浮动，FCC0000001T1-非保本浮动，FCC00000040P-固定，FCC00000040Q-浮动，FCC00000040R-分层，未披露。

### IfInitialShare (是否初始份额)

是否初始份额(IfInitialShare)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否初始份额的具体描述：FCC000000005-是，FCC000000006-否。

### CurrencyUnit (货币单位)

货币单位（CurrencyUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到货币单位的具体描述：FCC000000015-人民币元，FCC00000000B-美元，FCC00000000C-港元，FCC00000000G-日本元，FCC00000000W-新加坡元，FCC00000002A-欧元，FCC00000002D-英镑，FCC00000002N-瑞士法郎，FCC00000002T-加拿大元，FCC00000002U-澳大利亚元，FCC00000002V-新西兰元。

### RaisingType (募集方式)

募集方式（RaisingType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到募集方式的具体描述：FCC0000001T2-公募，FCC0000001T3-私募。

### IssueObject (发行对象)

发行对象(IssueObject)：指产品的发行对象。1.自然人：个人，个人养老金客户，VIP，高净值客户；2.非自然人：机构，普通公司，法人，金融机构，同业机构，养老金客户；3.全部。

### MinInvestTermUnit (最短持有期限单位)

最短持有期限单位(MinInvestTermUnit)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到最短持有期限单位的具体描述：FCC0000001S7-年，FCC0000001S8-月，FCC0000001S9-日，FCC0000001TC-周。

## SQL示例

```sql
-- 查询 金融产品概况 数据
SELECT *
FROM fp_basicinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
