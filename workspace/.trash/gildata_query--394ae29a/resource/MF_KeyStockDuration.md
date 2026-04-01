# MF_KeyStockDuration

**中文名**: 公募基金重仓股持续期数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_KeyStockDuration` |
| MySQL表名 | `mf_keystockduration` |
| 中文名 | 公募基金重仓股持续期数 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：记录基金季报公布重仓股票的连续持有期数。用于反映基金连续重仓持股的情况。可用于平台基金重仓连续持股的展示，以及基金投资稳定性的评估。
2.数据范围：1998年6月起-至今。
3.信息来源：根据基金公司披露的定期报告计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `StockInnerCode` | 股票内部代码 | number(10) | ✗ | 100.0% | 	 股票内部代码（StockInnerCode）: 当StockInnerCode<1000000时，与“证券主表（Se... |
| 5 | `StockDuration` | 持仓股票持续期 | number(10) | ✓ | 100.0% |  |
| 6 | `RatioInNVChange` | 占资产净值比例较上期变动 | number(18,4) | ✓ | 51.67% |  |
| 7 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### StockInnerCode (股票内部代码)

	
股票内部代码（StockInnerCode）: 当StockInnerCode<1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等；当StockInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金重仓股持续期数 数据
SELECT *
FROM mf_keystockduration
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
