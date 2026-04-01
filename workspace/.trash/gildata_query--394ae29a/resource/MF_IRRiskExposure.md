# MF_IRRiskExposure

**中文名**: 公募基金利率风险敞口

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IRRiskExposure` |
| MySQL表名 | `mf_irriskexposure` |
| 中文名 | 公募基金利率风险敞口 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 57 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金年报/半年报的财务报表附注中的基金利率风险敞口数据。
2.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
3.该表中各财务科目下数据对应的货币单位均为人民币元。
4.历史数据：2006年12月起-至今。
5.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.77% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `BulletinType` | 公告类别 | number(10) | ✓ | 87.51% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB=1032，得到公告类别... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `DueMaturity` | 到期期限 | number(10) | ✗ | 100.0% | 到期期限(DueMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1541，得到到期期... |
| 9 | `Mark` | 调整标志 | number(10) | ✗ | 100.0% | 调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1... |
| 10 | `Deposit` | 银行存款 | number(19,4) | ✓ | 51.37% |  |
| 11 | `SettlementProvi` | 结算备付金 | number(19,4) | ✓ | 41.53% |  |
| 12 | `RefundableDeposit` | 存出保证金 | number(19,4) | ✓ | 42.03% |  |
| 13 | `TradingAssets` | 交易性金融资产 | number(19,4) | ✓ | 80.89% |  |
| 14 | `StockInvestment` | 其中:股票投资 | number(19,4) | ✓ | 0.39% |  |
| 15 | `BondInvestment` | 债券投资 | number(19,4) | ✓ | 2.45% |  |
| 16 | `ABSInvestment` | 资产支持证券投资 | number(19,4) | ✓ | 0.19% |  |
| 17 | `FundInvestment` | 基金投资 | number(19,4) | ✓ | 0.0% |  |
| 18 | `WarrentInvestment` | 权证投资 | number(19,4) | ✓ | 0.02% |  |
| 19 | `DerivativeAssets` | 衍生金融资产 | number(19,4) | ✓ | 1.04% |  |
| 20 | `BoughtSellbackAssets` | 买入返售金融资产 | number(19,4) | ✓ | 13.56% |  |
| 21 | `SecuSettlementReceivables` | 应收证券清算款 | number(19,4) | ✓ | 22.98% |  |
| 22 | `InterestReceivables` | 应收利息 | number(19,4) | ✓ | 25.91% |  |
| 23 | `DividendReceivables` | 应收股利 | number(19,4) | ✓ | 4.87% |  |
| 24 | `ApplyingReceivables` | 应收申购款 | number(19,4) | ✓ | 38.37% |  |
| 25 | `AccountReceivables` | 应收帐款 | number(19,4) | ✓ | 0.0% |  |
| 26 | `OtherReceivables` | 其他应收款 | number(19,4) | ✓ | 0.04% |  |
| 27 | `DeferrredExpense` | 待摊费用 | number(19,4) | ✓ | 0.01% |  |
| 28 | `OtherAssets` | 其他资产 | number(19,4) | ✓ | 5.61% |  |
| 29 | `AExceptionalItems` | ##资产特殊项目 | number(19,4) | ✓ | 0.11% |  |
| 30 | `AAdjustmentItems` | ##资产调整项目 | number(19,4) | ✓ | 0.0% |  |
| 31 | `TotalAssets` | 资产总计 | number(19,4) | ✓ | 98.86% |  |
| 32 | `ShortTermLoan` | 短期借款 | number(19,4) | ✓ | 0.76% |  |
| 33 | `TradingLiability` | 交易性金融负债 | number(19,4) | ✓ | 0.8% |  |
| 34 | `DerivativeLiability` | 衍生金融负债 | number(19,4) | ✓ | 0.77% |  |
| 35 | `SoldBuybackSecuProceeds` | 卖出回购金融资产款 | number(19,4) | ✓ | 17.12% |  |
| 36 | `SecuSettlementPayables` | 应付证券清算款 | number(19,4) | ✓ | 24.34% |  |
| 37 | `RedemptionMoneyPayable` | 应付赎回款 | number(19,4) | ✓ | 34.04% |  |
| 38 | `RedemptionFeePayable` | 应付赎回费 | number(19,4) | ✓ | 0.1% |  |
| 39 | `ManagementFeePayable` | 应付管理人报酬 | number(19,4) | ✓ | 48.9% |  |
| 40 | `TrustFeePayable` | 应付托管费 | number(19,4) | ✓ | 48.99% |  |
| 41 | `SalesFeePayable` | 应付销售服务费 | number(19,4) | ✓ | 25.1% |  |
| 42 | `TransactionFeePayable` | 应付交易费用 | number(19,4) | ✓ | 24.52% |  |
| 43 | `TaxsPayable` | 应交税费 | number(19,4) | ✓ | 22.32% |  |
| 44 | `InterestPayable` | 应付利息 | number(19,4) | ✓ | 7.99% |  |
| 45 | `ProfitPayable` | 应付利润 | number(19,4) | ✓ | 2.67% |  |
| 46 | `AccountPayable` | 应付帐款 | number(19,4) | ✓ | 0.0% |  |
| 47 | `OtherPayable` | 其他应付款 | number(19,4) | ✓ | 0.03% |  |
| 48 | `AccruedExpense` | 预提费用 | number(19,4) | ✓ | 0.18% |  |
| 49 | `OtherLiability` | 其他负债 | number(19,4) | ✓ | 48.51% |  |
| 50 | `LExceptionalItems` | ##负债特殊项目 | number(19,4) | ✓ | 0.01% |  |
| 51 | `LAdjustmentItems` | ##负债调整项目 | number(19,4) | ✓ | 0.0% |  |
| 52 | `TotalLiability` | 负债合计 | number(19,4) | ✓ | 58.25% |  |
| 53 | `IRSensitivityGap` | 利率敏感性缺口 | number(19,4) | ✓ | 99.97% |  |
| 54 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 0.13% |  |
| 55 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 56 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 57 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB=1032，得到公告类别的具体描述：1-招股说明书，2-招股意向书，3-配股说明书，4-上市公告书，5-年度报告，6-中期报告，7-公司章程，8-增发新股招股说明书，9-增发新股招股意向书，10-增发新股上市公告书，11-可转换债券募集说明书，12-可转换债券上市公告书，13-国家股配售说明书，14-吸收合并预案说明书，15-吸收合并公告书，16-债券发行公告，17-第一季度报告，18-国有股回购公告书，19-基金招募说明书，20-基金上市公告书，21-基金扩募说明书，22-B股配股说明书，23-第三季度报告，24-股份转让公告书，25-招股说明书(申报稿)，26-公开转让说明书，50-基金契约，51-基金经理照片，52-基金契约摘要，61-第二季度报告，63-第四季度报告，65-中期报告摘要，67-年度报告摘要，71-公司治理制度，72-实际控制人结构图，73-发行上市书附录，75-发行上市书摘要，99-临时公告，101-发行公告，104-上市公告，107-回访报告，110-定期报告摘要更正补充公告，113-定期报告更正补充公告，116-公司章程修正公告，118-基金招募说明书更新摘要，119-基金招募说明书更新，121-基金契约修正，123-基金托管协议，130-募集说明书，131-募集说明书摘要，132-季度报告，133-招股意向书摘要，134-增发股招股意向书摘要，135-招股说明书摘要，136-配股说明书摘要，137-基金招募说明书摘要，138-可转换债券募集说明书摘要，139-第三季度报告正文，140-第一季度报告正文，141-基金产品资料概要，142-基金产品资料概要更新，143-月度报告，144-周度报告，150-优先股发行预案，151-优先股分红预案，152-优先股发行预案修正，153-优先股分红预案修正，154-优先股信用评级报告，155-基金合同生效公告，156-资产评估报告。

### DueMaturity (到期期限)

到期期限(DueMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1541，得到到期期限的具体描述：1-1个月以内，2-1-3个月，3-3个月-1年，4-1年以内，5-1-5年，6-5年以上，7-1-6个月，8-6个月至1年，9-不计息，10-6个月以上，11-6个月至5年，12-1年以上，13-5-10年，14-3至6个月，99-合计。

### Mark (调整标志)

调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,7)，得到调整标志的具体描述：1-是，2-否，7-二季末调整。

## SQL示例

```sql
-- 查询 公募基金利率风险敞口 数据
SELECT *
FROM mf_irriskexposure
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
