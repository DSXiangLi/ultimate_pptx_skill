# MF_AdvisorShareholder

**中文名**: 公募基金管理人股东状况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AdvisorShareholder` |
| MySQL表名 | `mf_advisorshareholder` |
| 中文名 | 公募基金管理人股东状况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1.02 |

## 表描述

1.本表记录了基金管理公司披露的基金管理人股东名单、股东性质及实际持股状况等信息。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InvestAdvisorCode` | 基金管理人编号 | number(10) | ✗ | 100.0% | 基金管理人编号（InvestAdvisorCode）：与“基金管理人概况（MF_InvestAdvisorOutline... |
| 3 | `ChangeDate` | 变更日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `SerialNumber` | 股东序号 | number(10) | ✓ | 47.21% |  |
| 6 | `Name` | 股东名称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `InstitutionCode` | 机构代码 | number(10) | ✓ | 83.9% | 机构代码（InstitutionCode）：与“机构基本资料表（LC_InstiArchive）”中的“企业编号（Com... |
| 8 | `CompanyCode` | 所属上市公司代码 | number(10) | ✓ | 12.11% | 所属上市公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”... |
| 9 | `Nature` | 股东性质 | number(10) | ✓ |  | 股东性质(Nature)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到股东性质的具体描... |
| 10 | `HoldingShares` | 持股数(股/元) | number(18,4) | ✓ | 27.22% |  |
| 11 | `HoldingRatio` | 持股比例 | number(18,6) | ✓ | 100.0% |  |
| 12 | `IfExisted` | 存在与否 | number(3) | ✓ | 100.0% | 存在与否(IfExisted)，该字段固定以下常量：1-是；0-否 |
| 13 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InvestAdvisorCode (基金管理人编号)

基金管理人编号（InvestAdvisorCode）：与“基金管理人概况（MF_InvestAdvisorOutline）”中的“基金管理人编号（InvestAdvisorCode）”关联，得到基金管理人的基础信息。

### InstitutionCode (机构代码)

机构代码（InstitutionCode）：与“机构基本资料表（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到对应的机构基础信息。

### CompanyCode (所属上市公司代码)

所属上市公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属上市公司的交易代码、简称等。

### Nature (股东性质)

股东性质(Nature)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到股东性质的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，13-院校—院校企业，14-职工工会，15-财务公司，16-上市公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，40-金融机构—信用社，50-上市公司下属公司，60-中外合资企业，61-外资独资企业，64-保险投资组合，66-保险资管产品，67-股市国家队，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### IfExisted (存在与否)

存在与否(IfExisted)，该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 公募基金管理人股东状况 数据
SELECT *
FROM mf_advisorshareholder
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
