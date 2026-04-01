# Bond_CBDescription

**中文名**: 中债债券基本资料表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDescription` |
| MySQL表名 | `bond_cbdescription` |
| 中文名 | 中债债券基本资料表 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 40 |
| 版本 | 1 |

## 表描述

1.内容说明：本表用于中债发布的债券首次发行以及增发的债券基本要素信息。
2.数据范围：2005-04-11-至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `IssueFrequency` | 发行次数 | number(10) | ✗ | 100.0% |  |
| 4 | `SecuAbbr` | 债券简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `SecuCode` | 债券代码 | varchar2(30) | ✓ | 100.0% |  |
| 6 | `IssueDate` | 发行日期 | date | ✓ | 100.0% |  |
| 7 | `ActualIssueSize` | 实际发行量(亿元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `IntPaymentMethod` | 付息方式 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `PayInterestEffency` | 付息周期(月) | varchar2(20) | ✓ | 96.84% |  |
| 10 | `CouponRate` | 票面利率(%) | number(9,6) | ✓ | 100.0% |  |
| 11 | `ValueDate` | 起息日 | date | ✓ | 100.0% |  |
| 12 | `EndDate` | 到期日 | date | ✓ | 100.0% |  |
| 13 | `ListedDate` | 上市流通日 | date | ✓ | 97.39% |  |
| 14 | `Maturity` | 债券期限 | number(10,6) | ✓ | 100.0% |  |
| 15 | `BasicSpread` | 基本利差(%) | number(9,6) | ✓ | 100.0% |  |
| 16 | `CurrentBaseRate` | 当期基础利率(%) | number(9,6) | ✓ | 100.0% |  |
| 17 | `FirstPaymentDate` | 首次划款日 | date | ✓ | 99.99% |  |
| 18 | `IssueFeeRate` | 发行手续费率(%) | number(19,4) | ✓ | 100.0% |  |
| 19 | `RedemptionFeeRate` | 兑付手续费率(%) | number(19,4) | ✓ | 71.3% |  |
| 20 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 100.0% |  |
| 21 | `RefYTM` | 参考收益率(%) | number(10,6) | ✓ | 0.0% |  |
| 22 | `OptionType` | 选择权类别 | varchar2(100) | ✓ | 7.57% |  |
| 23 | `Remark` | 备注 | varchar2(1000) | ✓ | 0.0% |  |
| 24 | `ISIN` | ISIN码 | varchar2(50) | ✓ | 94.35% |  |
| 25 | `BondCreditRating` | 债券信用评级 | varchar2(20) | ✓ | 75.3% |  |
| 26 | `BondCreditRatingCompanyCode` | 债券信用评级机构 | varchar2(200) | ✓ | 75.43% |  |
| 27 | `IssuerCreditRating` | 主体信用评级 | varchar2(20) | ✓ | 13.76% |  |
| 28 | `IssuerCreditRatingCompanyCode` | 主体信用评级机构 | varchar2(200) | ✓ | 75.43% |  |
| 29 | `ChiName` | 债券名称 | varchar2(200) | ✓ | 100.0% |  |
| 30 | `BondNature` | 债券品种 | number(10) | ✓ | 100.0% | 债券品种(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB=2659，得到债券品种的具... |
| 31 | `PlanIssueSize` | 计划发行量(亿元) | number(19,4) | ✓ | 100.0% |  |
| 32 | `CirculationStatus` | 流通状态 | varchar2(100) | ✓ | 100.0% |  |
| 33 | `CirculationMarket` | 流通场所 | varchar2(200) | ✓ | 99.45% |  |
| 34 | `FirstIssueMarket` | 首次发行范围 | varchar2(200) | ✓ | 99.46% |  |
| 35 | `Issuer` | 发行人 | varchar2(200) | ✓ | 99.98% |  |
| 36 | `FRNRefRateSelecrRemark` | 浮动利率基准 | varchar2(200) | ✓ | 4.84% |  |
| 37 | `ResidualCapital` | 剩余本金值(元) | number(19,4) | ✓ | 100.0% |  |
| 38 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 39 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 40 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BondNature (债券品种)

债券品种(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB=2659，得到债券品种的具体描述：1-保险公司金融债，2-超短期融资券，3-储蓄国债，4-地方企业债，5-地方政府债，6-短期融资券，7-二级资本工具，8-非银行金融机构债，9-扶贫专项金融债，10-国际机构债券，11-集合票据，12-集合企业债，13-记账式国债，14-交易所资产支持证券，15-离岸债券，16-凭证式国债，17-其他一级资本工具，18-商业银行债券，19-项目收益债券，20-央行票据，21-证券公司短期融资券，22-证券公司债，23-政策性银行债券，24-政府支持机构债，25-中期票据，26-中央企业债，27-资产支持证券。

## SQL示例

```sql
-- 查询 中债债券基本资料表 数据
SELECT *
FROM bond_cbdescription
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
