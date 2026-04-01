# FP_AssetAllocation

**中文名**: 金融产品资产配置

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_AssetAllocation` |
| MySQL表名 | `fp_assetallocation` |
| 中文名 | 金融产品资产配置 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品投资组合 |
| 更新频率 | 季度更新 |
| 字段数量 | 16 |
| 版本 | 1.05 |

## 表描述

1.内容说明：本表记录金融产品（银行理财、信托计划、券商资管、保险资管、养老金产品）的大类配置情况，包括股票、债券、基金、银行存款等，本表币种单位为金融产品概况表的币种（FP_BasicInfo表单CurrencyUnit字段）。
注：产品若存在多份额情况，会多次存储，可通过限制FP_BasicInfo表单IfInitialShare='FCC000000005'，每个产品仅取一次数据。
2.信息来源：银行、信托公司、证券公司、资产管理公司、保险公司官方的定期报告等。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ReportType` | 报告类型 | varchar2(12) | ✓ | 97.94% | 报告类型(ReportType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `PenetrationType` | 穿透类型 | varchar2(12) | ✓ | 100.0% | 穿透类型（PenetrationType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 9 | `AssetTypeCode` | 资产种类 | varchar2(12) | ✗ | 100.0% | 资产种类（AssetTypeCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 10 | `AssetName` | 资产种类原始名称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `MarketValue` | 资产市值 | number(19,4) | ✓ | 62.28% |  |
| 12 | `RatioInNV` | 资产占净资产比例 | number(9,6) | ✓ | 3.76% |  |
| 13 | `RatioInTotalAsset` | 资产占总资产比例 | number(9,6) | ✓ | 86.61% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### ReportType (报告类型)

报告类型(ReportType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到信息来源代码的具体描述：FCC00000005E-定期报告:年度报告，FCC00000005F-定期报告:半年度报告，FCC000000YHK-定期报告:季度报告，FCC0000014SJ-定期报告:月度报告，FCC0000019BW-定期报告:周度报告，FCC000000YHL-临时报告，FCC0000002PW-成立公告，FCC000001CSB-到期清算公告，FIC0000000XS-其他公告分类。

### PenetrationType (穿透类型)

穿透类型（PenetrationType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到穿透类型的具体描述：FCC0000019PK-穿透前，FCC0000019PL-穿透后。

### AssetTypeCode (资产种类)

资产种类（AssetTypeCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到资产种类的具体描述：FCC0000001T9-权益类，FCC0000001WJ-股票，CFN0000002IA-股权投资，FCC000001EBU-利率债，CFN0000002WH-债券-国债，CFN0000007ZH-信用债，FCC000001EBR-地方政府债，CFN0000001H1-债券—可转债，CFN0000008TM-资产证券化，CFN0000000GP-现金及银行存款，CBS00000001J-定期存款，FCC0000001WW-同业存款，CFN000000ADH-高流动性资产，FCC0000001WP-同业存单，CFN000000AD3-货币市场基金，FCC0000001WK-基金，CFN000000808-FOF/MOM，CFN00000020A-理财资管产品，CFN000000274-理财产品/信托计划及资产管理计划，FCC0000001XA-金融产品资产合计，FCC0000001X9-金融产品净资产合计，CFN00000027A-项目收益票据，CFN0000002AX-受让债权收益权，CFN000000ADG-股票质押式回购等。

## SQL示例

```sql
-- 查询 金融产品资产配置 数据
SELECT *
FROM fp_assetallocation
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
