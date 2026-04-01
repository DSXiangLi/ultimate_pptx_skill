# LC_Tax

**中文名**: 公司税项

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Tax` |
| MySQL表名 | `lc_tax` |
| 中文名 | 公司税项 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 季更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

1.收录公司所得税、增值税、营业税、城建税等税率情况。
2.数据范围：1991-12-31至今
3.信息来源：定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.88% |  |
| 6 | `VATRate` | 税率 | number(9,6) | ✓ | 35.24% |  |
| 7 | `VATNote` | 备注 | clob | ✓ | 55.91% |  |
| 8 | `SalesTaxRateCeiling` | 税率下限 | number(9,6) | ✓ | 29.53% |  |
| 9 | `SalesTaxRateFloor` | 税率上限 | number(9,6) | ✓ | 28.75% |  |
| 10 | `SalesTaxNote` | 备注 | clob | ✓ | 41.87% |  |
| 11 | `CityPlanningTaxRate` | 税率 | number(9,6) | ✓ | 58.57% |  |
| 12 | `CityPlanningTaxNote` | 备注 | clob | ✓ | 58.88% |  |
| 13 | `EducationSurTaxRate` | 税率 | number(9,6) | ✓ | 75.18% |  |
| 14 | `EducationSurTaxNote` | 备注 | clob | ✓ | 73.35% |  |
| 15 | `EnterpriseIncomeTaxRate` | 名义税率 | number(9,6) | ✓ | 2.34% |  |
| 16 | `RefundRatio` | 返还比例 | number(9,6) | ✓ | 0.89% |  |
| 17 | `ActualRate` | 实际税率 | number(9,6) | ✓ | 78.77% |  |
| 18 | `EITaxNote` | 备注 | clob | ✓ | 55.55% |  |
| 19 | `HousePropertyTaxRate` | 税率 | number(9,6) | ✓ | 5.33% |  |
| 20 | `HousePropertyTaxNote` | 备注 | clob | ✓ | 46.77% |  |
| 21 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公司税项 数据
SELECT *
FROM lc_tax
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
