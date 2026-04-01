# Bond_AreaImportance

**中文名**: 城投区域重要性评分表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_AreaImportance` |
| MySQL表名 | `bond_areaimportance` |
| 中文名 | 城投区域重要性评分表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 城投专题信息 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.本表按城投在所属区域内的地位重要性，对城投进行分区域的打分和排序。提供最终的平台重要性标签和平台重要性评分结果。
2.年报更新或区域城投数量变化时会对区域内所有城投进行重新评分并生成一条新的计算日期记录。当选择是否有效=1时，则对每家城投仅展示最新一次打分，折叠历史打分结果。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 城投公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `CompanyName` | 城投公司名称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `AreaCode` | 所属地区代码 | number(10) | ✓ | 98.96% |  |
| 5 | `Area` | 所属地区名称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `CompanyAmount` | 区域内城投平台数量 | number(10) | ✓ | 100.0% |  |
| 7 | `AreaImptScore` | 平台重要性打分 | number(2,1) | ✓ | 100.0% |  |
| 8 | `AreaImportance` | 平台重要性 | number(10) | ✓ | 100.0% | 平台重要性(AreaImportance)与(CT_SystemConst)表中的DM字段关联，令LB = 2531，得... |
| 9 | `CalDate` | 计算日期 | date | ✗ | 100.0% |  |
| 10 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% |  |
| 11 | `ThreeYearAssetAve` | 近3年总资产均值 | number(19,6) | ✓ | 94.01% |  |
| 12 | `AssetScore` | 总资产评分 | number(2,1) | ✓ | 88.76% |  |
| 13 | `AssetTransferTotal` | 历年资本金注入与资产划拨累计值 | number(19,6) | ✓ | 91.73% |  |
| 14 | `AssetTransferThreeY` | 近3年资本金注入与资产划拨累计值 | number(19,6) | ✓ | 91.61% |  |
| 15 | `AssetTransferScore` | 资本金注入与资产划拨评分 | number(2,1) | ✓ | 86.38% |  |
| 16 | `SubsidiesTotal` | 历年政府补贴累计值 | number(19,6) | ✓ | 81.23% |  |
| 17 | `SubsidiesThreeY` | 近3年政府补贴累计值 | number(19,6) | ✓ | 72.28% |  |
| 18 | `SubsidiesScore` | 政府补贴评分 | number(2,1) | ✓ | 76.37% |  |
| 19 | `ControllerRatio` | 实控人穿透控股比例 | number(19,6) | ✓ | 97.01% |  |
| 20 | `ControllerRScore` | 实控人穿透控股比例评分 | number(2,1) | ✓ | 91.02% |  |
| 21 | `ControlLevel` | 实控人穿透层数 | number(10) | ✓ | 97.01% |  |
| 22 | `ControlLScore` | 实控人穿透层数评分 | number(2,1) | ✓ | 91.02% |  |
| 23 | `PublicBusRatioThreeY` | 近3年公益性业务收入占比 | number(19,6) | ✓ | 79.57% |  |
| 24 | `PublicBusRatioScore` | 公益性业务占比评分 | number(2,1) | ✓ | 75.28% |  |
| 25 | `BusinessType` | 城投平台业务类型 | number(10) | ✓ | 89.73% | 城投平台业务类型(BusinessType)与(CT_SystemConst)表中的DM字段关联，令LB = 2528，... |
| 26 | `BusinessTypeScore` | 城投平台业务类型评分 | number(2,1) | ✓ | 84.72% |  |
| 27 | `MainBusinessArea` | 主要业务片区 | varchar2(200) | ✓ | 72.47% |  |
| 28 | `ProprietaryScore` | 业务专营性评分 | number(2,1) | ✓ | 0.0% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AreaImportance (平台重要性)

平台重要性(AreaImportance)与(CT_SystemConst)表中的DM字段关联，令LB = 2531，得到平台重要性的具体描述：1-唯一平台，2-主要平台，3-重要平台，4-普通平台，5-次要平台。

### BusinessType (城投平台业务类型)

城投平台业务类型(BusinessType)与(CT_SystemConst)表中的DM字段关联，令LB = 2528，得到城投平台业务类型的具体描述：1-产投平台，2-土地开发整理平台，3-基建代建平台，4-棚改保障房开发平台，5-公用事业平台，6-园区功能区平台，7-文化旅游平台，8-轨道交通建设运营平台，9-高速公路建设运营平台，10-铁路建设运营平台，11-交通投融资平台，12-综合型城投平台。

## SQL示例

```sql
-- 查询 城投区域重要性评分表 数据
SELECT *
FROM bond_areaimportance
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
