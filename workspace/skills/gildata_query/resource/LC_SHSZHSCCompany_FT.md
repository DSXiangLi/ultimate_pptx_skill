# LC_SHSZHSCCompany_FT

**中文名**: 沪(深)港通公司概况_繁体版

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSZHSCCompany_FT` |
| MySQL表名 | `lc_shszhsccompany_ft` |
| 中文名 | 沪(深)港通公司概况_繁体版 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：收录沪（深）港通上市公司的基础信息繁体版，包括公司名称、公司简介、注册办事处、主要营业点等信息。
2.数据范围：全部沪（深）港通上市公司。
3.信息来源：港交所等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844，得到交易类... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 4 | `CompanyName` | 公司名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `BriefIntroText` | 公司简介 | clob | ✓ | 94.06% |  |
| 6 | `Business` | 公司业务 | clob | ✓ | 94.06% |  |
| 7 | `Chairman` | 主席 | varchar2(100) | ✓ | 93.54% |  |
| 8 | `CompanySecretary` | 公司秘书 | varchar2(100) | ✓ | 93.7% |  |
| 9 | `CertifiedAccountant` | 合资格会计师 | varchar2(100) | ✓ | 5.57% |  |
| 10 | `RegisteredOffice` | 注册办事处 | varchar2(200) | ✓ | 94.06% |  |
| 11 | `GeneralOffice` | 总办事处及主要营业地点 | varchar2(200) | ✓ | 94.06% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844，得到交易类型的具体描述：1-沪股通，2-港股通（沪），3-深股通，4-港股通（深），5-港股通（沪深）。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 沪(深)港通公司概况_繁体版 数据
SELECT *
FROM lc_shszhsccompany_ft
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
