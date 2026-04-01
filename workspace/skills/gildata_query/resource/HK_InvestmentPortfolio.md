# HK_InvestmentPortfolio

**中文名**: 香港基金投资组合

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_InvestmentPortfolio` |
| MySQL表名 | `hk_investmentportfolio` |
| 中文名 | 香港基金投资组合 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 月更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录香港互认基金投资组合数据，包含地区数据，行业数据，币种分布，债券种类等。
2.数据范围：1998年6月起-至今。
3.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.94% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✗ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1605 and DM i... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 AND ... |
| 7 | `NV` | 基金资产净值(百万) | number(19,6) | ✓ | 95.08% |  |
| 8 | `DataType` | 数据类型 | number(10) | ✗ | 100.0% | 数据类型(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 2059，得到数据类型的具... |
| 9 | `IndustryStd` | 行业分类标准 | number(10) | ✓ | 38.39% | 行业分类标准(IndustryStd)与(CT_SystemConst)表中的DM字段关联，令LB=1081 and D... |
| 10 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 11 | `ProjectName` | 项目名称 | varchar2(200) | ✓ | 100.0% |  |
| 12 | `ItemCode` | 项目类别 | number(10) | ✓ | 81.7% | 项目类别(ItemCode)：当DataType=1，与"系统常量表"中的DM字段关联，得到项目类别的具体描述，Indu... |
| 13 | `MarketValue` | 市值 | number(19,6) | ✓ | 16.42% |  |
| 14 | `RatioInNV` | 占净值比例 | number(19,4) | ✓ | 99.99% |  |
| 15 | `PortAllocationDesc` | 组合配置描述 | varchar2(500) | ✓ | 1.33% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1605 and DM in (22,23,24,25) ，得到信息来源的具体描述：22-月度信息报告，23-季度信息报告，24-半年度信息报告，25-年度信息报告。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 AND DM in (1100,1000,1420) ，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### DataType (数据类型)

数据类型(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 2059，得到数据类型的具体描述：1-行业数据，2-地区数据，3-币种分布，4-债券种类，5-资产配置，6-久期分布。

### IndustryStd (行业分类标准)

行业分类标准(IndustryStd)与(CT_SystemConst)表中的DM字段关联，令LB=1081 and DM in (6,16,31,100)，得到行业分类标准的具体描述：6-聚源行业分类(旧)，16-MSCI行业分类，31-香港基金行业分类，100-恒生行业分类。

### ItemCode (项目类别)

项目类别(ItemCode)：当DataType=1，与"系统常量表"中的DM字段关联，得到项目类别的具体描述，IndustryStd=6时，另LB=1460；IndustryStd=16时，另LB=1539；IndustryStd=31时，另LB=2061；IndustryStd=100时，另LB=2060；
当DataType=2，与"	国家城市代码表"中的AreaInnerCode字段关联，另FirstLevelCode IN (9000, 4000)；
当DataType=3，与"系统常量表"中的DM字段关联，另LB=1548；
当DataType IN (4,5) ，与"系统常量表"中的DM字段关联，另LB=2062。

## SQL示例

```sql
-- 查询 香港基金投资组合 数据
SELECT *
FROM hk_investmentportfolio
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
