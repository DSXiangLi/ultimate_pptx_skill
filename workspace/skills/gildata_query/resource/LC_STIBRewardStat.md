# LC_STIBRewardStat

**中文名**: 科创板报告期高管薪酬汇总

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBRewardStat` |
| MySQL表名 | `lc_stibrewardstat` |
| 中文名 | 科创板报告期高管薪酬汇总 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 人力资源 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：记录按报告期统计管理层的报酬情况。
2.数据范围：2019年-至今。
3.信息来源：招股说明书、定期报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `TotalYearPay` | 报酬总额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `NumPayManagers` | 领取报酬的管理层人数 | number(10) | ✓ | 61.3% |  |
| 8 | `Remark` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 科创板报告期高管薪酬汇总 数据
SELECT *
FROM lc_stibrewardstat
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
