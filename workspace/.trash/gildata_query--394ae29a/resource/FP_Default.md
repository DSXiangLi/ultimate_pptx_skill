# FP_Default

**中文名**: 金融产品违约信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_Default` |
| MySQL表名 | `fp_default` |
| 中文名 | 金融产品违约信息 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 37 |
| 版本 | 1.07 |

## 表描述

1.内容说明：本表收录金融产品的违约情况，包括信息披露情况，涉及产品，违约情况、处置情况等
2.数据范围：2018年及以后
3.信息来源：来自公开信息，包括各类新闻、公告、微信公众号等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `SourceTable` | 来源表单 | varchar2(50) | ✓ | 42.66% | 来源表单(SourceTable)：记录信息来源的公告表单，当前有PS_NewsMain和FP_NotTextAnnou... |
| 2 | `RID` | RID | number(19) | ✓ | 46.52% | RID(RID)：当来源表单(SourceTable)='PS_NewsMain'时，RID可关联PS_NewsMain... |
| 3 | `ID` | ID | number(19) | ✗ |  |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `DisclosureMethod` | 披露方式 | varchar2(200) | ✓ | 96.52% |  |
| 6 | `DisclosurePlatform` | 披露平台 | varchar2(50) | ✓ | 96.41% |  |
| 7 | `InfoTitle` | 信息标题 | varchar2(200) | ✓ | 93.85% |  |
| 8 | `Weblink` | 地址链接 | varchar2(500) | ✓ | 90.42% |  |
| 9 | `OtherInfoSource` | 其他披露来源 | varchar2(200) | ✓ | 1.74% |  |
| 10 | `FinProCode` | 金融产品编码 | varchar2(12) | ✓ | 90.97% | 与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。 |
| 11 | `ChiName` | 产品中文名称 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `EnterpriseCode` | 发行机构编码 | varchar2(12) | ✓ | 100.0% | 与“ 企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体... |
| 13 | `FinancingScale` | 融资规模(亿元) | number(19,10) | ✓ | 54.52% |  |
| 14 | `InvestScope` | 投资领域 | varchar2(12) | ✓ | 74.37% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资领域的具体描述：F... |
| 15 | `ProjectSite` | 项目所在地区 | varchar2(100) | ✓ | 47.66% |  |
| 16 | `EstablishmentDate` | 产品成立日 | date | ✓ | 68.55% |  |
| 17 | `InvestTermUnit` | 投资期限单位 | varchar2(12) | ✓ | 78.94% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资期限单位的具体描述... |
| 18 | `InvestTerm` | 投资期限 | number(19,8) | ✓ | 78.94% |  |
| 19 | `MaturityDate` | 产品到期日 | date | ✓ | 73.67% |  |
| 20 | `RelatedProducts` | 关联产品 | varchar2(500) | ✓ | 4.35% |  |
| 21 | `Counterparty` | 融资主体 | varchar2(500) | ✓ | 84.44% |  |
| 22 | `Guarantor` | 保证人 | varchar2(500) | ✓ | 39.23% |  |
| 23 | `DefaultDate` | 违约日期 | date | ✓ | 87.81% |  |
| 24 | `DefaultAmount` | 违约金额(亿元) | number(19,10) | ✓ | 20.02% |  |
| 25 | `DefaultType` | 违约种类 | varchar2(12) | ✓ | 53.65% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到违约种类的具体描述：F... |
| 26 | `DefaultProg` | 违约进度 | varchar2(12) | ✓ | 91.08% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到违约进度的具体描述：F... |
| 27 | `DeReason` | 违约原因 | varchar2(500) | ✓ | 79.98% |  |
| 28 | `DeResp` | 违约责任 | varchar2(500) | ✓ | 33.24% |  |
| 29 | `RepayProg` | 偿还进度 | varchar2(12) | ✓ | 14.31% | 偿还进度(RepayProg)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 30 | `SettlementMethod` | 处置方式 | varchar2(200) | ✓ | 91.08% |  |
| 31 | `NewestAdvance` | 处置进展 | varchar2(1000) | ✓ | 89.72% |  |
| 32 | `SettlementResult` | 处理结果 | varchar2(500) | ✓ | 9.85% |  |
| 33 | `Remark` | 备注 | varchar2(1000) | ✓ | 18.34% |  |
| 34 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 35 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 36 | `JSID` | JSID | number(19) | ✗ |  |  |
| 37 | `SettlementPlan` | 处置方案 | varchar2(1000) | ✓ | 2.5% |  |

## 字段说明

### SourceTable (来源表单)

来源表单(SourceTable)：记录信息来源的公告表单，当前有PS_NewsMain和FP_NotTextAnnouncement。

### RID (RID)

RID(RID)：当来源表单(SourceTable)='PS_NewsMain'时，RID可关联PS_NewsMain表单的ID；当来源表单(SourceTable)='FP_NotTextAnnouncement'时，RID可关联FP_NotTextAnnouncement表单的ID。

### FinProCode (金融产品编码)

与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### EnterpriseCode (发行机构编码)

与“ 企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体名称、基本信息等。

### InvestScope (投资领域)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资领域的具体描述：FCC000000411-房地产，FCC000000412-金融，FCC000000413-基础设施，FCC000000414-工商企业，FBT000000036-其他。

### InvestTermUnit (投资期限单位)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资期限单位的具体描述：FCC0000001S7-年，FCC0000001S8-月，FCC0000001S9-日，FCC0000001TC-周。

### DefaultType (违约种类)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到违约种类的具体描述：FCC0000015DF-本金违约，FCC0000015DG-利息违约，FCC0000015DH-本金和利息违约。

### DefaultProg (违约进度)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到违约进度的具体描述：FCC0000015DI-提前兑付，FCC0000015DJ-展期，FCC0000015DK-延期兑付，FCC0000015DL-预计违约，FCC0000015DM-违约仲裁，FCC0000015DN-违约诉讼。

### RepayProg (偿还进度)

偿还进度(RepayProg)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到偿还进度的具体描述：FCC000001I2P-未偿还，FCC000001I2Q-部分偿还，FCC000001I2R-全部偿还。

## SQL示例

```sql
-- 查询 金融产品违约信息 数据
SELECT *
FROM fp_default
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
