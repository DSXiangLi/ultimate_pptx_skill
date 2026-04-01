# Fut_QJIndexCW

**中文名**: 千际商品指数成份及权重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_QJIndexCW` |
| MySQL表名 | `fut_qjindexcw` |
| 中文名 | 千际商品指数成份及权重 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数权重信息 |
| 更新频率 | 季更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.收录了千际投资发布的全商品系列指数的成份构成涵盖的品种，以及该品种在对应指数中的权重配置数据等信息。
2.历史数据：1995年7月至今
3.数据源：千际指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ContractInnerCode` | 品种合约内码 | number(10) | ✗ | 100.0% | 品种合约内码（ContractInnerCode）：与“期货合约（Fut_FuturesContract）”中的“合约内... |
| 4 | `ProductCode` | 成份品种代码 | number(10) | ✗ | 100.0% | 成份品种代码（ProductCode）：当品种上市交易所(ExchangeCode) in(10,13,15)时，成份品... |
| 5 | `ExchangeCode` | 品种上市交易所 | number(10) | ✗ | 100.0% | 品种上市交易所(ExchangeCode)：与“系统常量表 (CT_SystemConst)”中的DM字段关联，令LB=... |
| 6 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 7 | `ExpiryDate` | 失效日期 | date | ✓ | 100.0% |  |
| 8 | `WeightedRatio` | 权重(%) | number(18,15) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### ContractInnerCode (品种合约内码)

品种合约内码（ContractInnerCode）：与“期货合约（Fut_FuturesContract）”中的“合约内部编码（ContractInnerCode）”关联，得到构成指数成份为商品对应的上市品种合约具体描述。

### ProductCode (成份品种代码)

成份品种代码（ProductCode）：当品种上市交易所(ExchangeCode) in(10,13,15)时，成份品种代码（ProductCode）与产品表（CT_Product）”中的“产品代码（ProductCode）”关联，“产品类别(ProductCategory )=326”，得到指数成份的具体描述。

### ExchangeCode (品种上市交易所)

品种上市交易所(ExchangeCode)：与“系统常量表 (CT_SystemConst)”中的DM字段关联，令LB=201，得到交易所代码的具体描述：10-上海期货交易所，13-大连商品交易所，15-郑州商品交易所

## SQL示例

```sql
-- 查询 千际商品指数成份及权重 数据
SELECT *
FROM fut_qjindexcw
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
