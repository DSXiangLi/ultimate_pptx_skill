# FM_FundCSMSSize

**中文名**: 基金管理公司及其子公司专户业务规模

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FM_FundCSMSSize` |
| MySQL表名 | `fm_fundcsmssize` |
| 中文名 | 基金管理公司及其子公司专户业务规模 |
| 路径 | 聚源新版数据库 > 市场统计数据库 > 证券市场统计 |
| 更新频率 | 季更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

1.本表记录基金管理公司及其子公司专户业务的相关产品数量和资产规模等统计情况。
2.数据范围：2014.12-至今
3.信息来源：中国证券投资基金业协会；

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `StatPeriod` | 统计区间 | number(10) | ✗ | 100.0% | 统计区间（StatPeriod）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1... |
| 6 | `FundCompanyN` | 1.基金公司(只) | number(10) | ✓ | 100.0% |  |
| 7 | `OneToOneN` | 基金公司:一对一产品(只) | number(10) | ✓ | 100.0% |  |
| 8 | `OneToManyN` | 基金公司:一对多产品(只) | number(10) | ✓ | 100.0% |  |
| 9 | `SSFundOPensionN` | 基金公司:社保基金及企业年金(只) | number(10) | ✓ | 4.0% |  |
| 10 | `SubCompanyN` | 2.基金子公司(只) | number(10) | ✓ | 100.0% |  |
| 11 | `SubOneToOneN` | 基金子公司:一对一产品(只) | number(10) | ✓ | 100.0% |  |
| 12 | `SubOneToManyN` | 基金子公司:一对多产品(只) | number(10) | ✓ | 100.0% |  |
| 13 | `TotalSAccountN` | 合计-产品数量(只) | number(10) | ✓ | 100.0% |  |
| 14 | `FundCompanyS` | 1.基金公司(亿元) | number(10,2) | ✓ | 100.0% |  |
| 15 | `OneToOneS` | 基金公司:一对一产品(亿元) | number(10,2) | ✓ | 100.0% |  |
| 16 | `OneToManyS` | 基金公司:一对多产品(亿元) | number(10,2) | ✓ | 100.0% |  |
| 17 | `SSFundOPensionS` | 基金公司:社保基金及企业年金(亿元) | number(10,2) | ✓ | 56.0% |  |
| 18 | `SubCompanyS` | 2.基金子公司(亿元) | number(10,2) | ✓ | 100.0% |  |
| 19 | `SubOneToOneS` | 基金子公司:一对一产品(亿元) | number(10,2) | ✓ | 100.0% |  |
| 20 | `SubOneToManyS` | 基金子公司:一对多产品(亿元) | number(10,2) | ✓ | 100.0% |  |
| 21 | `TotalSAccountS` | 合计-资产规模(亿元) | number(10,2) | ✓ | 100.0% |  |
| 22 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StatPeriod (统计区间)

统计区间（StatPeriod）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1954”，得到数据的具体统计区间：210-当季及累计。

## SQL示例

```sql
-- 查询 基金管理公司及其子公司专户业务规模 数据
SELECT *
FROM fm_fundcsmssize
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
