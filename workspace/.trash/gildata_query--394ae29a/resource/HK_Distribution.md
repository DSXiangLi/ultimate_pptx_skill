# HK_Distribution

**中文名**: 港股新股公开发售分配结果

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_Distribution` |
| MySQL表名 | `hk_distribution` |
| 中文名 | 港股新股公开发售分配结果 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录香港上市公司首次上市分配结果，包括有效申购股数和份数，实际配发股数和份数，额外配发股数和份数等。
2.数据范围：2018-01-01至今
3.信息来源：港交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% | 与港股发行与上市HK_ShareIPO中首次信息发布日期InitialInfoPublDate相关联，为公开发售最早开始... |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM... |
| 6 | `GroupID` | 分组 | number(10) | ✗ | 100.0% | 分组(GroupID)与(CT_SystemConst)表中的DM字段关联，令LB = 2157，得到分组的具体描述：1... |
| 7 | `ApplyNumSub` | 申请认购股数 | number(19,0) | ✓ | 100.0% |  |
| 8 | `ValidApplyShares` | 有效申请数 | number(19,0) | ✓ | 100.0% |  |
| 9 | `DistributionNum` | 配发份数 | number(19,0) | ✓ | 100.0% |  |
| 10 | `DistributionShares` | 配发股数 | number(19,0) | ✓ | 100.0% |  |
| 11 | `AddDistributionNum` | 额外配发份数 | number(19,0) | ✓ | 32.31% |  |
| 12 | `AddDistributionShares` | 额外配发股数 | number(19,0) | ✓ | 32.31% |  |
| 13 | `ApplySubRatio` | 获配发占申请认购总数百分比(%) | number(19,4) | ✓ | 100.0% |  |
| 14 | `Remark` | 备注 | varchar2(1000) | ✓ | 24.69% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### InfoPublDate (信息发布日期)

与港股发行与上市HK_ShareIPO中首次信息发布日期InitialInfoPublDate相关联，为公开发售最早开始的日期。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM = 27，得到信息来源的具体描述：27-配发结果。

### GroupID (分组)

分组(GroupID)与(CT_SystemConst)表中的DM字段关联，令LB = 2157，得到分组的具体描述：10-甲组，20-乙组，30-不分组，40-雇员优先分配组，99-其他分组。

## SQL示例

```sql
-- 查询 港股新股公开发售分配结果 数据
SELECT *
FROM hk_distribution
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
