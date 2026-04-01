# Bond_ConBDChangeAttach

**中文名**: 可转债券修正信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDChangeAttach` |
| MySQL表名 | `bond_conbdchangeattach` |
| 中文名 | 可转债券修正信息附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

内容说明：记录可转债转股价格修正条款中约束修正价格的价值指标。
数据范围：2000-03-15 至今
信息来源：上交所、深交所、巨潮资讯网等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID(RID)：与“可转债券修正信息(Bond_ConBDChangeInfo)”表的ID字段相关联。 |
| 3 | `AdjLimitType` | 修正价格限制类型 | number(10) | ✗ | 100.0% | 修正价格限制类型(AdjLimitType)与(CT_SystemConst)表中的DM字段关联，令LB=2368，得到... |
| 4 | `AdjLimitTypeSN` | 修正价格限制编号 | number(10) | ✗ | 100.0% |  |
| 5 | `AdjLimitComDirect` | 修正价格底线比较方向 | number(10) | ✓ | 32.85% | 修正价格底线比较方向(AdjLimitComDirect)与(CT_SystemConst)表中的DM字段关联，令LB=... |
| 6 | `AdjRefIndicatorSN` | 修正参考价值指标编号 | number(10) | ✗ | 100.0% |  |
| 7 | `AdjRefIndicator` | 修正参考价值指标 | number(10) | ✓ | 100.0% | 修正参考价值指标(AdjRefIndicator)与(CT_SystemConst)表中的DM字段关联，令LB=2369... |
| 8 | `AdjLimitPrice` | 修正价格限制调整值 | number(18,4) | ✓ | 0.36% |  |
| 9 | `AdjLimitRange` | 修正价格限制调整幅度(%) | number(18,4) | ✓ | 9.62% |  |
| 10 | `LimitConditionDay` | 限制时间条件天数(n) | number(10) | ✓ | 95.93% |  |
| 11 | `LimitTimeValueType` | 限制时间值类型 | number(10) | ✓ | 95.93% |  |
| 12 | `RefEvent` | 参照事件 | number(10) | ✓ | 64.63% | 参照事件(RefEvent)与(CT_SystemConst)表中的DM字段关联，令LB=2370，得到参照事件的具体描... |
| 13 | `RefDate` | 参照日期 | date | ✓ | 0.08% | 参照日期(RefDate)与(CT_SystemConst)表中的DM字段关联，令LB=2367，得到参照日期的具体描述... |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID(RID)：与“可转债券修正信息(Bond_ConBDChangeInfo)”表的ID字段相关联。

### AdjLimitType (修正价格限制类型)

修正价格限制类型(AdjLimitType)与(CT_SystemConst)表中的DM字段关联，令LB=2368，得到修正价格限制类型的具体描述：1-修正价格，2-修正后价格上限，3-修正后价格下限，4-修正后换股所需股票数量上限。

### AdjLimitComDirect (修正价格底线比较方向)

修正价格底线比较方向(AdjLimitComDirect)与(CT_SystemConst)表中的DM字段关联，令LB=1862，得到修正价格底线比较方向的具体描述：1-加，2-减，3-乘，4-除，5-max，6-min。

### AdjRefIndicator (修正参考价值指标)

修正参考价值指标(AdjRefIndicator)与(CT_SystemConst)表中的DM字段关联，令LB=2369，得到修正参考价值指标的具体描述：1-股票收盘价（均价），2-每股净资产，3-每股股票面值，4-IPO发行价(不考虑复权），5-当期转股/换股价格，6-初始转股/换股价格，7-截至参照日发行人持有股票数量，8-取得的初始成本，9-股票收盘价，10-股票加权价（均价）。

### RefEvent (参照事件)

参照事件(RefEvent)与(CT_SystemConst)表中的DM字段关联，令LB=2370，得到参照事件的具体描述：1-前n个交易日，2-前n个月，3-前n个有成交记录的交易日，4-最近n期。

### RefDate (参照日期)

参照日期(RefDate)与(CT_SystemConst)表中的DM字段关联，令LB=2367，得到参照日期的具体描述：1-决议日，2-决议生效日，3-决议公告日，4-价格修正日，5-发行日，6-修正条件触发日，7-募集说明书公告日，8-换股/转股价格自动修正的提示性公告公告日，9-换股/转股价格修正公告的公告日。

## SQL示例

```sql
-- 查询 可转债券修正信息附表 数据
SELECT *
FROM bond_conbdchangeattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
