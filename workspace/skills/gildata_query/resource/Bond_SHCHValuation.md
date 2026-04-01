# Bond_SHCHValuation

**中文名**: 上清所债券估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SHCHValuation` |
| MySQL表名 | `bond_shchvaluation` |
| 中文名 | 上清所债券估值 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 32 |
| 版本 | 1 |

## 表描述

1.信息来源：银行间市场清算所股份有限公司。
2.收录清算所官方公布的估值数据，包含银行间和交易所债券。
3.包含“推荐”估值数据
4.数据范围：2011-09-06 至今
5.信息来源：上清所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValueFullPrice` | 日间估价全价(元) | number(18,10) | ✓ | 100.0% |  |
| 5 | `AccruInterest` | 日间应计利息(元) | number(18,12) | ✓ | 100.0% |  |
| 6 | `ValueCleanPrice` | 估价净价(元) | number(18,10) | ✓ | 100.0% |  |
| 7 | `VPYield` | 估价收益率(%) | number(18,12) | ✓ | 99.49% |  |
| 8 | `VPADuration` | 估价修正久期 | number(18,10) | ✓ | 99.08% |  |
| 9 | `VPConvexity` | 估价凸性 | number(18,10) | ✓ | 99.08% |  |
| 10 | `VPPointValue` | 估价基点价值 | number(18,10) | ✓ | 99.32% |  |
| 11 | `VPInterestDuration` | 估价利率久期 | number(18,10) | ✓ | 0.24% |  |
| 12 | `VPInterestConvexity` | 估价利率凸性 | number(18,10) | ✓ | 0.24% |  |
| 13 | `VPSpreadDuration` | 估价利差久期 | number(18,10) | ✓ | 0.24% |  |
| 14 | `VPSpreadConvexity` | 估价利差凸性 | number(18,10) | ✓ | 0.24% |  |
| 15 | `TrueFullPrice` | 真实全价(元) | number(18,10) | ✓ | 6.92% |  |
| 16 | `TrueCleanPrice` | 真实净价(元) | number(18,10) | ✓ | 6.92% |  |
| 17 | `TrueYield` | 真实收益率(%) | number(18,12) | ✓ | 6.91% |  |
| 18 | `TrueRemainMaturity` | 实际待偿期(年) | number(18,10) | ✓ | 100.0% |  |
| 19 | `TrueADuration` | 真实修正久期 | number(18,10) | ✓ | 6.9% |  |
| 20 | `TrueConvexity` | 真实凸性 | number(18,10) | ✓ | 6.9% |  |
| 21 | `TruePointValue` | 真实基点价值 | number(18,10) | ✓ | 6.91% |  |
| 22 | `TrueInterestDuration` | 真实利差久期 | number(18,10) | ✓ | 0.02% |  |
| 23 | `TrueInterestConvexity` | 真实利差凸性 | number(18,10) | ✓ | 0.02% |  |
| 24 | `TrueSpreadDuration` | 真实利率久期 | number(18,10) | ✓ | 0.02% |  |
| 25 | `TrueSpreadConvexity` | 真实利率凸性 | number(18,10) | ✓ | 0.02% |  |
| 26 | `SettFullPrice` | 日终估价全价(元) | number(18,10) | ✓ | 100.0% |  |
| 27 | `SettAccruInterest` | 日终应计利息(元) | number(18,12) | ✓ | 100.0% |  |
| 28 | `ResidualCapital` | 剩余本金(元) | number(18,10) | ✓ | 99.81% |  |
| 29 | `CredibilityCode` | 可信度代码 | number(3) | ✗ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 30 | `CredibilityDesc` | 可信度描述 | varchar2(50) | ✓ | 100.0% |  |
| 31 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

## SQL示例

```sql
-- 查询 上清所债券估值 数据
SELECT *
FROM bond_shchvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
