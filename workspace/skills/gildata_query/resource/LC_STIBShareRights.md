# LC_STIBShareRights

**中文名**: 科创板股权层级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBShareRights` |
| MySQL表名 | `lc_stibsharerights` |
| 中文名 | 科创板股权层级 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.内容说明：本表以公司纬度收录适用科创板上市公司的股本构成情况。
2.数据范围：科创板上市至今
3.信息来源：上海证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `AuthorCommonStock` | 法定普通股股数(股) | number(18,2) | ✓ | 98.88% |  |
| 7 | `PaidinCommonStock` | 实收普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 8 | `CommonStockA` | A类普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 9 | `RestrictedCSA` | 其中:A类有限售股数(股) | number(18,2) | ✓ | 79.18% |  |
| 10 | `NonRestrictedCSA` | A类无限售股数(股) | number(18,2) | ✓ | 20.07% |  |
| 11 | `CommonStockB` | B类普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 12 | `RestrictedCSB` | 其中:B类有限售股数(股) | number(18,2) | ✓ | 73.98% |  |
| 13 | `NonRestrictedCSB` | B类无限售股数(股) | number(18,2) | ✓ | 59.11% |  |
| 14 | `CommonStockC` | C类普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 15 | `CommonStockD` | D类普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 16 | `CommonStockOther` | 其他类普通股股数(股) | number(18,2) | ✓ | 100.0% |  |
| 17 | `AuthorPreferStock` | 法定优先股股数(股) | number(18,2) | ✓ | 3.35% |  |
| 18 | `PaidinPreferStock` | 实收优先股股数(股) | number(18,2) | ✓ | 3.35% |  |
| 19 | `ChangeType` | 股本变动原因类别 | number(10) | ✓ |  |  |
| 20 | `ChangeReason` | 股本变动原因说明 | varchar2(500) | ✓ | 59.48% |  |
| 21 | `ChangePaidinCommon` | 实收普通股变动股数(股) | number(18,2) | ✓ | 79.18% |  |
| 22 | `ChangePaidinCommonA` | (1)A类股变动(股) | number(18,2) | ✓ | 79.18% |  |
| 23 | `ChangePaidinCommonB` | (2)B类股变动(股) | number(18,2) | ✓ | 79.18% |  |
| 24 | `ChangePaidinCommonC` | (3)C类股变动(股) | number(18,2) | ✓ | 0.0% |  |
| 25 | `ChangePaidinCommonD` | (4)D类股变动(股) | number(18,2) | ✓ | 0.0% |  |
| 26 | `ChangePaidinCommonO` | (5)其他类普通股变动股数(股) | number(18,2) | ✓ | 0.0% |  |
| 27 | `ChangePaidinPrefer` | 实收优先股变动股数(股) | number(18,2) | ✓ | 0.0% |  |
| 28 | `AID` | 公告ID | number(19) | ✓ | 0.0% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取“上市板块(ListedSector)”=7-科创板且“证券类别(SecuCategory)”=1-A股，得到上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 科创板股权层级 数据
SELECT *
FROM lc_stibsharerights
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
