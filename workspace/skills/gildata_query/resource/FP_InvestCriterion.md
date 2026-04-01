# FP_InvestCriterion

**中文名**: 金融产品投资目标与业绩基准

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_InvestCriterion` |
| MySQL表名 | `fp_investcriterion` |
| 中文名 | 金融产品投资目标与业绩基准 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录金融产品（银行理财、信托计划、券商资管、保险资管、养老金产品）的历史业绩比较基准，基准种类，产品投资标的资产，投资比例等信息
取业绩比较基准数据，限制InvestTarget='FCC000000YDE'；取投资标的资产、投资比例，限制InvestTarget<>'FCC000000YDE'。
2.信息来源：银行、信托、证券、资产管理公司、保险公司官网披露的说明书和公告。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 74.14% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `IfExecuted` | 是否执行 | varchar2(12) | ✓ | 100.0% | 是否执行（IfExecuted）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 7 | `ExcuteDate` | 执行日期 | date | ✗ | 100.0% |  |
| 8 | `CancelDate` | 取消日期 | date | ✓ | 99.04% |  |
| 9 | `InvestTarget` | 投资标的 | varchar2(12) | ✗ | 100.0% | 投资标的(InvestTarget)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 10 | `InvestTargetName` | 投资标的原始名称 | varchar2(200) | ✓ | 56.69% |  |
| 11 | `TracedIndexCode` | 参照基准指数内部编码 | varchar2(12) | ✓ | 45.86% | 参照基准指数内部编码(TracedIndexCode)：与“证券码表总表(SecuMainAll) ”中的“聚源代码（G... |
| 12 | `MaxInvestRatio` | 投资比例上限 | number(9,6) | ✓ | 88.72% |  |
| 13 | `MinInvestRatio` | 投资比例下限 | number(9,6) | ✓ | 86.68% |  |
| 14 | `InvestRatioBenchmark` | 投资比例基准 | varchar2(12) | ✓ | 53.44% | 投资比例基准(InvestRatioBenchmark)：与“金融产品指标码表（FP_Indicator）”中的“聚源指... |
| 15 | `InvestRatioDescription` | 投资比例描述 | clob | ✓ | 79.8% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### IfExecuted (是否执行)

是否执行（IfExecuted）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否执行的具体描述：FCC000000005-是，FCC000000006-否。

### InvestTarget (投资标的)

投资标的(InvestTarget)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资标的的具体描述：FCC0000001T8-固定收益类，FCC0000001X3-现金类资产，CBS00000000K-买入返售金融资产，CFN0000002OC-回购及逆回购，FCC0000013BX-高流动性资产，FCC0000001WN-标准化债权资产，FCC0000001WL-债券，FCC0000014T8-可转债，FCC0000001WO-非标准化债权资产，CFN000000ADG-股票质押式回购，FCC000001DY1-固定收益类：其他资产，FCC0000001T9-权益类，FCC0000001WJ-股票，FCC000001DXY-优先股，FCC000000076-股权，FCC000001DY2-权益类：其他资产，FCC0000001X6-金融衍生品，FCC000000YHQ-期货，FCC000000HEP-权证，FCC00000139U-期权，FCC000001DY3-商品及金融衍生品类：其他资产，CBS000000028-其他资产，CFN0000001CB-基金，FCC0000014SB-债券基金，FCC000001DXZ-权益类基金，FCC000001DY0-商品类基金，CFN000000274-理财产品/信托计划及资产管理计划，FCC000001CN5-权益类和商品及金融衍生品类，FCC000001CN6-固定收益类和资管产品，FCC000001CN7-固定收益类和商品及金融衍生品类，FCC000000YDE-业绩比较基准。

### TracedIndexCode (参照基准指数内部编码)

参照基准指数内部编码(TracedIndexCode)：与“证券码表总表(SecuMainAll) ”中的“聚源代码（GilCode）”关联，得到参照基准指数内部编码的具体描述：SEC0000002FD-沪深300指数，SEC000000001-上海证券交易所综合指数，SEC0000001UM-一年定期存款利率(税后)，SEC0000003B9-中证100指数，SEC00000050F-中债-综合指数，SEC000000010-上海证券交易所国债指数，SEC0000006XT-年收益率等。

### InvestRatioBenchmark (投资比例基准)

投资比例基准(InvestRatioBenchmark)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资比例基准的具体描述：FCC0000001X9-金融产品净资产合计，FCC0000001XA-金融产品资产合计，FCC0000014SH-非现金类资产，FCC0000014SI-投资标的份额。

## SQL示例

```sql
-- 查询 金融产品投资目标与业绩基准 数据
SELECT *
FROM fp_investcriterion
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
