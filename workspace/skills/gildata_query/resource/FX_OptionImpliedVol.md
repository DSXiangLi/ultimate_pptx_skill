# FX_OptionImpliedVol

**中文名**: 外汇期权隐含波动率曲线

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FX_OptionImpliedVol` |
| MySQL表名 | `fx_optionimpliedvol` |
| 中文名 | 外汇期权隐含波动率曲线 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：收录外汇交易中心发布的外汇期权隐含波动率曲线，覆盖不同的波动率类型和期限，每个交易日计算5次
2.数据范围：2021-06-18至今
3.信息来源：外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingTime` | 交易时间 | varchar2(8) | ✗ | 100.0% |  |
| 4 | `CurveName` | 曲线名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `CurveCode` | 曲线代码 | number(10) | ✗ | 100.0% | 曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2376 AND FVA... |
| 6 | `CurrencyTradeName` | 货币对 | varchar2(100) | ✓ | 100.0% | 货币对(CurrencyTradeName)：展示外汇交易中心披露的原始货币对描述。2025-08-30外汇交易中心版本... |
| 7 | `CurrencyTradeCode` | 货币对代码 | number(10) | ✓ | 100.0% | 货币对代码(CurrencyTradeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 235... |
| 8 | `MaturityCode` | 标准期限代码 | number(10) | ✗ | 100.0% | 标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1555 AN... |
| 9 | `BidDirection` | 报价方向 | number(10) | ✓ | 100.0% | 报价方向(BidDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1675 AND ... |
| 10 | `ImpliedVolatility` | 隐含波动率 | number(18,10) | ✓ | 100.0% |  |
| 11 | `VolatilityTypeCode` | 波动率类型代码 | number(10) | ✓ | 100.0% | 波动率类型代码(VolatilityTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (曲线代码)

曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2376 AND FVALUE = 5，得到曲线代码的具体描述：6500001-外汇期权隐含波动率报买曲线(美元ATM)，6500002-外汇期权隐含波动率报卖曲线(美元ATM)，6500003-外汇期权隐含波动率曲线(美元ATM)，6500004-外汇期权隐含波动率报买曲线(美元25 Delta Call)，6500005-外汇期权隐含波动率报卖曲线(美元25 Delta Call)，6500006-外汇期权隐含波动率曲线(美元25 Delta Call)，6500007-外汇期权隐含波动率报买曲线(美元25 Delta Put)，6500008-外汇期权隐含波动率报卖曲线(美元25 Delta Put)，6500009-外汇期权隐含波动率曲线(美元25 Delta Put)，6500010-外汇期权隐含波动率报买曲线(美元10 Delta Call)，6500011-外汇期权隐含波动率报卖曲线(美元10 Delta Call)，6500012-外汇期权隐含波动率曲线(美元10 Delta Call)，6500013-外汇期权隐含波动率报买曲线(美元10 Delta Put)，6500014-外汇期权隐含波动率报卖曲线(美元10 Delta Put)，6500015-外汇期权隐含波动率曲线(美元10 Delta Put)，6500016-外汇期权隐含波动率报买曲线(美元25D RR)，6500017-外汇期权隐含波动率报卖曲线(美元25D RR)，6500018-外汇期权隐含波动率曲线(美元25D RR)，6500019-外汇期权隐含波动率报买曲线(美元10D RR)，6500020-外汇期权隐含波动率报卖曲线(美元10D RR)，6500021-外汇期权隐含波动率曲线(美元10D RR)，6500022-外汇期权隐含波动率报买曲线(美元25D BTF)，6500023-外汇期权隐含波动率报卖曲线(美元25D BTF)，6500024-外汇期权隐含波动率曲线(美元25D BTF)，6500025-外汇期权隐含波动率报买曲线(美元10D BTF)，6500026-外汇期权隐含波动率报卖曲线(美元10D BTF)，6500027-外汇期权隐含波动率曲线(美元10D BTF)。

### CurrencyTradeName (货币对)

货币对(CurrencyTradeName)：展示外汇交易中心披露的原始货币对描述。2025-08-30外汇交易中心版本切换后，货币对描述规则发生变化，如USD.CNY，变化为USD/CNY，即由点变化为/。

### CurrencyTradeCode (货币对代码)

货币对代码(CurrencyTradeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2351 AND DM = 1，得到货币对代码的具体描述：1-USDCNY。

### MaturityCode (标准期限代码)

标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1555 AND DM in (5,6,7,8,9,12,13,14,15,16,17,19,20)，得到标准期限代码的具体描述：5-2W，6-3W，7-1M，8-2M，9-3M，12-6M，13-9M，14-18M，15-1Y，16-2Y，17-3Y，19-1D，20-1W。

### BidDirection (报价方向)

报价方向(BidDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1675 AND DM in (1,2,3)，得到报价方向的具体描述：1-报买入，2-报卖出，3-均值。

### VolatilityTypeCode (波动率类型代码)

波动率类型代码(VolatilityTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2405，得到波动率类型代码的具体描述：1-ATM，2-10D PUT，3-10D CALL，4-25D PUT，5-25D CALL，6-25D RR，7-25D BF，8-10D RR，9-10D BF，10-ATMF。

## SQL示例

```sql
-- 查询 外汇期权隐含波动率曲线 数据
SELECT *
FROM fx_optionimpliedvol
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
