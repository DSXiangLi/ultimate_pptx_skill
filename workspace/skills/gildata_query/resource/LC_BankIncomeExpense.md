# LC_BankIncomeExpense

**中文名**: 银行收入支出类细分指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_BankIncomeExpense` |
| MySQL表名 | `lc_bankincomeexpense` |
| 中文名 | 银行收入支出类细分指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 季更新 |
| 字段数量 | 18 |
| 版本 | 1.02 |

## 表描述

1.本表记录银行利息收入及支出，手续费及佣金收入及支出，业务以及管理费等细分项。
2.数据范围：2011-12-31至今
3.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(300) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志（Mark）：1-合并调整；2-合并未调整；3-母公司调整；4-母公司未调整。 |
| 8 | `IndicatorType` | 指标类别 | number(10) | ✓ | 100.0% |  |
| 9 | `IndicatorName` | 指标名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `IndicatorCode` | 标准指标代码 | number(10) | ✓ | 100.0% | 标准指标代码(IndicatorCode)与(LC_BankIndiConst)表中的ConstantCode字段关联，... |
| 11 | `DataDimension` | 数据维度 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `DataDimensionCode` | 数据维度编码 | number(10) | ✓ | 100.0% | 数据维度编码（DataDimensionCode）固定常量：10001-本期_指标金额 |
| 13 | `DataValue` | 指标数据 | number(19,4) | ✗ | 100.0% |  |
| 14 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% |  |
| 15 | `Unit` | 指标单位 | number(10) | ✓ | 100.0% | 指标单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB = 1358，得到指标单位的具体描述：... |
| 16 | `Remark` | 备注说明 | varchar2(1000) | ✓ | 0.0% |  |
| 17 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Mark (合并调整标志)

合并调整标志（Mark）：1-合并调整；2-合并未调整；3-母公司调整；4-母公司未调整。

### IndicatorCode (标准指标代码)

标准指标代码(IndicatorCode)与(LC_BankIndiConst)表中的ConstantCode字段关联，令ConstantCategoryCode IN (11,12)，得到标准指标代码的具体描述：

### DataDimensionCode (数据维度编码)

数据维度编码（DataDimensionCode）固定常量：10001-本期_指标金额

### Unit (指标单位)

指标单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB = 1358，得到指标单位的具体描述：1-元，3-千元，4-万元，6-百万元，8-亿元。

## SQL示例

```sql
-- 查询 银行收入支出类细分指标 数据
SELECT *
FROM lc_bankincomeexpense
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
