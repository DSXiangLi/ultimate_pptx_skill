# Bond_IndexBasicInfo

**中文名**: 债券指数概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IndexBasicInfo` |
| MySQL表名 | `bond_indexbasicinfo` |
| 中文名 | 债券指数概况 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 22 |
| 版本 | 1.01 |

## 表描述

1.收录了市场上主要债券指数的基本情况，包括指数类别、指数名称、成份证券类别、发布机构、发布日期、基期基点、成份证券调整周期等信息。
2.历史数据：2002年12月至今
3.数据源：上海交易所、深圳交易所、中信证券股份有限公司、新华富时指数有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部代码 | number(10) | ✗ | 100.0% | 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `IndexType` | 指数类别 | number(10) | ✗ | 100.0% | 指数类别(IndexType)与(CT_SystemConst)表中的DM字段关联，令LB = 1266 AND DM ... |
| 4 | `SecuCode` | 指数代码 | varchar2(30) | ✓ | 100.0% |  |
| 5 | `SecuAbbr` | 指数简称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ChiName` | 指数名称 | varchar2(200) | ✓ | 100.0% |  |
| 7 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 8 | `ComponentType` | 成份证券类别 | number(10) | ✓ | 100.0% | 成份证券类别(ComponentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1008 A... |
| 9 | `PubOrgCode` | 发布机构代码 | number(10) | ✓ | 100.0% | 发布机构代码（PubOrgCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Company... |
| 10 | `PubOrgName` | 发布机构名称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `CreatIndexOrgCode` | 编制机构代码 | number(10) | ✓ | 100.0% | 编制机构代码（CreatIndexOrgCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（... |
| 12 | `CreatIndexOrgName` | 编制机构名称 | varchar2(200) | ✓ | 100.0% |  |
| 13 | `PubDate` | 发布日期 | date | ✓ | 97.86% |  |
| 14 | `BaseDate` | 基日 | date | ✓ | 97.91% |  |
| 15 | `BasePoint` | 基点(点) | number(10) | ✓ | 97.69% |  |
| 16 | `WAMethod` | 加权方式 | number(10) | ✓ | 92.09% | 加权方式(WAMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1265，得到加权方式的具... |
| 17 | `ComponentSum` | 成份证券数量 | number(10) | ✓ | 11.69% |  |
| 18 | `ComponentAdPeriod` | 成份证券调整周期 | number(10) | ✓ | 97.16% |  |
| 19 | `IndexRemark` | 指数简介 | clob | ✓ | 54.85% |  |
| 20 | `EndDate` | 停用日期 | date | ✓ | 6.6% |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部代码)

指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### IndexType (指数类别)

指数类别(IndexType)与(CT_SystemConst)表中的DM字段关联，令LB = 1266 AND DM in (46)，得到指数类别的具体描述：46-债券类指数。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,84,89,90,71)，得到证券市场的具体描述：71-柜台交易市场，83-上海证券交易所，84-其他市场，89-银行间债券市场，90-深圳证券交易所。

### ComponentType (成份证券类别)

成份证券类别(ComponentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1008 AND (DM LIKE '15%' OR DM LIKE '17%' )，得到成份证券类别的具体描述：1500-债券，1503-国债，1506-企债，1507-公司债，1509-金融债，1512-回购，1515-可转债，1521-资产证券化产品，1522-同业存单，1700-央行公开市场业务，1703-票据。

### PubOrgCode (发布机构代码)

发布机构代码（PubOrgCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到发布机构的具体名称、基本信息等。

### CreatIndexOrgCode (编制机构代码)

编制机构代码（CreatIndexOrgCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到编制机构的具体名称、基本信息等。

### WAMethod (加权方式)

加权方式(WAMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1265，得到加权方式的具体描述：1-持仓市值加权，2-产量加权，3-自由流通市值加权，4-自由流通股本加权，5-调整自由流通股本加权，6-分档自由流通市值加权，7-调整自由流通市值加权，10-流通股加权，11-派许加权，12-预期股息率加权，13-流通股比例分级靠档加权，30-总股本加权，33-债券发行量加权，34-债券流通托管量加权，40-调整流通股本加权，41-调整流通市值加权，42-流通市值加权，43-总市值加权，44-风格评分加权法，45-基本面加权，46-等权，47-股息加权，48-市盈率加权，49-流动性加权，50-持仓量加权，51-消费量加权，52-波动率倒数加权，53-固定权重，54-波幅加权，55-贝塔系数加权，56-收益率加权，57-调整总市值加权，60-等风险加权，61-ESG评分加权，62-持股金额加权，63-成交量加权，64-消费金额加权，65-债券余额加权。

## SQL示例

```sql
-- 查询 债券指数概况 数据
SELECT *
FROM bond_indexbasicinfo
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
