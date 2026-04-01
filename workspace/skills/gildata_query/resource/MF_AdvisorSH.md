# MF_AdvisorSH

**中文名**: 公募基金管理人股东状况(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AdvisorSH` |
| MySQL表名 | `mf_advisorsh` |
| 中文名 | 公募基金管理人股东状况(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

1.本表记录了基金管理公司披露的基金管理人股东名单、股东性质及实际持股状况等信息。与公募基金管理人股东状况MF_AdvisorShareholder区别在于，MF_AdvisorShareholder 中 ChangeDate 记录任股东起始日期，反应管理人历次引入股东的时间和具体股东信息；MF_AdvisorSH记录 担任股东的时间区间，其中BeginDate为起始日、EndDate为结束日，反应管理人目前在任或历史上曾任股东的'具体时段'。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InvestAdvisorCode` | 基金管理人编号 | number(10) | ✗ | 100.0% | 与“基金管理人概况（MF_InvestAdvisorOutline）”中的“基金管理人编号（InvestAdvisorC... |
| 3 | `BeginDate` | 开始日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✓ | 75.62% |  |
| 5 | `SHSN` | 股东序号 | number(10) | ✓ | 68.76% |  |
| 6 | `SHName` | 股东名称 | varchar2(100) | ✗ | 100.0% |  |
| 7 | `SHKind` | 股东性质 | number(10) | ✓ |  | 股东性质(SHKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到股东性质的具体描... |
| 8 | `InstitutionCode` | 机构代码 | number(10) | ✓ | 83.9% | 与“机构基本资料表（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到对应的机构基础... |
| 9 | `CompanyCode` | 所属上市公司代码 | number(10) | ✓ | 12.11% | 与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属上市公司的交易代码、简称等。 |
| 10 | `HoldingShares` | 持股数(股/元) | number(18,4) | ✓ | 27.22% |  |
| 11 | `EquityRatio` | 持股比例 | number(18,6) | ✓ | 100.0% |  |
| 12 | `IfExisted` | 存在与否 | number(10) | ✗ | 100.0% | 存在与否(IfExisted)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN ... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |
| 16 | `PaidAmount` | 出资额(元) | number(18,4) | ✓ | 72.47% |  |
| 17 | `CurrencyCode` | 币种 | number(10) | ✓ | 73.09% |  |

## 字段说明

### InvestAdvisorCode (基金管理人编号)

与“基金管理人概况（MF_InvestAdvisorOutline）”中的“基金管理人编号（InvestAdvisorCode）”关联，得到基金管理人的基础信息。

### SHKind (股东性质)

股东性质(SHKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到股东性质的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，13-院校—院校企业，14-职工工会，15-财务公司，16-上市公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，40-金融机构—信用社，50-上市公司下属公司，60-中外合资企业，61-外资独资企业，64-保险投资组合，66-保险资管产品，67-股市国家队，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### InstitutionCode (机构代码)

与“机构基本资料表（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到对应的机构基础信息。

### CompanyCode (所属上市公司代码)

与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属上市公司的交易代码、简称等。

### IfExisted (存在与否)

存在与否(IfExisted)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到存在与否的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金管理人股东状况(新) 数据
SELECT *
FROM mf_advisorsh
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
