# FP_ChargeRate

**中文名**: 金融产品费率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_ChargeRate` |
| MySQL表名 | `fp_chargerate` |
| 中文名 | 金融产品费率 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录金融产品（银行理财、信托计划、券商资管、保险资管、养老金产品）的相关费率数据及执行情况，包括认购费、申购费、赎回费、管理费、托管费等详细费用。
2.信息来源：银行、信托、证券、资产管理公司、保险公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 82.84% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `ChargeRateType` | 费率类别 | varchar2(12) | ✗ | 100.0% | 费率类别（ChargeRateType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 7 | `ExcuteDate` | 执行日期 | date | ✗ | 100.0% |  |
| 8 | `CancelDate` | 取消日期 | date | ✓ | 99.62% |  |
| 9 | `IfEffected` | 是否有效 | varchar2(12) | ✓ | 100.0% | 是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 10 | `AppliObject` | 适用对象 | varchar2(12) | ✗ | 100.0% | 适用对象（AppliObject）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode... |
| 11 | `ChargeRateInterval` | 费率区间划分 | varchar2(12) | ✓ | 100.0% | 费率区间划分（ChargeRateInterval）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代... |
| 12 | `ChargeRateIntervalBe` | 费率区间起始 | number(19,4) | ✓ | 16.9% |  |
| 13 | `ChargeRateIntervalEd` | 费率区间截止 | number(19,4) | ✓ | 3.1% |  |
| 14 | `IfApplyBegin` | 是否包含费率区间起始 | varchar2(12) | ✓ | 16.9% | 是否包含费率区间起始（IfApplyBegin）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（... |
| 15 | `IfApplyEnd` | 是否包含费率区间截止 | varchar2(12) | ✓ | 3.1% | 是否包含费率区间截止（IfApplyEnd）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 16 | `IntervalUnit` | 费率区间单位 | varchar2(12) | ✓ | 18.29% | 费率区间单位（IntervalUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 17 | `ChargeRate` | 费率值 | number(19,6) | ✓ | 96.58% | 费率值（ChargeRate）：指费率的明细值。若费率是区间值，维护较高的数值；若费率表述是“不高于X”，维护X；若费率... |
| 18 | `ChargeRateUnit` | 费率单位 | varchar2(12) | ✓ | 100.0% | 费率单位（ChargeRateUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 19 | `ChargeRateDesc` | 费率描述 | varchar2(1000) | ✓ | 83.69% |  |
| 20 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### ChargeRateType (费率类别)

费率类别（ChargeRateType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到费率类别的具体描述：FCC0000001RU-管理费，FCC0000001RV-托管费，FCC0000001S1-销售服务费，FCC0000001RX-业绩报酬，FCC0000001RY-认购费（推广期），FCC0000001RZ-申购费（存续期），FCC0000001S0-赎回费，FCC000001EF6-投资顾问费，FCC000001EFR-强制赎回费，FCC000001EFS-提前赎回费，FBT000000036-其他。

### IfEffected (是否有效)

是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：FCC000000005-是，FCC000000006-否。

### AppliObject (适用对象)

适用对象（AppliObject）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到适用对象的具体描述：FCC0000001D4-个人，FCC0000001S2-机构，FCC0000001S3-全部，FCC0000001S4-VIP，FCC0000001S5-高净值客户，FCC0000001S6-企业年金基金，FCC0000002PR-普通公司，FCC0000002PS-同业机构。

### ChargeRateInterval (费率区间划分)

费率区间划分（ChargeRateInterval）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到费率区间划分的具体描述：FCC0000001SF-单一费率，FCC0000001SH-按申购金额划分，FCC000001EGT-按赎回金额划分，FCC0000001SJ-按持有期限划分，FCC0000001SL-按基金资产净值划分，FCC0000001SO-按单位净值增长率划分，FCC0000001SQ-按累计净值增长率划分，FCC000001EGS-按单位净值大小划分，FCC0000001SP-按累计净值大小划分，FCC0000001SR-按运作期年化收益率划分，FBT000000036-其他。

### IfApplyBegin (是否包含费率区间起始)

是否包含费率区间起始（IfApplyBegin）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否包含费率区间起始的具体描述：FCC000000005-是，FCC000000006-否。

### IfApplyEnd (是否包含费率区间截止)

是否包含费率区间截止（IfApplyEnd）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否包含费率区间截止的具体描述：FCC000000005-是，FCC000000006-否。

### IntervalUnit (费率区间单位)

费率区间单位（IntervalUnit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到费率区间单位的具体描述：FCC00000006T-元，FCC00000006V-万元，FCC00000006Y-亿元，FCC00000000B-美元，FCC00000000C-港元，FCC00000006Z-%，FCC000000070-个，FCC0000001CM-万份，FCC0000001S7-年，FCC0000001S8-月，FCC0000001S9-日，FCC0000001SA-亿美元，FCC0000001SB-次，FCC0000001SC-万美元，FCC0000001SD-万港元。

### ChargeRate (费率值)

费率值（ChargeRate）：指费率的明细值。若费率是区间值，维护较高的数值；若费率表述是“不高于X”，维护X；若费率表述是“不低于X”，置空。

## SQL示例

```sql
-- 查询 金融产品费率 数据
SELECT *
FROM fp_chargerate
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
