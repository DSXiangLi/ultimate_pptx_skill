# Bond_AsPoCashInflow

**中文名**: 资产池现金流归集表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_AsPoCashInflow` |
| MySQL表名 | `bond_aspocashinflow` |
| 中文名 | 资产池现金流归集表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 资产支持证券信息 |
| 更新频率 | 滚动更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.本表记录资产支持证券发行说明书公布的资产池现金流归集信息，客户可用此现金流估算ABS未来还本信息，便于评估投资风险
2.资产池归集现金流是以整个项目维度
3.数据范围：2015-02-28至今，2017年12月31日之后到期的ABS项目
4.信息来源：货币网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% | 截止日期（EndDate）：为当期归集现金流的第一个计算日期 |
| 4 | `CalDate` | 计算日期 | date | ✗ | 100.0% |  |
| 5 | `CPR` | CPR值(%) | number(9,6) | ✓ | 100.0% |  |
| 6 | `BeginPrincipal` | 期初本金余额(元) | number(19,4) | ✓ | 98.31% |  |
| 7 | `BeginPriceBalance` | 期初本息余额(元) | number(19,4) | ✓ | 0.99% |  |
| 8 | `BeginPriceFee` | 期初本息费余额(元) | number(19,4) | ✓ | 0.64% |  |
| 9 | `PrincipalPer` | 本期应收本金(元) | number(19,4) | ✓ | 98.35% |  |
| 10 | `InterestPer` | 本期应收利息(元) | number(19,4) | ✓ | 98.34% |  |
| 11 | `FeePer` | 本期应收手续费(元) | number(19,4) | ✓ | 0.13% |  |
| 12 | `PricePer` | 本期应收本息额(元) | number(19,4) | ✓ | 98.59% |  |
| 13 | `PriceFeePer` | 本期预计回收金额(元) | number(19,4) | ✓ | 1.55% |  |
| 14 | `EndPrincipal` | 期末本金余额(元) | number(19,4) | ✓ | 98.33% |  |
| 15 | `EndPriceBalance` | 期末本息余额(元) | number(19,4) | ✓ | 1.02% |  |
| 16 | `EndPriceFee` | 期末本息费余额(元) | number(19,4) | ✓ | 0.65% |  |
| 17 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 AND DM... |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；对于多只债券的ABS项目，还可与“债券代码关联（Bond_CodeRelated）”中的“内部编码（InnerCode）”关联，得到此ABS项目中其他的债券（关联代码内部编码）

### EndDate (截止日期)

截止日期（EndDate）：为当期归集现金流的第一个计算日期

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 AND DM IN (200103,200204)，得到信息来源的具体描述：200103-募集说明书，200204-受托机构报告。

## SQL示例

```sql
-- 查询 资产池现金流归集表 数据
SELECT *
FROM bond_aspocashinflow
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
