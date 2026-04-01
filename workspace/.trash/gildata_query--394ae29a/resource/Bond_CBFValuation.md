# Bond_CBFValuation

**中文名**: 中债境外债券估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBFValuation` |
| MySQL表名 | `bond_cbfvaluation` |
| 中文名 | 中债境外债券估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债估值中心对中资境外债券的估值数据，包含“推荐”和“非推荐”估值数据。
2.数据范围：2017-12-28至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✓ | 66.34% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `SecuCode` | 证券代码 | varchar2(50) | ✗ | 100.0% |  |
| 5 | `ValueFullPrice` | 估价全价 | number(18,8) | ✓ | 100.0% |  |
| 6 | `AccruInterest` | 应计利息 | number(18,8) | ✓ | 100.0% |  |
| 7 | `ValueCleanPrice` | 估价净价 | number(18,8) | ✓ | 100.0% |  |
| 8 | `VPYield` | 估价收益率(%) | number(18,8) | ✓ | 100.0% |  |
| 9 | `VPADuration` | 估价修正久期 | number(18,8) | ✓ | 97.88% |  |
| 10 | `VPConvexity` | 估价凸性 | number(18,8) | ✓ | 97.88% |  |
| 11 | `VPPointValue` | 估价基点价值 | number(18,8) | ✓ | 100.0% |  |
| 12 | `VPInterestDuration` | 估价利率久期 | number(18,8) | ✓ | 2.12% |  |
| 13 | `VPInterestConvexity` | 估价利率凸性 | number(18,8) | ✓ | 2.12% |  |
| 14 | `VPSpreadDuration` | 估价利差久期 | number(18,8) | ✓ | 2.12% |  |
| 15 | `VPSpreadConvexity` | 估价利差凸性 | number(18,8) | ✓ | 2.12% |  |
| 16 | `TrueRemainMaturity` | 待偿期(年) | number(18,8) | ✓ | 100.0% |  |
| 17 | `CredibilityCode` | 可信度代码 | number(10) | ✗ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 18 | `CredibilityDesc` | 可信度描述 | varchar2(50) | ✓ | 88.47% |  |
| 19 | `SettFullPrice` | 日终估价全价 | number(18,8) | ✓ | 100.0% |  |
| 20 | `SettAccruInterest` | 日终应计利息 | number(18,8) | ✓ | 100.0% |  |
| 21 | `ResidualCapital` | 剩余本金(元) | number(18,8) | ✓ | 100.0% |  |
| 22 | `PointSpreadYield` | 点差收益率(%) | number(18,10) | ✓ | 3.85% |  |
| 23 | `YieldTypeCode` | 收益率类型代码 | number(10) | ✓ | 100.0% | 收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益... |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

### YieldTypeCode (收益率类型代码)

收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益率

## SQL示例

```sql
-- 查询 中债境外债券估值 数据
SELECT *
FROM bond_cbfvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
