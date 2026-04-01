# LC_STIBCSRights

**中文名**: 科创板公司普通股股权结构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCSRights` |
| MySQL表名 | `lc_stibcsrights` |
| 中文名 | 科创板公司普通股股权结构 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1、内容说明：收录科创板上市公司各类普通股的投票权、转换权的分类及描述
2、数据范围：科创板上市至今
3、信息来源：招股说明书、上市公告书、临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `ShareType` | 股份类别 | number(10) | ✗ | 100.0% | 股份类别(ShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1024 and DM ... |
| 7 | `VotingRights` | 投票权(每股/票) | number(10) | ✓ | 100.0% |  |
| 8 | `VotingRightsDesc` | 投票权描述 | varchar2(2000) | ✓ | 100.0% |  |
| 9 | `ConversionRights` | 转换权 | number(10) | ✓ | 100.0% | 转换权(ConversionRights)与(CT_SystemConst)表中的DM字段关联，令LB = 998，得到... |
| 10 | `ConversionRightsDesc` | 转换权描述 | varchar2(2000) | ✓ | 16.67% |  |
| 11 | `CancelDate` | 取消日期 | date | ✓ | 9.52% |  |
| 12 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 13 | `SpecialRightsRemark` | 特殊股权说明 | varchar2(2000) | ✓ | 26.19% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取“上市板块(ListedSector)”=7-科创板，得到科创板上市公司的交易代码、简称等。

### ShareType (股份类别)

股份类别(ShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1024 and DM in (51,52,53,54)，得到股份类别的具体描述：51-A类普通股，52-B类普通股，53-C类普通股，54-D类普通股。

### ConversionRights (转换权)

转换权(ConversionRights)与(CT_SystemConst)表中的DM字段关联，令LB = 998，得到转换权的具体描述：1-有，2-无。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 科创板公司普通股股权结构 数据
SELECT *
FROM lc_stibcsrights
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
