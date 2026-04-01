# FP_FCAUM

**中文名**: 金融产品管理人业务规模

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_FCAUM` |
| MySQL表名 | `fp_fcaum` |
| 中文名 | 金融产品管理人业务规模 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品主体信息 |
| 更新频率 | 半年度更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录金融产品管理人发布的业务报告中业务规模等信息。
2.信息来源：银行理财子公司官网。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EnterpriseCode` | 企业编码 | varchar2(12) | ✗ | 100.0% | 企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（Enterpr... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 4 | `QualCode` | 资格内部编码 | number(10) | ✓ | 100.0% | 资格内部编码(QualCode)与(CT_SystemConst)表中的DM字段关联，令LB=2004 AND DM I... |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 97.18% |  |
| 6 | `InfoSourceCode` | 信息来源代码 | varchar2(12) | ✗ | 100.0% | 信息来源代码（InfoSourceCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 7 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 8 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 9 | `BusinessCategory` | 业务类别 | varchar2(12) | ✗ | 100.0% | 业务类别（BusinessCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gi... |
| 10 | `ProductCategory` | 产品分类 | varchar2(12) | ✗ | 100.0% | 产品分类（ProductCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 11 | `IndiCategory` | 指标类别 | varchar2(12) | ✗ | 100.0% | 指标类别（IndiCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 12 | `DataValue` | 指标数据 | number(19,4) | ✓ | 100.0% |  |
| 13 | `Unit` | 单位 | varchar2(12) | ✓ | 100.0% | 单位（Unit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到单位... |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### EnterpriseCode (企业编码)

企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### QualCode (资格内部编码)

资格内部编码(QualCode)与(CT_SystemConst)表中的DM字段关联，令LB=2004 AND DM IN (2016,2002,2029,2022,2025,2008,2021,2004,2007,2014,2015,2013,2005,2027,2026)，得到资格内部编码的具体描述：2002-合格境外机构投资者(QFII)，2004-城市商业银行，2005-村镇银行，2007-股份制商业银行，2008-国有大型商业银行，2013-民营银行，2014-农村合作银行，2015-农村商业银行，2016-农村信用社，2021-外国及港澳台银行分行，2022-外资法人银行，2025-邮储银行，2026-政策性银行，2027-住房储蓄银行，2029-商业理财子公司。

### InfoSourceCode (信息来源代码)

信息来源代码（InfoSourceCode）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到信息来源代码的具体描述：FCC00000005E-定期报告:年度报告，FCC00000005F-定期报告:半年度报告，FCC000000YHK-定期报告:季度报告，FCC0000014SJ-定期报告:月度报告，FCC0000019BW-定期报告:周度报告，FCC000000YHL-临时报告，FCC0000002PW-成立公告，FCC000001CSB-到期清算公告，FIC0000000XS-其他公告分类。

### BusinessCategory (业务类别)

业务类别（BusinessCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到业务类别的具体描述：FCC000001E7X-当期发行，FCC000001E7Y-当期到期，FCC000001E7Z-期末存续。

### ProductCategory (产品分类)

产品分类（ProductCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到产品分类的具体描述：FCC0000001T2-公募，FCC0000001T3-私募，FCC0000001T4-封闭式净值型，FCC0000001T5-封闭式非净值型，FCC0000001T6-开放式净值型，FCC0000001T7-开放式非净值型，FCC0000001T8-固定收益类，FCC0000001T9-权益类，FCC0000001TA-商品及金融衍生品类，FCC0000001TB-混合类，FCC0000000G7-合计。

### IndiCategory (指标类别)

指标类别（IndiCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到指标类别的具体描述：FCC0000000MS-数量，FCC0000001BC-金额，FCC0000000B5-份额，FCC000001DZO-数量占比，FIC0000056B8-金额占比，FCC000001E9T-份额占比。

### Unit (单位)

单位（Unit）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到单位的具体描述：FCC00000006T-元，FCC000000070-个，FCC00000006Z-%。

## SQL示例

```sql
-- 查询 金融产品管理人业务规模 数据
SELECT *
FROM fp_fcaum
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
