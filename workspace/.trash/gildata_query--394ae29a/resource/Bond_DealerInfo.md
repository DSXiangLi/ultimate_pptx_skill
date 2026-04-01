# Bond_DealerInfo

**中文名**: 交易商信息表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_DealerInfo` |
| MySQL表名 | `bond_dealerinfo` |
| 中文名 | 交易商信息表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 滚动更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.介绍上交所固定收益平台交易商、上交所三方回购投资者适当性备案信息以及深圳证券交易所交易商。
2.数据范围：2018-05-08 至今
3.信息来源：上海证券交易所、深圳证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2123，得到信息类别的具... |
| 3 | `DealerTypeCode` | 交易商类别 | number(10) | ✓ | 0.81% | 交易商类别(DealerTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2125，得... |
| 4 | `Market` | 市场 | number(10) | ✗ | 100.0% | 市场(Market)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83... |
| 5 | `DealerCode` | 交易商代码 | varchar2(10) | ✓ | 99.75% |  |
| 6 | `DealerFullName` | 交易商全称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `DealerAbbrName` | 交易商简称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `DealerCompanyCode` | 交易商企业编号 | number(10) | ✗ | 100.0% | 交易商企业编号（DealerCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号... |
| 9 | `Status` | 状态 | number(10) | ✓ | 100.0% | 状态(Status)与(CT_SystemConst)表中的DM字段关联，令LB = 2124，得到状态的具体描述：1-... |
| 10 | `InvestorName` | 投资者名称 | varchar2(200) | ✓ | 99.44% |  |
| 11 | `InvestorType` | 投资者类别代码 | number(10) | ✓ | 99.44% | 投资者类别代码(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 A... |
| 12 | `InvestorCode` | 投资者编码 | number(10) | ✓ | 5.93% | 投资者编码(InvestorCode)：当InvestorTypeCod=2时，与“机构基本资料（LC_InstiArc... |
| 13 | `Contactman` | 联系人 | varchar2(50) | ✓ | 0.28% |  |
| 14 | `Fax` | 传真 | varchar2(50) | ✓ | 0.46% |  |
| 15 | `Tel` | 联系电话 | varchar2(50) | ✓ | 0.5% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2123，得到信息类别的具体描述：1-固定收益平台交易商，2-三方回购交易商，3-债券市场交易商。

### DealerTypeCode (交易商类别)

交易商类别(DealerTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2125，得到交易商类别的具体描述：1-一级交易商，2-普通交易商，11-正回购，12-逆回购，13-正回购、逆回购。

### Market (市场)

市场(Market)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (83,90)，得到市场的具体描述：83-上海证券交易所，90-深圳证券交易所。

### DealerCompanyCode (交易商企业编号)

交易商企业编号（DealerCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### Status (状态)

状态(Status)与(CT_SystemConst)表中的DM字段关联，令LB = 2124，得到状态的具体描述：1-正常，2-S。

### InvestorType (投资者类别代码)

投资者类别代码(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM IN (2,3,99)，得到投资者类别代码的具体描述：2-企业，3-证券品种，99-其他。

### InvestorCode (投资者编码)

投资者编码(InvestorCode)：当InvestorTypeCod=2时，与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到投资者具体名称、基本信息等；当InvestorTypeCod=3时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到投资者名称交易代码、简称等。

## SQL示例

```sql
-- 查询 交易商信息表 数据
SELECT *
FROM bond_dealerinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
