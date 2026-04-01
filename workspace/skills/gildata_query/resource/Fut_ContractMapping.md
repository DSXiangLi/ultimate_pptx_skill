# Fut_ContractMapping

**中文名**: 主力(连续)合约与月合约对应关系

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_ContractMapping` |
| MySQL表名 | `fut_contractmapping` |
| 中文名 | 主力(连续)合约与月合约对应关系 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录每个交易日各大交易所各品种主力(连续)合约与月合约的对应关系。
2.数据范围：1992年至今
3.信息来源：聚源数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoContractInnerCode` | 主力(连续)合约内部编码 | number(10) | ✗ | 100.0% | 主力(连续)合约内部编码(InfoContractInnerCode)：与(Fut_ContractMain)表中的Co... |
| 3 | `InfoContractCode` | 主力(连续)合约代码 | varchar2(10) | ✓ | 100.0% |  |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `ContractType` | 主力(连续)合约类型 | number(10) | ✓ | 100.0% | 目前只支持1-主力合约。 |
| 6 | `MapContractInnerCode` | 对应月合约内部编码 | number(10) | ✗ | 100.0% |  |
| 7 | `MapContractCode` | 对应月合约交易代码 | varchar2(10) | ✓ | 97.32% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoContractInnerCode (主力(连续)合约内部编码)

主力(连续)合约内部编码(InfoContractInnerCode)：与(Fut_ContractMain)表中的ContractInnerCode字段关联，令ContinueContType = 1，得到主力(连续)合约内部编码的具体描述。

### ContractType (主力(连续)合约类型)

目前只支持1-主力合约。

## SQL示例

```sql
-- 查询 主力(连续)合约与月合约对应关系 数据
SELECT *
FROM fut_contractmapping
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
