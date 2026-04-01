# LC_RewardStat

**中文名**: 公司管理层报酬统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_RewardStat` |
| MySQL表名 | `lc_rewardstat` |
| 中文名 | 公司管理层报酬统计 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司人力资源 |
| 更新频率 | 季更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.按报告期统计管理层的报酬情况，包括报酬总额、前三名董事报酬、前三名高管报酬、报酬区间统计分析等。
2.数据范围：2001-12-31至今
3.信息来源：定期报告、招股说明书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.99% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `TotalYearPay` | 报酬总额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `NumPayManagers` | 领取报酬的管理层人数 | number(10) | ✓ | 91.59% |  |
| 8 | `High3Directors` | 前三名董事报酬(元) | number(19,4) | ✓ | 88.4% |  |
| 9 | `High3Managers` | 前三名高管报酬(元) | number(19,4) | ✓ | 87.77% |  |
| 10 | `TotalIndeSupeYearPay` | 独立董事津贴(元/人) | number(19,4) | ✓ | 9.0% |  |
| 11 | `TotalIndeSubsidy` | 独立董事津贴总额(元) | number(19,4) | ✓ | 9.0% |  |
| 12 | `Statement` | 备注说明 | varchar2(500) | ✓ | 0.02% |  |
| 13 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 公司管理层报酬统计 数据
SELECT *
FROM lc_rewardstat
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
