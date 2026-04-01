# FX_OptionDeltaCurves

**中文名**: 外汇期权Delta参数曲线

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FX_OptionDeltaCurves` |
| MySQL表名 | `fx_optiondeltacurves` |
| 中文名 | 外汇期权Delta参数曲线 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1 |

## 表描述

1.内容说明：收录外汇中心发布的外汇期权Delta计量参数相关数据，定价数据源包括人民币无风险利率、外币无风险利率、即期利率、外汇期权隐含波动率等
2.数据范围：2020-07-07至今
3.信息来源：外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CurveCode` | 曲线代码 | number(10) | ✗ | 100.0% | 曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB=2376 AND FVALU... |
| 3 | `CurveName` | 曲线名称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `YieldTerm` | 标准期限值 | varchar2(20) | ✓ | 100.0% |  |
| 5 | `MaturityCode` | 标准期限代码 | number(10) | ✗ | 100.0% | 标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1555 AN... |
| 6 | `YieldTermDesc` | 标准期限描述 | varchar2(20) | ✓ | 100.0% |  |
| 7 | `CalDate` | 计算日期 | date | ✗ | 100.0% |  |
| 8 | `CalDays` | 计算天数 | number(13,8) | ✓ | 100.0% |  |
| 9 | `SettlDate` | 期权到期日 | date | ✓ | 100.0% |  |
| 10 | `StrikePrice` | 执行价格 | number(13,8) | ✓ | 100.0% |  |
| 11 | `Delta_CallOption` | 看涨期权delta值 | number(13,8) | ✓ | 100.0% |  |
| 12 | `Delta_PutOption` | 看跌期权delta值 | number(13,8) | ✓ | 100.0% |  |
| 13 | `ImpliedVolatility` | 隐含波动率 | number(13,8) | ✓ | 100.0% |  |
| 14 | `DC_RateSource` | 本币利率来源 | number(10) | ✓ | 100.0% | 本币利率来源(DC_RateSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2385，得... |
| 15 | `DC_RateSourceDesc` | 本币利率来源描述 | varchar2(100) | ✓ | 100.0% |  |
| 16 | `DC_Rate` | 本币利率(参考利率) | number(13,8) | ✓ | 100.0% |  |
| 17 | `FC_Rate` | 外币利率(参考利率) | number(13,8) | ✓ | 100.0% |  |
| 18 | `FC_SwapPoint` | 外汇掉期点 | number(13,8) | ✓ | 100.0% |  |
| 19 | `SpotRateSource` | 即期价格来源 | number(10) | ✓ | 100.0% | 即期价格来源(SpotRateSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2386，... |
| 20 | `SpotRateSourceDesc` | 即期价格来源描述 | varchar2(100) | ✓ | 100.0% |  |
| 21 | `SpotRate` | 即期价格 | number(13,8) | ✓ | 52.86% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (曲线代码)

曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB=2376 AND FVALUE =3，得到曲线代码的具体描述：6300000-外汇期权DELTA参数曲线(外汇掉期+中间价+Shibor)，6300001-外汇期权DELTA参数曲线(外汇掉期+即期询价报价均值+Shibor)，6300002-外汇期权DELTA参数曲线(外汇掉期+中间价+FR007)，6300003-外汇期权DELTA参数曲线(外汇掉期+即期询价报价均值+FR007)，6300004-外汇期权DELTA参数曲线(外汇掉期+中间价+Shibor3M)，6300005-外汇期权DELTA参数曲线(外汇掉期+即期询价报价均值+Shibor3M)。

### MaturityCode (标准期限代码)

标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1555 AND DM IN (5,6,7,8,9,12,13,14,15,16,17,19,20)，得到标准期限代码的具体描述：5-2W，6-3W，7-1M，8-2M，9-3M，12-6M，13-9M，14-18M，15-1Y，16-2Y，17-3Y，19-1D，20-1W。

### DC_RateSource (本币利率来源)

本币利率来源(DC_RateSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2385，得到本币利率来源的具体描述：1-本币利率+Shibor，2-本币利率+回购定盘利率/FR007利率互换收盘曲线，3-本币利率+Shibor/Shibor3M利率互换收盘曲线。

### SpotRateSource (即期价格来源)

即期价格来源(SpotRateSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2386，得到即期价格来源的具体描述：1-人民币中间价，2-即期询价均值。

## SQL示例

```sql
-- 查询 外汇期权Delta参数曲线 数据
SELECT *
FROM fx_optiondeltacurves
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
