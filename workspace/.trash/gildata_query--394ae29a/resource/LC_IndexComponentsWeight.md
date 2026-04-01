# LC_IndexComponentsWeight

**中文名**: 指数成份股权重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndexComponentsWeight` |
| MySQL表名 | `lc_indexcomponentsweight` |
| 中文名 | 指数成份股权重 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数权重信息 |
| 更新频率 | 日更新
月更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录了市场上主要指数成份证券的权重信息，包括中证指数有限公司每月发布的“沪深300”指数的权重数据等。中证基金指数暂不提供权重数据，展示为0。
2.该表仅收录主指数成份权重信息，不收录与主指数关系（Relationship）为“1-币种不同，2-分红规则不同，3-分红规则和币种都不同，4-税后分红”的衍生指数的信息。
3.历史数据：1970年1月至今
4.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InnerCode` | 成份股内部编码 | number(10) | ✗ | 100.0% | 成份股内部编码（InnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<InnerCode<=100... |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `Weight` | 权重(%) | number(18,6) | ✗ | 100.0% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (成份股内部编码)

成份股内部编码（InnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<InnerCode<=1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当1000000<InnerCode<=2000000时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联；当7000000<InnerCode<=10000000时，与“ 美股证券主表（US_SecuMain）”中的“证券内部编码（InnerCode）”关联；当4000000<InnerCode<=6000000 或 12000000<InnerCode<=13000000 或 25000000<InnerCode<=26000000 时，与“ 基金业协会产品公示（FM_AMACProduct）”中的“产品内部编码（InnerCode）关联

## SQL示例

```sql
-- 查询 指数成份股权重 数据
SELECT *
FROM lc_indexcomponentsweight
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
