# MF_ReturnOutliersJY

**中文名**: 公募基金日收益率极值表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ReturnOutliersJY` |
| MySQL表名 | `mf_returnoutliersjy` |
| 中文名 | 公募基金日收益率极值表 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录公募基金的日收益率的相关极值阈值情况，已做转型拼接处理。作为公募基金收益率排名(去极值) MF_FundReturnRankDeExt的中间算法表，根据基金自身纵向时间序列和同类横向数据，同时进行判定，若判定当日日收益率为异常值，则剔除该日日收益率值的涨跌影响。
2.数据范围：1998年3月起-至今。
3.信息来源：基金收益率根据基金公司披露的净值、分红、拆分折算数据复权后计算而得，其中货币型基金的收益率根据基金公司披露的万份收益、7日年化收益率数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode): 与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述... |
| 5 | `DailyReturn` | 日收益 | number(18,9) | ✓ | 99.9% |  |
| 6 | `ReturnTypeAvg` | 日收益同类均值 | number(18,9) | ✓ | 100.0% |  |
| 7 | `ReturnTypeStd` | 日收益同类标准差 | number(18,9) | ✓ | 100.0% |  |
| 8 | `PeerUpperLimit` | 横截面阈值上限 | number(18,9) | ✓ | 100.0% |  |
| 9 | `PeerLowerLimit` | 横截面阈值下限 | number(18,9) | ✓ | 100.0% |  |
| 10 | `ReturnAvg` | 近三月基金日收益均值 | number(18,9) | ✓ | 95.97% |  |
| 11 | `ReturnStd` | 近三月基金日收益标准差 | number(18,9) | ✓ | 95.97% |  |
| 12 | `FundUpperLimit` | 纵向阈值上限 | number(18,9) | ✓ | 95.97% |  |
| 13 | `FundLowerLimit` | 纵向阈值下限 | number(18,9) | ✓ | 95.97% |  |
| 14 | `Leverage` | 杠杆因子 | number(10,4) | ✗ | 100.0% | 杠杆因子(Leverage)：针对分级基金设定，若为进取份额分级杠杆子基金，考虑杠杆带来的倍数影响。 |
| 15 | `IfOutlier` | 是否极值 | number(10) | ✗ | 100.0% | 是否极值(IfOutlier)：1-是；2-否 |
| 16 | `DailyReturnNew` | 日收益率新 | number(18,9) | ✓ | 99.9% | 日收益率新(DailyReturnNew)：若判定当日为异常值，DailyReturnNew重新赋值为0. |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode): 与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述。

### Leverage (杠杆因子)

杠杆因子(Leverage)：针对分级基金设定，若为进取份额分级杠杆子基金，考虑杠杆带来的倍数影响。

### IfOutlier (是否极值)

是否极值(IfOutlier)：1-是；2-否

### DailyReturnNew (日收益率新)

日收益率新(DailyReturnNew)：若判定当日为异常值，DailyReturnNew重新赋值为0.

## SQL示例

```sql
-- 查询 公募基金日收益率极值表 数据
SELECT *
FROM mf_returnoutliersjy
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
