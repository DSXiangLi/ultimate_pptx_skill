# MF_IndustryTagChgPos

**中文名**: 公募基金行业标签变动(基于持仓)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IndustryTagChgPos` |
| MySQL表名 | `mf_industrytagchgpos` |
| 中文名 | 公募基金行业标签变动(基于持仓) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 周更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：
本表目标：本表基于基金重仓股持仓情况进行了行业打标（FOF和ETF联接基金向下穿透至股票），真实展现基金持仓行业分布情况。
使用说明：本表有2个辅助筛选字段，标签阈值（TagThreshold）、序号（SerialNumber）。标签阈值可满足不同持仓比例阈值的筛选，序号可实现对标签个数的限定，可进行一对一打标筛选。目前行业分布的划分包含申万一、二级，中信一级。
2.数据范围：2007年10月-至今。
3.信息来源：基于基金的定报数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode)：与“行业类别表（CT_IndustryType）”的“ 行业代码(IndustryC... |
| 4 | `FundTagName` | 标签名称 | varchar2(500) | ✓ | 100.0% |  |
| 5 | `Relationship` | 关联类型 | number(10) | ✗ | 100.0% | 关联类型（Relationship): 与“行业类别表（CT_IndustryType）”中的“行业分类标准（Stand... |
| 6 | `TagThreshold` | 标签阈值 | number(18,9) | ✓ | 100.0% | 标签阈值(TagThreshold)：0.05--区间在【0.05,0.1）；0.1--区间在【0.1,0.2）；0.2... |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `Classification` | 行业级别 | number(10) | ✓ | 100.0% | 行业级别(Classification)：1-一级行业；2-二级行业。 |
| 9 | `ReportDate` | 报告期 | date | ✓ | 100.0% | 报告期(ReportDate)：标签有效的最后一个报告期。 |
| 10 | `StartDate` | 启用日期 | date | ✗ | 100.0% | 启用日期(StartDate)：标签有效时的第一个报告期。 |
| 11 | `EndDate` | 停用日期 | date | ✓ | 92.8% | 停用日期(EndDate)：标签失效的第一个报告期。 |
| 12 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)：1-是，2-否。 |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundTagCode (标签代码)

标签代码(FundTagCode)：与“行业类别表（CT_IndustryType）”的“ 行业代码(IndustryCode)”关联。

### Relationship (关联类型)

关联类型（Relationship): 与“行业类别表（CT_IndustryType）”中的“行业分类标准（Standard）”关联，得到行业分类标准的具体描述：37-中信行业2019分类，38-申万行业分类(新)。

### TagThreshold (标签阈值)

标签阈值(TagThreshold)：0.05--区间在【0.05,0.1）；0.1--区间在【0.1,0.2）；0.2--区间在【0.2,0.5）；0.5--区间在【0.5,1）。

### Classification (行业级别)

行业级别(Classification)：1-一级行业；2-二级行业。

### ReportDate (报告期)

报告期(ReportDate)：标签有效的最后一个报告期。

### StartDate (启用日期)

启用日期(StartDate)：标签有效时的第一个报告期。

### EndDate (停用日期)

停用日期(EndDate)：标签失效的第一个报告期。

### IfEffected (是否有效)

是否有效(IfEffected)：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金行业标签变动(基于持仓) 数据
SELECT *
FROM mf_industrytagchgpos
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
