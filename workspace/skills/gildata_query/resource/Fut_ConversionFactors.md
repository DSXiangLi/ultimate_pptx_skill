# Fut_ConversionFactors

**中文名**: 期货交割转换因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_ConversionFactors` |
| MySQL表名 | `fut_conversionfactors` |
| 中文名 | 期货交割转换因子 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国债期货交易的转换因子。可查询该期货的合约信息和转换债券的相关信息。包括票面利率(%)、转换因子等指标信息。
2.数据范围：2013年至今
3.信息来源：中国金融金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `IssuanceOrg` | 发布机构 | number(10) | ✓ | 100.0% | 发布机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND D... |
| 4 | `ContractInnerCode` | 合约内部编码 | number(10) | ✓ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 5 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 6 | `IBMarketInnerCode` | 银行间债券市场内部编码 | number(10) | ✓ | 100.0% | 银行间债券市场内部编码(IBMarketInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编... |
| 7 | `SHExchangeInnerCode` | 上海证券交易所内部编码 | number(10) | ✓ | 100.0% | 上海证券交易所内部编码(SHExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内... |
| 8 | `SZExchangeInnerCode` | 深圳证券交易所内部编码 | number(10) | ✓ | 100.0% | 深圳证券交易所内部编码(SZExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内... |
| 9 | `CouponRate` | 票面利率(%) | number(19,8) | ✓ | 100.0% |  |
| 10 | `ConversionFactors` | 转换因子 | number(19,8) | ✓ | 100.0% |  |
| 11 | `XGRQ` | 修改时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IssuanceOrg (发布机构)

发布机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = 20，得到发布机构的具体描述：20-中国金融期货交易所。

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### IBMarketInnerCode (银行间债券市场内部编码)

银行间债券市场内部编码(IBMarketInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SHExchangeInnerCode (上海证券交易所内部编码)

上海证券交易所内部编码(SHExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SZExchangeInnerCode (深圳证券交易所内部编码)

深圳证券交易所内部编码(SZExchangeInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 期货交割转换因子 数据
SELECT *
FROM fut_conversionfactors
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
