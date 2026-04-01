# Fut_WRStatDaily

**中文名**: 国内商品期货仓单日报

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_WRStatDaily` |
| MySQL表名 | `fut_wrstatdaily` |
| 中文名 | 国内商品期货仓单日报 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国内商品以仓库维度和品种维度的仓单日报数据，包括仓库简称、注册仓单量、注销仓单量、升贴水和有效预报等信息。
2.数据范围：2007年至今
3.信息来源：上海期货交易所（上海国际能源中心）、大连商品期货交易所、广州期货交易所、郑州商品期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `Exchange` | 交易所 | number(10) | ✗ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 4 | `VarietyInnerCode` | 品种内部编码 | number(10) | ✗ | 100.0% | 品种内部编码(VarietyInnerCode)与期货品种(Fut_FuturesContract)的(Contract... |
| 5 | `WarehouseCode` | 仓库编号 | varchar2(100) | ✓ | 73.83% |  |
| 6 | `State` | 省份 | number(10) | ✓ | 88.85% | 省份（ProvinceCode）与国家城市代码表（LC_AreaCode）中的地区内部编码（AreaInnerCode）... |
| 7 | `WarehouseAbbr` | 仓库简称 | varchar2(100) | ✓ | 92.85% |  |
| 8 | `IndicatorCode` | 仓单统计类型 | number(10) | ✗ | 100.0% | 仓单统计类型(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2315，得... |
| 9 | `Year` | 年度 | varchar2(10) | ✓ | 0.0% |  |
| 10 | `Grade` | 等级 | varchar2(200) | ✓ | 0.0% |  |
| 11 | `Category` | 品种 | varchar2(200) | ✓ | 0.0% |  |
| 12 | `EventType` | 类别 | varchar2(200) | ✓ | 0.0% |  |
| 13 | `Brand` | 品牌 | varchar2(200) | ✓ | 0.0% |  |
| 14 | `ProducingArea` | 产地 | varchar2(200) | ✓ | 0.0% |  |
| 15 | `IfConvertedWR` | 是否折算仓单 | number(10) | ✓ | 0.0% | 是否折算仓单(IfConvertedWR)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AN... |
| 16 | `IfTransgenosis` | 是否转基因 | number(10) | ✓ | 0.0% | 是否转基因(IfTransgenosis)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AN... |
| 17 | `PreWRQ` | 昨日仓单量 | number(18,4) | ✓ | 98.68% |  |
| 18 | `WRQ` | 今日仓单量 | number(18,4) | ✓ | 98.76% |  |
| 19 | `DutiableWRQ` | 今日完税仓单量 | number(18,4) | ✓ | 3.98% |  |
| 20 | `BondedWRQ` | 今日保税仓单量 | number(18,4) | ✓ | 3.98% |  |
| 21 | `WRQChange` | 增减 | number(18,4) | ✓ | 98.76% |  |
| 22 | `WRQRegister` | 注册仓单量 | number(18,4) | ✓ | 100.0% |  |
| 23 | `WRQWriteOff` | 注销仓单量 | number(18,4) | ✓ | 100.0% |  |
| 24 | `WRQPrediction` | 有效预报 | number(18,4) | ✓ | 13.74% |  |
| 25 | `PremiumsAndDiscounts` | 升贴水(元/吨) | number(18,4) | ✓ | 27.44% |  |
| 26 | `WRUnitCode` | 仓单单位 | number(10) | ✓ | 100.0% | 仓单单位(WRUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB = 102 AND DM ... |
| 27 | `ConversionFormula` | 转换公式 | varchar2(100) | ✓ | 0.0% |  |
| 28 | `Remark` | 备注 | clob | ✓ | 38.71% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN(10,11,13,15,17)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所。

### VarietyInnerCode (品种内部编码)

品种内部编码(VarietyInnerCode)与期货品种(Fut_FuturesContract)的(ContractInnerCode)字段关联，得到该期货品种的基础信息。

### State (省份)

省份（ProvinceCode）与国家城市代码表（LC_AreaCode）中的地区内部编码（AreaInnerCode）字段关联，令是否有效（ IfEffected）=1 且令 一级区划代码（FirstLevelCode）=1000，得到省份的具体描述。

### IndicatorCode (仓单统计类型)

仓单统计类型(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2315，得到仓单统计类型的具体描述：1-按仓库统计，2-按地区统计，3-按品种统计，4-按品种保税交割统计，5-按品种完税交割统计，6-按厂库统计，7-按车船板统计。

### IfConvertedWR (是否折算仓单)

是否折算仓单(IfConvertedWR)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否折算仓单的具体描述：1-是，2-否。

### IfTransgenosis (是否转基因)

是否转基因(IfTransgenosis)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2) ，得到是否转基因的具体描述：1-是，2-否。

### WRUnitCode (仓单单位)

仓单单位(WRUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB = 102 AND DM IN (8,12,24,31,33)，得到仓单单位的具体描述：8-千克，12-吨，24-张，31-手，33-桶。

## SQL示例

```sql
-- 查询 国内商品期货仓单日报 数据
SELECT *
FROM fut_wrstatdaily
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
