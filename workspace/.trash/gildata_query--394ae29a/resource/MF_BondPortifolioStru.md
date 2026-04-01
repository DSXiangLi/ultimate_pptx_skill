# MF_BondPortifolioStru

**中文名**: 公募基金债券组合结构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BondPortifolioStru` |
| MySQL表名 | `mf_bondportifoliostru` |
| 中文名 | 公募基金债券组合结构 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 不定时 |
| 字段数量 | 12 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金债券组合结构信息，包括国债、金融债、企业债、可转债、央行票据等各类券种占债券总体的比重。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的上市交易公告书、定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `BondType` | 债券类型 | varchar2(50) | ✗ | 100.0% | 债券类型（BondType）：包括国债、金融债券、企业债券、可转换债券、央行票据、同业存单、中小企业私募债、其他债券、中... |
| 7 | `MarketValue` | 市值(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `RatioInNV` | 占资产净值比例 | number(18,6) | ✓ | 100.0% |  |
| 9 | `RatioInBondPortfolio` | 占债券组合市值比例 | number(18,6) | ✓ | 99.75% |  |
| 10 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 11 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### BondType (债券类型)

债券类型（BondType）：包括国债、金融债券、企业债券、可转换债券、央行票据、同业存单、中小企业私募债、其他债券、中期票据、地方政府债券、短期融资券、政策性金融债券、公司债


## SQL示例

```sql
-- 查询 公募基金债券组合结构 数据
SELECT *
FROM mf_bondportifoliostru
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
