# Bond_ConBDChangeInfo

**中文名**: 可转债券修正信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDChangeInfo` |
| MySQL表名 | `bond_conbdchangeinfo` |
| 中文名 | 可转债券修正信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.05 |

## 表描述

1.记录可转债券修正信息触发相关内容。
2.数据范围：2000-03-15 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(19) | ✗ | 100.0% |  |
| 3 | `BondCode` | 可转债券代码 | varchar2(50) | ✗ | 100.0% |  |
| 4 | `BondAbbr` | 可转债券简称 | varchar2(50) | ✗ | 100.0% |  |
| 5 | `StartDate` | 发行日期 | date | ✓ | 99.58% |  |
| 6 | `PutLevel` | 修正触发转股价比例 | number(19,8) | ✓ | 98.07% |  |
| 7 | `PutChangePro` | 修正幅度 | number(19,8) | ✓ | 1.51% |  |
| 8 | `PutStartDate` | 修正开始日期 | date | ✓ | 99.64% |  |
| 9 | `PutEndDate` | 修正结束日期 | date | ✓ | 99.64% |  |
| 10 | `PutType` | 行使权力次数 | number(3) | ✓ | 100.0% | 行使权力次数(PutType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到行使权力次... |
| 11 | `PutTypeName` | 行使权力次数名称 | varchar2(50) | ✓ | 100.0% |  |
| 12 | `PutConditionDay` | 修正条件天数 | number(10) | ✓ | 98.31% |  |
| 13 | `PutReachDay` | 修正条件满足天数 | number(10) | ✓ | 98.31% |  |
| 14 | `AdjTriggerType` | 修正触发指标 | number(10) | ✓ | 97.41% | 修正触发指标(AdjTriggerType)与(CT_SystemConst)表中的DM字段关联，令LB = 2369 ... |
| 15 | `AdjDirection` | 修正方向 | number(10) | ✓ | 100.0% | 修正方向(AdjDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 2366，得到修正... |
| 16 | `AdjMode` | 修正方式 | number(10) | ✓ | 100.0% | 修正方式(AdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2365，得到修正方式的具体... |
| 17 | `MultiLevel` | 多个触发比例筛选 | number(10) | ✓ | 100.0% | 多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到... |
| 18 | `MultiAdjMode` | 多个修正方式筛选 | number(10) | ✓ | 100.0% | 多个修正方式筛选(MultiAdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2393，... |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PutType (行使权力次数)

行使权力次数(PutType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到行使权力次数的具体描述：1-随时，2-每计息年度1次，3-12月内不超过1次。

### AdjTriggerType (修正触发指标)

修正触发指标(AdjTriggerType)与(CT_SystemConst)表中的DM字段关联，令LB = 2369 AND DM IN (1,9)，得到修正触发指标的具体描述：1-股票收盘价（均价），9-股票收盘价。

### AdjDirection (修正方向)

修正方向(AdjDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 2366，得到修正方向的具体描述：1-向下修正，2-向上修正，3-无确定方向。

### AdjMode (修正方式)

修正方式(AdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2365，得到修正方式的具体描述：1-人为修正，2-自动修正。

### MultiLevel (多个触发比例筛选)

多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到多个触发比例筛选的具体描述：1-不存在多个，2-触发比例从大到小排序-1，3-触发比例从大到小排序-2。

### MultiAdjMode (多个修正方式筛选)

多个修正方式筛选(MultiAdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2393，得到多个修正方式筛选的具体描述：1-不存在多个，2-人为修正，3-自动修正。

## SQL示例

```sql
-- 查询 可转债券修正信息 数据
SELECT *
FROM bond_conbdchangeinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
