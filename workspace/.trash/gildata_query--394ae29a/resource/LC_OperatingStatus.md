# LC_OperatingStatus

**中文名**: 公司经营情况述评

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_OperatingStatus` |
| MySQL表名 | `lc_operatingstatus` |
| 中文名 | 公司经营情况述评 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 季更新 |
| 字段数量 | 8 |
| 版本 | 1.02 |

## 表描述

1.收录公司管理层对季度、半年度、年度经营情况的自我评价，以及其后期发展计划和预测，本表涵盖了公司招股以来的历次纪录。
2.数据范围：1997-12-31至今
3.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 39.44% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.85% |  |
| 6 | `OperatingStatement` | 经营述评 | clob | ✓ | 9.98% |  |
| 7 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 公司经营情况述评 数据
SELECT *
FROM lc_operatingstatus
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
