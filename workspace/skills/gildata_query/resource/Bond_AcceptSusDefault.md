# Bond_AcceptSusDefault

**中文名**: 票据承兑人持续逾期名单

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_AcceptSusDefault` |
| MySQL表名 | `bond_acceptsusdefault` |
| 中文名 | 票据承兑人持续逾期名单 |
| 路径 | 聚源新版数据库 > 债券数据库 > 票据基本信息 |
| 更新频率 | 月更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

内容说明：本表收录上海票据交易所披露的各期承兑人逾期或持续逾期名单。
数据范围：2021年9月至今
信息来源：上海票据交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别（InfoType）：1-逾期名单；2-持续逾期名单 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `CompanyCode` | 承兑人公司代码 | number(10) | ✗ | 100.0% | 承兑人公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 6 | `AcceptorName` | 承兑人名称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `SustDefaultStartDate` | 持续逾期开始日期 | date | ✓ | 56.82% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoType (信息类别)

信息类别（InfoType）：1-逾期名单；2-持续逾期名单

### CompanyCode (承兑人公司代码)

承兑人公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

## SQL示例

```sql
-- 查询 票据承兑人持续逾期名单 数据
SELECT *
FROM bond_acceptsusdefault
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
