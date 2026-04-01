# FP_IFBasicInfoAttach

**中文名**: 保险理财产品概况附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFBasicInfoAttach` |
| MySQL表名 | `fp_ifbasicinfoattach` |
| 中文名 | 保险理财产品概况附表 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

收录保险理财的销售地区、交费方式、交费期间、红利领取方式、销售渠道的结构化数据。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 74.86% |  |
| 3 | `FinProCode` | 保险产品编码 | varchar2(12) | ✗ | 100.0% | 保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `TypeCode` | 信息类别代码 | varchar2(12) | ✗ | 100.0% | 信息类别代码(TypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 5 | `EventType` | 类别 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `InvolvedCode` | 涉及代码 | varchar2(12) | ✗ | 100.0% | 涉及代码(InvolvedCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 7 | `Remark` | 备注说明 | clob | ✓ | 5.7% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (保险产品编码)

保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### TypeCode (信息类别代码)

信息类别代码(TypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到信息类别代码的具体描述：FIC000003HPY-省市地区，FIC000003HQI-保险产品交费方式，FIC000003HQJ-保险产品交费期间，FIC000003HQK-保险产品红利领取方式，FIC000003HQM-保险产品销售渠道。

### InvolvedCode (涉及代码)

涉及代码(InvolvedCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到涉及代码的具体描述：FCC0000015WE-趸交，FCC0000015WF-月交，FCC0000015WG-期交，FCC0000015WH-年交，FCC0000015WI-季交，FCC0000015WJ-半年交，FCC0000015WK-1年，FCC0000015WL-2年，FCC0000015WM-3年，FCC0000015WN-4年，FCC0000015WO-5年，FCC0000015WP-6年，FCC0000015WQ-7年，FCC0000015WR-8年，FCC0000015WS-9年，FCC0000015WT-10年，FCC000001636-12年，FCC0000015WU-15年，FCC000001893-19年，FCC0000015WV-20年，FCC0000015WW-25年，FCC0000015WX-30年，FCC0000017AH-终身，FCC0000015WY-现金领取，FCC0000015WZ-累积生息，FCC0000015X0-抵交保费，FCC0000015X1-购买交清增额保险，FCC000001635-转换年金，FCC0000015X2-银保产品，FCC0000015X3-个人营销，FCC0000015X4-团体直销，FCC0000015X5-电话销售，FCC0000015X6-中介代理，FCC0000015X7-公司直销，FCC0000015X8-网上直销，FCC0000015WB-全国，FCC0000015UG-北京，FCC0000015UH-上海，FCC0000015UI-天津，FCC0000015UT-江苏等。

## SQL示例

```sql
-- 查询 保险理财产品概况附表 数据
SELECT *
FROM fp_ifbasicinfoattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
