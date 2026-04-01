# HK_IndustryValuation

**中文名**: 港股行业估值指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IndustryValuation` |
| MySQL表名 | `hk_industryvaluation` |
| 中文名 | 港股行业估值指标 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

内容说明：本表记录不同行业标准下的的衍生指标，包括行业静态市盈率、滚动市盈率、市净率、股息率等指标。本表中涉及的单位“元”指“人民币元”。
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
| 6 | `StatType` | 统计类型 | number(10) | ✗ | 100.0% |  |
| 7 | `IndustryStd` | 行业分类标准 | number(10) | ✓ | 100.0% | 行业分类标准(Standard)与“系统常量表”中的DM字段关联，令LB = 1081 AND DM IN (38)，得... |
| 8 | `IndustryCode` | 行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 9 | `ListedSecuNum` | 上市证券数量(只) | number(10) | ✓ | 100.0% |  |
| 10 | `TotalMV` | 总市值(元) | number(19,2) | ✓ | 100.0% |  |
| 11 | `NegotiableMV` | 港股流通市值(元) | number(19,2) | ✓ | 100.0% |  |
| 12 | `PETTM` | 滚动市盈率 | number(19,4) | ✓ | 100.0% |  |
| 13 | `PE_LYR` | 静态市盈率(LYR) | number(19,4) | ✓ | 100.0% |  |
| 14 | `PB_LF` | 市净率(LF) | number(19,4) | ✓ | 100.0% |  |
| 15 | `DividendRatio` | 滚动股息率(%) | number(19,4) | ✓ | 85.34% |  |
| 16 | `PCF_TTM` | 滚动市现率 | number(19,4) | ✓ | 100.0% |  |
| 17 | `PCF_LYR` | 静态市现率(LYR) | number(19,4) | ✓ | 100.0% |  |
| 18 | `PSTTM` | 滚动市销率 | number(19,4) | ✓ | 99.85% |  |
| 19 | `PS_LYR` | 静态市销率(LYR) | number(19,4) | ✓ | 99.87% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndustryStd (行业分类标准)

行业分类标准(Standard)与“系统常量表”中的DM字段关联，令LB = 1081 AND DM IN (38)，得到行业分类标准的具体描述：38-申万行业分类(新)。

## SQL示例

```sql
-- 查询 港股行业估值指标 数据
SELECT *
FROM hk_industryvaluation
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
