# LC_IndustryValuation

**中文名**: 行业估值指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndustryValuation` |
| MySQL表名 | `lc_industryvaluation` |
| 中文名 | 行业估值指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1.01 |

## 表描述

内容说明：本表记录不同行业标准下的的衍生指标，包括行业静态市盈率、滚动市盈率、市净率、股息率等指标。
数据范围：2014-01-01至今
信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndustryNum` | 行业内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `IndustryName` | 行业名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `Classification` | 行业级别 | number(10) | ✓ | 100.0% |  |
| 5 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 6 | `StatType` | 统计类型 | number(10) | ✗ | 100.0% | 统计类型(StatType)，该字段固定以下常量：2-整体法不剔除负值 |
| 7 | `SectorCode` | 统计板块 | number(10) | ✗ | 100.0% | 统计板块(SectorCode)，该字段固定以下常量：5-沪、深及北交所市场 |
| 8 | `Standard` | 行业分类标准 | number(10) | ✓ | 100.0% | 行业分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM... |
| 9 | `IndustryCode` | 行业代码 | varchar2(20) | ✓ | 100.0% | 行业代码（IndustryCode）：当Standard=24时，与“系统常量表”的“代码（DM）”关联，“LB=180... |
| 10 | `ListedSecuNum` | 上市证券数量(只) | number(10) | ✓ | 100.0% |  |
| 11 | `TotalMV` | 总市值(元) | number(19,2) | ✓ | 100.0% |  |
| 12 | `NegotiableMV` | A股流通市值(元) | number(19,2) | ✓ | 100.0% |  |
| 13 | `FreeFloatMV` | A股自由流通市值(元) | number(19,2) | ✓ | 100.0% |  |
| 14 | `PE_TTM` | 滚动市盈率 | number(19,4) | ✓ | 100.0% |  |
| 15 | `PE_LYR` | 静态市盈率(LYR) | number(19,4) | ✓ | 100.0% |  |
| 16 | `PB_LF` | 市净率(LF) | number(19,4) | ✓ | 100.0% |  |
| 17 | `DividendRatio` | 滚动股息率(%) | number(19,4) | ✓ | 98.15% |  |
| 18 | `PCF_TTM` | 滚动市现率 | number(19,4) | ✓ | 100.0% |  |
| 19 | `PCF_LYR` | 静态市现率(LYR) | number(19,4) | ✓ | 100.0% |  |
| 20 | `PS_TTM` | 滚动市销率 | number(19,4) | ✓ | 100.0% |  |
| 21 | `PS_LYR` | 静态市销率(LYR) | number(19,4) | ✓ | 100.0% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StatType (统计类型)

统计类型(StatType)，该字段固定以下常量：2-整体法不剔除负值

### SectorCode (统计板块)

统计板块(SectorCode)，该字段固定以下常量：5-沪、深及北交所市场

### Standard (行业分类标准)

行业分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (24,41)，得到行业分类标准的具体描述：24-申万行业分类2014版，41-申万行业分类2021版。

### IndustryCode (行业代码)

行业代码（IndustryCode）：当Standard=24时，与“系统常量表”的“代码（DM）”关联，“LB=1804”，得到行业名称；当Standard=41时，与“行业类别表”的“行业代码（IndustryCode）”关联，“Standard=41”，得到行业名称

## SQL示例

```sql
-- 查询 行业估值指标 数据
SELECT *
FROM lc_industryvaluation
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
