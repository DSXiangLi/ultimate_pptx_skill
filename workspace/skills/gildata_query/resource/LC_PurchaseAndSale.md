# LC_PurchaseAndSale

**中文名**: 公司采销明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PurchaseAndSale` |
| MySQL表名 | `lc_purchaseandsale` |
| 中文名 | 公司采销明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 季度更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.收录上市公司定期报告中披露的向前5名供应商的采购情况及向前5名客户的销售情况等。
2.数据范围：2000年-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 6 | `DataType` | 数据类别 | number(10) | ✗ | 100.0% | 数据类别(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1048，得到数据类别的具... |
| 7 | `IfMerged` | 合并标志 | number(10) | ✗ | 100.0% | 合并标志(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189，得到合并标志的具... |
| 8 | `PurchaseType` | 采购类型 | number(10) | ✓ | 0.03% | 采购类型(PurchaseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1047，得到采购... |
| 9 | `TradeSum` | 金额合计(元) | number(19,4) | ✓ | 97.64% |  |
| 10 | `RatioInTotal` | 占总额比例 | number(18,8) | ✓ | 97.56% |  |
| 11 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |
| 13 | `Company` | 公司名称 | varchar2(100) | ✓ | 0.0% |  |
| 14 | `SN` | 序号 | number(10) | ✓ | 0.0% |  |
| 15 | `RatioInMainIncome` | 占主营业务收入比例 | number(18,8) | ✓ | 15.75% |  |
| 16 | `RatioInMainCost` | 占主营业务成本比例 | number(18,8) | ✓ | 15.64% |  |
| 17 | `Note` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### DataType (数据类别)

数据类别(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1048，得到数据类别的具体描述：1-前5名客户销售合计，2-前5名供应商采购合计，3-前5名客户销售明细，4-前5名供应商采购明细。

### IfMerged (合并标志)

合并标志(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189，得到合并标志的具体描述：1-合并，2-母公司，3-合并调整，4-母公司调整，5-合并修正前，6-母公司修正前，7-专项合并。

### PurchaseType (采购类型)

采购类型(PurchaseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1047，得到采购类型的具体描述：1-主要原材料，2-包装材料。

## SQL示例

```sql
-- 查询 公司采销明细 数据
SELECT *
FROM lc_purchaseandsale
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
