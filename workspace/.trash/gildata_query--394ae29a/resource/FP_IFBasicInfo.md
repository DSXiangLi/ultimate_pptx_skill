# FP_IFBasicInfo

**中文名**: 保险理财产品概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFBasicInfo` |
| MySQL表名 | `fp_ifbasicinfo` |
| 中文名 | 保险理财产品概况 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1 |

## 表描述

收录保险理财（分红险、万能险和投连险）的投保年龄、犹豫期、适合人群、缴费方式、保险责任、产品特点等基本信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 64.7% |  |
| 3 | `FinProCode` | 保险产品编码 | varchar2(12) | ✗ | 100.0% | 保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `InsuranceType` | 保险类别 | varchar2(12) | ✗ | 100.0% | 保险类别(InsuranceType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 5 | `CompoundMode` | 主附险 | varchar2(12) | ✓ | 100.0% | 主附险(CompoundMode) ：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 6 | `PlanState` | 产品状态 | varchar2(12) | ✓ | 87.74% | 产品状态(PlanState)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 7 | `InsuringAgeFloor` | 投保年龄下限(周岁) | number(19,8) | ✓ | 78.98% |  |
| 8 | `InsuringAgeCeiling` | 投保年龄上限(周岁) | number(19,8) | ✓ | 78.12% |  |
| 9 | `InsuringAgeDesc` | 投保年龄描述 | clob | ✓ | 79.19% |  |
| 10 | `ChargingInterval` | 保险期间 | clob | ✓ | 92.71% |  |
| 11 | `SuitableCrowd` | 适合人群 | clob | ✓ | 81.62% |  |
| 12 | `HesitationPeriod` | 犹豫期 | varchar2(100) | ✓ | 83.85% |  |
| 13 | `CurrencyCode` | 币种 | varchar2(12) | ✓ | 89.57% | 币种(CurrencyCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 14 | `PremiumRemark` | 保费说明 | clob | ✓ | 94.21% |  |
| 15 | `InsuredLiability` | 保险责任 | clob | ✓ | 96.2% |  |
| 16 | `ExcludedLiability` | 责任免除 | clob | ✓ | 89.3% |  |
| 17 | `AmountCovered` | 保险金额 | clob | ✓ | 54.25% |  |
| 18 | `FeeRemark` | 费用收取 | clob | ✓ | 48.22% |  |
| 19 | `InvestStrategy` | 投资策略 | clob | ✓ | 60.63% |  |
| 20 | `ProductFeatures` | 产品特点 | clob | ✓ | 44.86% |  |
| 21 | `RiskRemark` | 风险提示 | clob | ✓ | 65.33% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (保险产品编码)

保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### InsuranceType (保险类别)

保险类别(InsuranceType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到保险类别的具体描述：FCC00000164G-分红险，FCC00000164H-万能险，FCC00000164I-投连险，FCC000001ECY-普通险。

### CompoundMode (主附险)

主附险(CompoundMode) ：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到主附险的具体描述：FCC00000164E-主险，FCC00000164F-附险 。

### PlanState (产品状态)

产品状态(PlanState)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到产品状态的具体描述：FCC0000015X9-在售，FCC0000015XA-停售 。

### CurrencyCode (币种)

币种(CurrencyCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到币种的具体描述：FCC000000015-人民币元，FCC00000000B-美元，FCC00000000C-港元，FCC00000000G-日本元，FCC00000002A-欧元，FCC00000002D-英镑，FCC00000002N-瑞士法郎，FCC00000002T-加拿大元，FCC00000002U-澳大利亚元，FCC00000002V-新西兰元。

## SQL示例

```sql
-- 查询 保险理财产品概况 数据
SELECT *
FROM fp_ifbasicinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
