# Bond_ConBDFluctuAttach

**中文名**: 可转债交易公开信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDFluctuAttach` |
| MySQL表名 | `bond_conbdfluctuattach` |
| 中文名 | 可转债交易公开信息附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1.04 |

## 表描述

内容说明：记录沪深交易所披露的可转债在交易异常波动期间证券公司交易席位的公开买卖信息。
数据范围：2022-08-01 至今
信息来源：上海证券交易所、深圳证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 与“可转债交易公开信息表(Bond_ConBDFluctuation)”表的ID字段相关联。 |
| 3 | `BSDirection` | 买卖方向 | number(10) | ✗ | 100.0% | 买卖方向(BSDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1363 AND D... |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `SalesDepartmentName` | 营业部名称 | varchar2(300) | ✓ | 100.0% |  |
| 6 | `SalesDepartmentCode` | 营业部机构代码 | number(10) | ✓ | 99.67% | 营业部机构代码(SalesDepartmentCode)：与“机构基本资料(LC_InstiArchive)”中的企业编... |
| 7 | `BelongedCompanyCode` | 营业部所属公司代码 | number(10) | ✓ | 99.67% | 营业部所属公司代码(BelongedCompanyCode)：与“机构基本资料(LC_InstiArchive)”中的企... |
| 8 | `BuySellSum` | 买卖合计金额(元) | number(19,4) | ✓ | 99.56% |  |
| 9 | `BuySum` | 买入金额(元) | number(19,4) | ✓ | 81.83% |  |
| 10 | `SellSum` | 卖出金额(元) | number(19,4) | ✓ | 82.06% |  |
| 11 | `InvestorType` | 投资者类型 | number(10) | ✓ | 0.44% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND D... |
| 12 | `AccuBuySum` | 累计买入金额(元) | number(19,4) | ✓ | 0.44% |  |
| 13 | `AccuSaleSum` | 累计卖出金额(元) | number(19,4) | ✓ | 0.44% |  |
| 14 | `BuyingRatio` | 买入占比(%) | number(19,4) | ✓ | 0.44% |  |
| 15 | `SellingRatio` | 卖出占比(%) | number(19,4) | ✓ | 0.44% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

与“可转债交易公开信息表(Bond_ConBDFluctuation)”表的ID字段相关联。

### BSDirection (买卖方向)

买卖方向(BSDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1363 AND DM IN (10,11,13)，得到买卖方向的具体描述：10-买卖金额，11-买入金额，13-卖出金额。

### SalesDepartmentCode (营业部机构代码)

营业部机构代码(SalesDepartmentCode)：与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部的具体信息。

### BelongedCompanyCode (营业部所属公司代码)

营业部所属公司代码(BelongedCompanyCode)：与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部所属公司的具体信息。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND DM IN (1,4,100,101)，得到投资者类型的具体描述：1-自然人，4-机构，100-中小投资者，101-其他自然人。

## SQL示例

```sql
-- 查询 可转债交易公开信息附表 数据
SELECT *
FROM bond_conbdfluctuattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
