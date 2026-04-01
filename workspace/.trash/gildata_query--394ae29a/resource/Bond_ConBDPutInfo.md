# Bond_ConBDPutInfo

**中文名**: 可转债券回售信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDPutInfo` |
| MySQL表名 | `bond_conbdputinfo` |
| 中文名 | 可转债券回售信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.04 |

## 表描述

1.收录可转债回售信息，包括：回售价，及触发条件等。
2.数据范围：2002-12-13 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `DataType` | 数据类型 | number(3) | ✗ | 100.0% | 数据类型（DataType），该字段固定以下常量：1-发行时权利约定 |
| 4 | `PaymentYear` | 计息年度序列 | number(3) | ✗ | 100.0% | 计息年度序列（PaymentYear）具体指某一个计息年度。 |
| 5 | `IfUnique` | 回售价格是否唯一 | number(3) | ✓ | 100.0% | 回售价格是否唯一(IfUnique)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND D... |
| 6 | `PutPrice` | 回售价 | number(19,4) | ✓ | 99.61% |  |
| 7 | `PutType` | 回售类型 | number(3) | ✓ | 99.96% | 回售类型(PutType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到回售类型的具体... |
| 8 | `PutTypeName` | 回售类型描述 | varchar2(50) | ✓ | 99.96% |  |
| 9 | `PutStartDate` | 回售开始日期 | date | ✓ | 100.0% |  |
| 10 | `PutEndDate` | 回售结束日期 | date | ✓ | 100.0% |  |
| 11 | `PaymentYearStartDate` | 计息年度起始日 | date | ✓ | 99.77% |  |
| 12 | `PaymentYearEndDate` | 计息年度截止日 | date | ✓ | 99.77% |  |
| 13 | `PutLevel` | 回售触发比例(%) | number(9,4) | ✓ | 99.84% |  |
| 14 | `TriggerDays` | 回售条件计算天数 | number(10) | ✓ | 99.84% |  |
| 15 | `ReachDays` | 回售条件满足天数 | number(10) | ✓ | 99.84% |  |
| 16 | `IfInterest` | 是否包含应记利息 | number(3) | ✓ | 100.0% | 是否包含应记利息(IfInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 17 | `MultiLevel` | 多个触发比例筛选 | number(10) | ✓ | 100.0% | 多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到... |
| 18 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 19 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### DataType (数据类型)

数据类型（DataType），该字段固定以下常量：1-发行时权利约定

### PaymentYear (计息年度序列)

计息年度序列（PaymentYear）具体指某一个计息年度。

### IfUnique (回售价格是否唯一)

回售价格是否唯一(IfUnique)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到回售价格是否唯一的具体描述：1-是，2-否。

### PutType (回售类型)

回售类型(PutType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到回售类型的具体描述：1-随时，2-每计息年度1次，3-12月内不超过1次。

### IfInterest (是否包含应记利息)

是否包含应记利息(IfInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含应记利息的具体描述：1-是，2-否。

### MultiLevel (多个触发比例筛选)

多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到多个触发比例筛选的具体描述：1-不存在多个，2-触发比例从大到小排序-1，3-触发比例从大到小排序-2。

## SQL示例

```sql
-- 查询 可转债券回售信息 数据
SELECT *
FROM bond_conbdputinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
