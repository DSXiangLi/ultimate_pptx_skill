# LC_BankIndiConst

**中文名**: 银行财务附注常量表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_BankIndiConst` |
| MySQL表名 | `lc_bankindiconst` |
| 中文名 | 银行财务附注常量表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

本表记录银行收入支出类细分指标LC_BankIncomeExpense、银行贷款类细分指标LC_BankLoan、银行资产负债规模类细分指标LC_BankAssetsLiability、银行监管类细分指标LC_BankRegulator四张表IndicatorCode字段的常量解释。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ConstantCategoryCode` | 常量类别代码 | number(10) | ✗ | 100.0% |  |
| 3 | `ConstantCategory` | 常量类别名称 | varchar2(300) | ✗ | 100.0% |  |
| 4 | `ConstantName` | 常量名称 | varchar2(300) | ✗ | 100.0% |  |
| 5 | `ConstantCode` | 常量代码 | number(10) | ✗ | 100.0% |  |
| 6 | `ParentCode` | 父节点代码 | number(10) | ✓ | 95.56% | 本字段用于描述该常量的上一层级常量的代码 |
| 7 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ParentCode (父节点代码)

本字段用于描述该常量的上一层级常量的代码

## SQL示例

```sql
-- 查询 银行财务附注常量表 数据
SELECT *
FROM lc_bankindiconst
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
