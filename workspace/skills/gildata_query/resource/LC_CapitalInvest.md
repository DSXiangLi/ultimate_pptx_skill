# LC_CapitalInvest

**中文名**: 资金投向说明

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_CapitalInvest` |
| MySQL表名 | `lc_capitalinvest` |
| 中文名 | 资金投向说明 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 32 |
| 版本 | 1.03 |

## 表描述

1.公司自有资金、通过发行新股、增发新股、配股等方式所得募集资金的项目投资情况以及运用进展和改投状况。
2.数据范围：1988-12-01至今
3.信息来源：董事会公告、招股意向书、招股说明书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InitialInfoPunlDate` | 首次信息发布日期 | date | ✓ | 34.3% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 99.98% |  |
| 7 | `RaisingMethod` | 募资方式 | number(10) | ✓ | 100.0% | 募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND... |
| 8 | `InvestProject` | 募资投向项目名称 | varchar2(255) | ✓ | 100.0% |  |
| 9 | `ProjectStatement` | 项目内容 | clob | ✓ | 1.67% |  |
| 10 | `PlannedSum` | 计划投入金额(元) | number(19,4) | ✓ | 86.58% |  |
| 11 | `ActualInvestEndDate` | 实际投入截至日期 | date | ✓ | 17.32% |  |
| 12 | `ActualSum` | 实际投入金额(元) | number(19,4) | ✓ | 17.37% |  |
| 13 | `Industry` | 投向行业 | number(10) | ✓ | 0.01% | 关联行业表【CT_Industry】的行业编码[IndustryNum]，获取对应的行业信息 |
| 14 | `InvestField` | 投向领域 | number(10) | ✓ |  |  |
| 15 | `ProceedingStatement` | 进展和收益说明 | clob | ✓ | 17.45% |  |
| 16 | `IfSwitched` | 改投与否 | number(10) | ✓ | 94.19% | 改投与否(IfSwitched)与(CT_SystemConst)表中的DM字段关联，令LB = 1219，得到改投与否... |
| 17 | `ProjectSwitchedTo` | 改投项目 | varchar2(255) | ✓ | 2.98% |  |
| 18 | `SumSwitched` | 改投金额(元) | number(19,4) | ✓ | 1.76% |  |
| 19 | `PurchaseType` | 收购兼并类型 | number(10) | ✓ | 12.76% | 收购兼并类型(PurchaseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1304，得到... |
| 20 | `BookValue` | 收购资产账面价值(元) | number(19,4) | ✓ | 0.68% |  |
| 21 | `AppraisalValue` | 收购资产评估价值(元) | number(19,4) | ✓ | 1.49% |  |
| 22 | `PurchasePrice` | 收购资产价格(元) | number(19,4) | ✓ | 10.25% |  |
| 23 | `EquityRatio` | 收购权益比例(%) | number(18,6) | ✓ | 8.59% |  |
| 24 | `Transferor` | 项目出让方 | varchar2(255) | ✓ | 9.54% |  |
| 25 | `Relationship` | 与出让方关联关系 | number(10) | ✓ | 7.47% | 与出让方关联关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，... |
| 26 | `InvolvedStock` | 出让方相关股票 | number(10) | ✓ | 0.01% | 出让方相关股票（InvolvedStock）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 27 | `TransferorNature` | 出让方企业性质 | number(10) | ✓ | 0.07% | 出让方企业性质(TransferorNature)与(CT_SystemConst)表中的DM字段关联，令LB = 11... |
| 28 | `TargetName` | 收购标的名称 | varchar2(255) | ✓ | 12.65% |  |
| 29 | `TargetNature` | 收购标的企业性质 | number(10) | ✓ | 0.08% | 收购标的企业性质(TargetNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1112，... |
| 30 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 31 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### RaisingMethod (募资方式)

募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM NOT IN (13,14,19,20,21,22,31,23)，得到募资方式的具体描述：1-新股发行，2-历史遗留，3-增发新股，4-配股，5-发行可转换债券，6-发行企业债券，7-募资改投，8-非募集资金，9-发行权证，10-吸收合并，11-发行分离可转债，12-发行金融债，15-CDR首发，16-CDR增发，17-CDR配股，32-优先股发行，33-地方政府债发行，34-后续发行，99-其他。

### Industry (投向行业)

关联行业表【CT_Industry】的行业编码[IndustryNum]，获取对应的行业信息

### IfSwitched (改投与否)

改投与否(IfSwitched)与(CT_SystemConst)表中的DM字段关联，令LB = 1219，得到改投与否的具体描述：1-否，2-全部改投，3-部分改投。

### PurchaseType (收购兼并类型)

收购兼并类型(PurchaseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1304，得到收购兼并类型的具体描述：1-兼并，2-收购无形资产，3-收购实物资产，4-收购股权，5-其他收购。

### Relationship (与出让方关联关系)

与出让方关联关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与出让方关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接兄弟企业，80-间接控股股东，83-潜在控股股东，84-潜在非控股股东，86-转让前控股股东，87-转让前非控股股东，121-股权受托管理人，122-受同一方控制，999-无关联关系。

### InvolvedStock (出让方相关股票)

出让方相关股票（InvolvedStock）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到出让方相关股票的交易代码、简称等。

### TransferorNature (出让方企业性质)

出让方企业性质(TransferorNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1112，得到出让方企业性质的具体描述：1-上市公司，2-金融机构—证券信托公司，3-金融机构—银行，4-金融机构—保险公司，5-金融机构—期货公司，6-投资咨询公司，7-院校—高校，8-院校—研究院，9-院校—院校企业，10-风险与创业投资公司，11-金融机构—财务公司，12-资产管理公司，13-外资独资企业，14-中外合资企业，15-国家单位，16-国有独资，17-国有控股，18-民营企业。

### TargetNature (收购标的企业性质)

收购标的企业性质(TargetNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1112，得到收购标的企业性质的具体描述：1-上市公司，2-金融机构—证券信托公司，3-金融机构—银行，4-金融机构—保险公司，5-金融机构—期货公司，6-投资咨询公司，7-院校—高校，8-院校—研究院，9-院校—院校企业，10-风险与创业投资公司，11-金融机构—财务公司，12-资产管理公司，13-外资独资企业，14-中外合资企业，15-国家单位，16-国有独资，17-国有控股，18-民营企业。

## SQL示例

```sql
-- 查询 资金投向说明 数据
SELECT *
FROM lc_capitalinvest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
