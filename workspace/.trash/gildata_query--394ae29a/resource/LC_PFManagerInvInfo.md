# LC_PFManagerInvInfo

**中文名**: 私募基金管理人-出资人信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PFManagerInvInfo` |
| MySQL表名 | `lc_pfmanagerinvinfo` |
| 中文名 | 私募基金管理人-出资人信息 |
| 路径 | 聚源新版数据库 > 机构数据库 > 私募基金管理人 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1、内容说明：收录中国证券投资基金业协会披露的私募基金管理人公示信息中关于出资人信息的部分；
2、数据范围：私募基金管理人；
3、信息来源：中国证券投资基金业协会。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“企业码表（EP_CompanyMain）”的“企业编码（CompanyCode）... |
| 3 | `EnterpriseCode` | 企业编码 | varchar2(12) | ✗ | 100.0% | 企业编码（EnterpriseCode）：与“企业码表（EP_CompanyMain）”的“企业编码（Enterpris... |
| 4 | `OrgNameChi` | 基金管理人全称(中文) | varchar2(300) | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 6 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 7 | `InvestorName` | 出资人名称 | varchar2(200) | ✗ | 100.0% |  |
| 8 | `InvestorCPCode` | 出资人编号 | number(10) | ✓ | 37.91% | 出资人编号（InvestorCPCode）：与“企业码表（EP_CompanyMain）”的“企业编码（CompanyC... |
| 9 | `InvestorEPCode` | 出资人编码 | varchar2(12) | ✓ | 37.91% | 出资人编码（InvestorEPCode）：与“企业码表（EP_CompanyMain）”的“企业编码（Enterpri... |
| 10 | `InvestoAttribute` | 出资人属性 | number(10) | ✓ | 100.0% | 出资人属性(InvestoAttribute)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得... |
| 11 | `CapitalRatio` | 认缴比例 | number(8,4) | ✓ | 100.0% |  |
| 12 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM in... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“企业码表（EP_CompanyMain）”的“企业编码（CompanyCode）”关联，获取企业的基本信息。

### EnterpriseCode (企业编码)

企业编码（EnterpriseCode）：与“企业码表（EP_CompanyMain）”的“企业编码（EnterpriseCode）”关联，获取企业的基本信息。

### InvestorCPCode (出资人编号)

出资人编号（InvestorCPCode）：与“企业码表（EP_CompanyMain）”的“企业编码（CompanyCode）”关联，获取企业的基本信息。

### InvestorEPCode (出资人编码)

出资人编码（InvestorEPCode）：与“企业码表（EP_CompanyMain）”的“企业编码（EnterpriseCode）”关联，获取企业的基本信息。

### InvestoAttribute (出资人属性)

出资人属性(InvestoAttribute)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到出资人属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 私募基金管理人-出资人信息 数据
SELECT *
FROM lc_pfmanagerinvinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
