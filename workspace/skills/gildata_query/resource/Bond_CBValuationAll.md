# Bond_CBValuationAll

**中文名**: 中债估值信息(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBValuationAll` |
| MySQL表名 | `bond_cbvaluationall` |
| 中文名 | 中债估值信息(全) |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 41 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录对各类债券的估值数据、涵盖债券违约期间的估值，并且包含“推荐”和“非推荐”估值数据。
3.数据范围：2006-03-01 至今
4.信息来源：中央国债登记结算有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValueFullPrice` | 估价全价 | number(18,8) | ✓ | 100.0% |  |
| 5 | `AccruInterest` | 应计利息(元) | number(18,10) | ✓ | 99.29% |  |
| 6 | `ValueCleanPrice` | 估价净价 | number(18,8) | ✓ | 99.29% |  |
| 7 | `VPYield` | 估价收益率(%) | number(18,10) | ✓ | 99.42% |  |
| 8 | `VPADuration` | 估价修正久期 | number(18,8) | ✓ | 98.17% |  |
| 9 | `VPConvexity` | 估价凸性 | number(18,8) | ✓ | 98.17% |  |
| 10 | `VPPointValue` | 估价基点价值 | number(18,8) | ✓ | 99.28% |  |
| 11 | `VPInterestDuration` | 估价利率久期 | number(18,8) | ✓ | 2.47% |  |
| 12 | `VPInterestConvexity` | 估价利率凸性 | number(18,8) | ✓ | 2.47% |  |
| 13 | `VPSpreadDuration` | 估价利差久期 | number(18,8) | ✓ | 2.47% |  |
| 14 | `VPSpreadConvexity` | 估价利差凸性 | number(18,8) | ✓ | 2.47% |  |
| 15 | `TrueFullPrice` | 加权平均结算全价(真实全价)(元) | number(18,8) | ✓ | 2.16% |  |
| 16 | `TrueCleanPrice` | 加权平均结算净价(真实净价)(元) | number(18,8) | ✓ | 2.16% |  |
| 17 | `TrueYield` | 加权平均结算价收益率(真实收益率)(%) | number(18,10) | ✓ | 2.16% |  |
| 18 | `TrueRemainMaturity` | 实际待偿期(年) | number(18,8) | ✓ | 99.29% |  |
| 19 | `TrueADuration` | 加权平均结算价修正久期(真实修正久期) | number(18,8) | ✓ | 2.12% |  |
| 20 | `TrueConvexity` | 加权平均结算价凸性(真实凸性) | number(18,8) | ✓ | 2.12% |  |
| 21 | `TruePointValue` | 加权平均结算价基点价值(真实基点价值) | number(18,8) | ✓ | 2.16% |  |
| 22 | `TrueInterestDuration` | 加权平均结算价利率久期(真实利率久期) | number(18,8) | ✓ | 1.25% |  |
| 23 | `TrueInterestConvexity` | 加权平均结算价利率凸性(真实利率凸性) | number(18,8) | ✓ | 1.25% |  |
| 24 | `TrueSpreadDuration` | 加权平均结算价利差久期(真实利差久期) | number(18,8) | ✓ | 1.25% |  |
| 25 | `TrueSpreadConvexity` | 加权平均结算价利差凸性(真实利差凸性) | number(18,8) | ✓ | 1.25% |  |
| 26 | `AbLiqCoefficient` | 绝对流动性系数 | number(18,8) | ✓ | 0.0% |  |
| 27 | `PositionPercent` | 位置百分比 | number(18,8) | ✓ | 0.0% |  |
| 28 | `RelativeLiqCoefficient` | 相对流动性系数 | number(18,8) | ✓ | 0.0% |  |
| 29 | `RelativeLiqNum` | 相对流动性取值 | number(18,8) | ✓ | 0.0% |  |
| 30 | `CredibilityCode` | 可信度代码 | number(3) | ✓ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 31 | `CredibilityDesc` | 可信度描述 | varchar2(50) | ✓ | 100.0% |  |
| 32 | `SettFullPrice` | 日终估价全价 | number(18,8) | ✓ | 99.08% |  |
| 33 | `SettAccruInterest` | 日终应计利息 | number(18,10) | ✓ | 99.08% |  |
| 34 | `ResidualCapital` | 剩余本金(元) | number(18,8) | ✓ | 99.29% |  |
| 35 | `PointSpreadYield` | 点差收益率(%) | number(18,10) | ✓ | 2.32% |  |
| 36 | `YieldCode` | 收益率类型代码 | number(3) | ✓ | 99.29% | 收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益... |
| 37 | `EstimatedAllocatingR` | 估算的行权后票面利率(%) | number(18,8) | ✓ | 28.65% |  |
| 38 | `SpecialMark` | 特殊标识 | number(10) | ✓ | 82.69% | 特殊标识(SpecialMark)，该字段固定以下常量：1-违约资产估值，2-信用风险缓释工具估值，11-国债、地方政府... |
| 39 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 40 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 41 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

### YieldCode (收益率类型代码)

收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益率

### SpecialMark (特殊标识)

特殊标识(SpecialMark)，该字段固定以下常量：1-违约资产估值，2-信用风险缓释工具估值，11-国债、地方政府债、政策性银行债、企业债、商业银行债、银行间资产支持证券估值
12-中期票据、短期（超短期）融资券及标准化票据估值
13-非公开定向债务融资工具(PPN)和其他债务融资工具估值
14-同业存单估值
15-公司债估值
16-资产支持证券和资产支持票据估值

## SQL示例

```sql
-- 查询 中债估值信息(全) 数据
SELECT *
FROM bond_cbvaluationall
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
