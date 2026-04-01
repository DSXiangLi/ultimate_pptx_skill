# MF_IndustryPortAll

**中文名**: 公募基金股票投资组合行业分类总表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IndustryPortAll` |
| MySQL表名 | `mf_industryportall` |
| 中文名 | 公募基金股票投资组合行业分类总表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.本表记录公募基金、QDII基金行业投资分布信息，包括行业的名称、代码、行业市值、该行业市值占基金净资产的比例等。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportType` | 报告类型 | number(10) | ✗ | 100.0% | 报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `InvestType` | 投资类型 | number(10) | ✗ | 100.0% | 投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型... |
| 8 | `InduStandard` | 行业分类标准 | number(10) | ✓ | 100.0% | 行业分类标准(InduStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AN... |
| 9 | `IndustryCode` | 行业代码 | number(10) | ✗ | 100.0% | 行业代码(IndustryCode)：当InduStandard in (6,17)时，与系统常量表的“代码（DM）”关... |
| 10 | `IndustryName` | 行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `MarketValue` | 持仓市值(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `RatioInNV` | 占净值比 | number(18,6) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ReportType (报告类型)

报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN(5,6,17,20,23,61,63,143)，得到报告类型的具体描述：5-年度报告，6-中期报告，17-第一季度报告，20-基金上市公告书，23-第三季度报告，61-第二季度报告，63-第四季度报告，143-月度报告。

### InvestType (投资类型)

投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-港股通投资。

### InduStandard (行业分类标准)

行业分类标准(InduStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (1,6,16,17,22,100)，得到行业分类标准的具体描述：1-CSRC行业分类，6-聚源行业分类(旧)，16-MSCI行业分类，17-聚源全球行业分类B，22-证监会行业分类2012版，100-恒生行业分类。

### IndustryCode (行业代码)

行业代码(IndustryCode)：当InduStandard in (6,17)时，与系统常量表的“代码（DM）”关联，“LB=1460”；当InduStandard=16时，与系统常量表的“代码（DM）”关联，“LB=1539”；当InduStandard=22时，与系统常量表的“代码（DM）”关联，“LB=1755”；当InduStandard=1时，和行业表(CT_Industry)中字段行业编码(IndustryNum)关联；当InduStandard=100时，和港股行业分类表(HK_IndustryCategory)的行业编码(IndustryNum)关联，限制Standard=100

## SQL示例

```sql
-- 查询 公募基金股票投资组合行业分类总表 数据
SELECT *
FROM mf_industryportall
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
