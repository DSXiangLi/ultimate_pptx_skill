# HK_OperatingStatus

**中文名**: 港股经营述评

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_OperatingStatus` |
| MySQL表名 | `hk_operatingstatus` |
| 中文名 | 港股经营述评 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.记录港股的经营回顾、展望以及其他事项，包含的主要字段有：信息来源、截止日期、经营回顾、经营展望等。
2.数据范围：2001年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 6 | `Retrospection` | 经营回顾 | clob | ✓ | 1.68% |  |
| 7 | `Prospect` | 经营展望 | clob | ✓ | 10.58% |  |
| 8 | `Others` | 其他事项 | clob | ✓ | 77.5% |  |
| 9 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股经营述评 数据
SELECT *
FROM hk_operatingstatus
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
