# ED_InsurerCoOperations

**中文名**: 保险公司经营数据

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `ED_InsurerCoOperations` |
| MySQL表名 | `ed_insurercooperations` |
| 中文名 | 保险公司经营数据 |
| 路径 | 聚源新版数据库 > 机构数据库 > 保险公司 |
| 更新频率 | 月更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

1.收录中国保险业务情况，包括财产险、人身险的保费收入、赔款给付、营业费用的累计金额及其银行存款、投资、资产的期末金额等
2.数据范围：1999年1月-至今
3.数据源：中国保监会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `Sources` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `PremiumRevenue` | ▲保费收入(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `PropertyInsuranceIncome` | 1．财产险(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `LifeInsuranceIncome` | 2．人身险(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `AccidentInsuranceIncome` | 1)人身意外伤害(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `HealthInsuranceIncome` | 2)健康险(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `LongevityInsuranceIncome` | 3)寿险(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `Indemnity` | ▲赔款、给付(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `PropertyInsurancePayout` | 1．财产险(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `LifeInsurancePayout` | 2．人身险(元) | number(19,4) | ✓ | 100.0% |  |
| 13 | `AccidentInsurancePayout` | 1)人身意外伤害(元) | number(19,4) | ✓ | 89.44% |  |
| 14 | `HealthInsurancePayout` | 2)健康险(元) | number(19,4) | ✓ | 89.44% |  |
| 15 | `LongevityInsurancePayout` | 3)寿险(元) | number(19,4) | ✓ | 89.44% |  |
| 16 | `OperatingFees` | ▲营业费用(元) | number(19,4) | ✓ | 89.44% |  |
| 17 | `BankDeposits` | 银行存款(元) | number(19,4) | ✓ | 93.17% |  |
| 18 | `Investment` | 投资(元) | number(19,4) | ✓ | 91.93% |  |
| 19 | `TreasuryBond` | 其中：国债(元) | number(19,4) | ✓ | 44.72% |  |
| 20 | `MutualFunds` | 其中：证券投资基金(元) | number(19,4) | ✓ | 41.3% |  |
| 21 | `TotalAssets` | 资产总额(元) | number(19,4) | ✓ | 96.27% |  |
| 22 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 保险公司经营数据 数据
SELECT *
FROM ed_insurercooperations
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
