# LC_StockStyle

**中文名**: 股票风格属性

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_StockStyle` |
| MySQL表名 | `lc_stockstyle` |
| 中文名 | 股票风格属性 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

内容说明：本表收录股票风格属性（如价值型、成长型和平衡型）及规模属性的数据。
数据范围：2017-01-01至今
信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码(InnerCode) 与(SecuMain)表中的InnerCode字段关联，令InnerCode=Inn... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `IndicatorType` | 指标类型 | number(10) | ✗ | 100.0% | 指标类型(IndicatorType)与(CT_SystemConst)表中的DM字段关联，令LB = 2350 AND... |
| 7 | `DataValue` | 指标值 | number(10) | ✓ | 100.0% | 指标值(DataValue)与(CT_SystemConst)表中的DM字段关联，令LB = 2350 AND DM N... |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码(InnerCode)
与(SecuMain)表中的InnerCode字段关联，令InnerCode=InnerCode，得到证券内部编码的具体描述

### IndicatorType (指标类型)

指标类型(IndicatorType)与(CT_SystemConst)表中的DM字段关联，令LB = 2350 AND DM IN (1,2)，得到指标类型的具体描述：1-风格属性，2-规模属性。

### DataValue (指标值)

指标值(DataValue)与(CT_SystemConst)表中的DM字段关联，令LB = 2350 AND DM NOT IN (1,2)，得到指标值的具体描述：101-成长型，102-价值型，103-平衡型，201-大盘，202-中盘，203-小盘。

## SQL示例

```sql
-- 查询 股票风格属性 数据
SELECT *
FROM lc_stockstyle
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
