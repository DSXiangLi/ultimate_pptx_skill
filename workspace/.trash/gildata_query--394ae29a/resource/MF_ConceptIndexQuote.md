# MF_ConceptIndexQuote

**中文名**: 概念标签指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ConceptIndexQuote` |
| MySQL表名 | `mf_conceptindexquote` |
| 中文名 | 概念标签指数行情 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：记录A股聚源概念板块（二级、三级）的行情。概念常量参见<概念板块常量表 LC_ConceptList>(不包括新股与次新股、昨日涨停、资金龙头）。应用场景为，获取 <公募基金主题标签变动 MF_ThemeTagChange>中，基金标签所属的股票概念板块的行情表现。
2.数据范围：2016年7月起-至今。
3.信息来源：等权法加权，基点为1000点。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ConceptCode` | 概念代码 | number(10) | ✗ | 100.0% | 概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptC... |
| 3 | `ConceptName` | 概念名称 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `ConceptLevel` | 概念级别 | number(10) | ✗ | 100.0% |  |
| 5 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 6 | `ChangePCT` | 日涨跌幅(%) | number(18,6) | ✓ | 99.94% |  |
| 7 | `ClosePrice` | 收盘价(点) | number(14,4) | ✓ | 99.96% |  |
| 8 | `ChangeOF` | 日涨跌 | number(14,4) | ✓ | 99.92% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ConceptCode (概念代码)

概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。

## SQL示例

```sql
-- 查询 概念标签指数行情 数据
SELECT *
FROM mf_conceptindexquote
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
