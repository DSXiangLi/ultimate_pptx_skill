# Bond_CBValuation

**中文名**: 中债估值信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBValuation` |
| MySQL表名 | `bond_cbvaluation` |
| 中文名 | 中债估值信息 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 39 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录对各类债券的估值数据、涵盖债券违约期间的估值。
2.数据范围：2006-03-01 至今
3.信息来源：中央国债登记结算有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `Exchange` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN... |
| 5 | `AccruInterest` | 应计利息(元) | number(19,4) | ✓ | 99.17% |  |
| 6 | `ValueFullPrice` | 估价全价 | number(19,4) | ✓ | 100.0% |  |
| 7 | `ValueCleanPrice` | 估价净价 | number(19,4) | ✓ | 99.17% |  |
| 8 | `VPYield` | 估价收益率(%) | number(18,8) | ✓ | 99.32% |  |
| 9 | `VPADuration` | 估价修正久期 | number(18,8) | ✓ | 98.44% |  |
| 10 | `VPConvexity` | 估价凸性 | number(18,8) | ✓ | 98.44% |  |
| 11 | `VPPointValue` | 估价基点价值 | number(18,8) | ✓ | 99.17% |  |
| 12 | `VPInterestDuration` | 估价利率久期 | number(18,8) | ✓ | 4.52% |  |
| 13 | `VPInterestConvexity` | 估价利率凸性 | number(18,8) | ✓ | 4.52% |  |
| 14 | `VPSpreadDuration` | 估价利差久期 | number(18,8) | ✓ | 4.61% |  |
| 15 | `VPSpreadConvexity` | 估价利差凸性 | number(18,8) | ✓ | 4.61% |  |
| 16 | `TrueFullPrice` | 加权平均结算全价(真实全价)(元) | number(19,4) | ✓ | 4.74% |  |
| 17 | `TrueCleanPrice` | 加权平均结算净价(真实净价)(元) | number(19,4) | ✓ | 4.74% |  |
| 18 | `TrueYield` | 加权平均结算价收益率(真实收益率) | number(18,8) | ✓ | 4.74% |  |
| 19 | `TrueRemainMaturity` | 实际待偿期(年) | number(18,8) | ✓ | 99.17% |  |
| 20 | `TrueADuration` | 加权平均结算价修正久期(真实修正久期) | number(18,8) | ✓ | 4.72% |  |
| 21 | `TrueConvexity` | 加权平均结算价凸性(真实凸性) | number(18,8) | ✓ | 4.72% |  |
| 22 | `TruePointValue` | 加权平均结算价基点价值(真实基点价值) | number(18,8) | ✓ | 4.74% |  |
| 23 | `TrueInterestDuration` | 加权平均结算价利率久期(真实利率久期) | number(18,8) | ✓ | 3.8% |  |
| 24 | `TrueInterestConvexity` | 加权平均结算价利率凸性(真实利率凸性) | number(18,8) | ✓ | 3.8% |  |
| 25 | `TrueSpreadDuration` | 加权平均结算价利差久期(真实利差久期) | number(18,8) | ✓ | 3.9% |  |
| 26 | `TrueSpreadConvexity` | 加权平均结算价利差凸性(真实利差凸性) | number(18,8) | ✓ | 3.9% |  |
| 27 | `AbLiqCoefficient` | 绝对流动性系数 | number(18,8) | ✓ | 0.0% |  |
| 28 | `PositionPercent` | 位置百分比 | number(18,8) | ✓ | 0.0% |  |
| 29 | `RelativeLiqCoefficient` | 相对流动性系数 | number(18,8) | ✓ | 0.0% |  |
| 30 | `RelativeLiqNum` | 相对流动性取值 | number(18,8) | ✓ | 0.0% |  |
| 31 | `SettFullPrice` | 日终估价全价 | number(10,4) | ✓ | 97.95% |  |
| 32 | `SettAccruInterest` | 日终应计利息 | number(9,6) | ✓ | 97.95% |  |
| 33 | `ResidualCapital` | 剩余本金(元) | number(10,4) | ✓ | 97.95% |  |
| 34 | `PointSpreadYield` | 点差收益率(%) | number(9,6) | ✓ | 3.39% |  |
| 35 | `EstimatedAllocatingR` | 估算的行权后票面利率(%) | number(18,8) | ✓ | 23.74% |  |
| 36 | `SpecialMark` | 特殊标识 | number(10) | ✓ | 82.06% | 特殊标识(SpecialMark)，该字段固定以下常量：1-违约资产估值，2-信用风险缓释工具估值，11-国债、地方政府... |
| 37 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 38 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 39 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### Exchange (证券市场)

证券市场(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,84,89,90,71)，得到证券市场的具体描述：71-柜台交易市场，83-上海证券交易所，84-其他市场，89-银行间债券市场，90-深圳证券交易所。

### SpecialMark (特殊标识)

特殊标识(SpecialMark)，该字段固定以下常量：1-违约资产估值，2-信用风险缓释工具估值，11-国债、地方政府债、政策性银行债、企业债、商业银行债、银行间资产支持证券估值
12-中期票据、短期（超短期）融资券及标准化票据估值
13-非公开定向债务融资工具(PPN)和其他债务融资工具估值
14-同业存单估值
15-公司债估值
16-资产支持证券和资产支持票据估值

## SQL示例

```sql
-- 查询 中债估值信息 数据
SELECT *
FROM bond_cbvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
