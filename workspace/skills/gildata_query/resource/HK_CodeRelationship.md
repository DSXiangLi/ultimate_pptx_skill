# HK_CodeRelationship

**中文名**: 港股代码关联表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CodeRelationship` |
| MySQL表名 | `hk_coderelationship` |
| 中文名 | 港股代码关联表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.记录香港上市公司对应的A股公司，美国预托证券（ADR）关联代码，以及港股转板公司转板前后的代码对应信息的信息。                           2.信息来源：港交所等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CodeDefine` | 代码关联方式 | number(10) | ✗ | 100.0% | 代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 34.42% |  |
| 4 | `EffectiveDate` | 生效日期 | date | ✓ | 64.81% |  |
| 5 | `EndDate` | 终止日期 | date | ✓ | 10.54% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 7 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 8 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 9 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 10 | `RelatedInnerCode` | 关联代码内部编码 | number(10) | ✗ | 100.0% | 关联代码内部编码（RelatedInnerCode）：当代码关联方式(CodeDefine)=10时，与“证券主表（Se... |
| 11 | `RelatedCompanyCode` | 关联代码公司代码 | number(10) | ✗ | 100.0% | 关联代码公司代码（RelatedCompanyCode）：与“证券主表（SecuMain）”或者“美股证券主表（US_S... |
| 12 | `Market` | 所属市场 | number(10) | ✗ | 100.0% | 所属市场(Market)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (... |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CodeDefine (代码关联方式)

代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM IN (10,201,202,203)，得到代码关联方式的具体描述：10-跨市场公司关联，201-ADR代码对应，202-港股创业板转主板，203-双柜台交易。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1, 2)，得到是否有效的具体描述：1-是，2-否。

### InnerCode (内部代码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM = 72，得到证券市场的具体描述：72-香港联交所。

### RelatedInnerCode (关联代码内部编码)

关联代码内部编码（RelatedInnerCode）：当代码关联方式(CodeDefine)=10时，与“证券主表（SecuMain）”中的证券内部编码（InnerCode）关联；当代码关联方式(CodeDefine)=201时，与“美股证券主表（US_SecuMain）”中的“证券内部代码（InnerCode）”关联；当代码关联方式(CodeDefine) IN (202,203)时，与“港股证券主表（HK_SecuMain）”中的证券内部编码（InnerCode）关联

### RelatedCompanyCode (关联代码公司代码)

关联代码公司代码（RelatedCompanyCode）：与“证券主表（SecuMain）”或者“美股证券主表（US_SecuMain）”或者‘’港股证券主表（HK_SecuMain)‘’中的“公司代码（CompanyCode）”关联。

### Market (所属市场)

所属市场(Market)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (72,77,78,83,90,460)，得到所属市场的具体描述：72-香港联交所，77-美国纳斯达克证券交易所，78-纽约证券交易所，83-上海证券交易所，90-深圳证券交易所，460-美国OTC(OTCBB和OtherOTC)。

## SQL示例

```sql
-- 查询 港股代码关联表 数据
SELECT *
FROM hk_coderelationship
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
