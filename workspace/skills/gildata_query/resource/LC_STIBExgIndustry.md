# LC_STIBExgIndustry

**中文名**: 科创板公司行业划分

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBExgIndustry` |
| MySQL表名 | `lc_stibexgindustry` |
| 中文名 | 科创板公司行业划分 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行业板块 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1.01 |

## 表描述

收录科创板上市公司在证监会行业划分、中信行业划分、GICS行业划分、申万行业划分、中信建投、中银(BOCI)行业分类、中证指数行业分类、聚源行业划分等各种划分标准下的所属行业情况。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.97% |  |
| 5 | `Standard` | 行业划分标准 | number(10) | ✗ | 100.0% | 行业划分标准（Standard）：与“系统常量表”中的“代码（DM）”关联，令“LB=1081”，得到行业划分的具体标准... |
| 6 | `Industry` | 所属行业 | number(10) | ✗ | 100.0% | 所属行业（Industry）：当Standard=1、8、18时，与“行业表”中的“行业编码（IndustryNum）”... |
| 7 | `IfExecuted` | 是否执行 | number(10) | ✗ | 100.0% | 是否执行(IfExecuted)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 8 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 9 | `CancelDate` | 取消日期 | date | ✓ | 20.49% |  |
| 10 | `FirstIndustryCode` | 一级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 11 | `FirstIndustryName` | 一级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `SecondIndustryCode` | 二级行业代码 | varchar2(20) | ✓ | 88.56% |  |
| 13 | `SecondIndustryName` | 二级行业名称 | varchar2(100) | ✓ | 88.56% |  |
| 14 | `ThirdIndustryCode` | 三级行业代码 | varchar2(20) | ✓ | 74.01% |  |
| 15 | `ThirdIndustryName` | 三级行业名称 | varchar2(100) | ✓ | 74.01% |  |
| 16 | `FourthIndustryCode` | 四级行业代码 | varchar2(20) | ✓ | 55.55% |  |
| 17 | `FourthIndustryName` | 四级行业名称 | varchar2(100) | ✓ | 55.55% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到科创板上市公司的交易代码、简称等。

### Standard (行业划分标准)

行业划分标准（Standard）：与“系统常量表”中的“代码（DM）”关联，令“LB=1081”，得到行业划分的具体标准：1-CSRC行业分类2001版(不更新)，3-中信行业分类(不更新)，5-上交所行业分类(不更新)，6-聚源行业分类(旧)(不更新)，7-SSE-GICS行业分类(不更新)，8-聚源行业分类(不更新)，9-申万行业分类(不更新)，11-中银(BOCI)行业分类(不更新)，12-中证指数行业分类(不更新)，13-中信标普GICS行业分类(不更新)，18-证监会行业分类(中证)(不更新)，19-银华自定义行业分类(不更新)，20-国证行业分类，21-新聚源行业分类(不更新)，22-证监会行业分类2012版，23-证监会行业分类2012版(中证披露)，24-申万行业分类2014版(不更新)，28-中证指数行业分类2016版(不更新)，30-聚源行业分类2016版，32-国民经济行业分类(2017)，37-中信行业2019分类，38-申万行业分类(新)，40-中证指数行业分类(2021版)，42-AMAC行业分类，44-中国上市公司协会行业分类。

### Industry (所属行业)

所属行业（Industry）：当Standard=1、8、18时，与“行业表”中的“行业编码（IndustryNum）”关联；当Standard=3、5时，与“系统常量表”的“代码（DM）”关联，“LB=1082”；当Standard=6、13时，与“系统常量表”的“代码（DM）”关联，“LB=1460”；当Standard=7时，与“系统常量表”的“代码（DM）”关联，“LB=1294”；当Standard=9时，与“系统常量表”的“代码（DM）”关联，“LB=1465”；当Standard=24时，与“系统常量表”的“代码（DM）”关联，“LB=1804”；当Standard=19、20、30、32、37、38、40、42、44时，与“行业类别表”的“行业内部编码（IndustryNum）”关联；当Standard=11时，与“系统常量表”的“代码（DM）”关联，“LB=1477”；当Standard=12时，与“系统常量表”的“代码（DM）”关联，“LB=1478”；当Standard=21时，与“系统常量表”的“代码（DM）”关联，“LB=1753”；当Standard=22时，与“系统常量表”的“代码（DM）”关联，“LB=1755”；当Standard=23时，与“系统常量表”的“代码（DM）”关联，“LB=1755”；当Standard=28时，与“系统常量表”的“代码（DM）”关联，“LB=1984”。

### IfExecuted (是否执行)

是否执行(IfExecuted)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否执行的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 科创板公司行业划分 数据
SELECT *
FROM lc_stibexgindustry
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
