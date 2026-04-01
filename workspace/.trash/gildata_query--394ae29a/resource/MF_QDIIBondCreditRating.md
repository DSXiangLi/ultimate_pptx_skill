# MF_QDIIBondCreditRating

**中文名**: 公募基金QDII基金债券组合信用等级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_QDIIBondCreditRating` |
| MySQL表名 | `mf_qdiibondcreditrating` |
| 中文名 | 公募基金QDII基金债券组合信用等级 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > QDII投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.本表记录QDII基金定期报告中披露的按债券信用等级分类的债券投资组合情况，市值、市值占净资产的比例。
2.历史数据：2008年9月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到Q... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 8 | `BondCreditRating` | 债券信用等级 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `RatingAgency` | 评级机构 | varchar2(50) | ✓ | 97.57% |  |
| 10 | `MarketValue` | 市值(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `RatioInNV` | 市值占资产净值比例(%) | number(10,6) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 13 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到QDII基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金QDII基金债券组合信用等级 数据
SELECT *
FROM mf_qdiibondcreditrating
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
