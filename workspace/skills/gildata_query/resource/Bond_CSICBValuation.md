# Bond_CSICBValuation

**中文名**: 中证可交换债券估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CSICBValuation` |
| MySQL表名 | `bond_csicbvaluation` |
| 中文名 | 中证可交换债券估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中证代理数据库 > 中证估值 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：收录对可交换债券的估值数据，包括估值价格、估值收益率等。
2.数据范围：2020-06-29至今
3.信息来源：中证指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `BondForm` | 债券形式 | number(10) | ✓ | 100.0% | 债券形式(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到债券形式的具... |
| 5 | `Value` | 估值价格 | number(18,8) | ✓ | 100.0% |  |
| 6 | `YieldToMaturity` | 估值收益率(%) | number(18,8) | ✓ | 100.0% |  |
| 7 | `OptionValue` | 期权价值 | number(18,8) | ✓ | 100.0% |  |
| 8 | `ConversionPremium` | 转股溢价率(%) | number(18,8) | ✓ | 100.0% |  |
| 9 | `BondPremium` | 纯债溢价率(%) | number(18,8) | ✓ | 100.0% |  |
| 10 | `BondFloorFull` | 债底全价 | number(18,8) | ✓ | 100.0% |  |
| 11 | `BondFloorClean` | 债底净价 | number(18,8) | ✓ | 100.0% |  |
| 12 | `BondFloorYTM` | 债底收益率(%) | number(18,8) | ✓ | 100.0% |  |
| 13 | `ModifiedDuration` | 债底修正久期 | number(18,8) | ✓ | 100.0% |  |
| 14 | `Convexity` | 债底凸性 | number(18,8) | ✓ | 100.0% |  |
| 15 | `AccruedInterest` | 应计利息 | number(18,8) | ✓ | 100.0% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BondForm (债券形式)

债券形式(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到债券形式的具体描述：1-常规债券，2-分离交易可转债，3-本息分离交易债券，4-可交换公司债券。

## SQL示例

```sql
-- 查询 中证可交换债券估值 数据
SELECT *
FROM bond_csicbvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
