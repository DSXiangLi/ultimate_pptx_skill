# LC_STIBCDRSHRights

**中文名**: 科创板CDR股权层级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCDRSHRights` |
| MySQL表名 | `lc_stibcdrshrights` |
| 中文名 | 科创板CDR股权层级 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 29 |
| 版本 | 1 |

## 表描述

1.内容说明：本表以CDR公司纬度收录适用CDR发行人以份为单位记录的股本构成情况。
2.数据范围：2020年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `AuthorCommonStock` | 法定普通股股数(份) | number(16,0) | ✓ | 0.0% |  |
| 7 | `PaidinCommonStock` | 实收普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 8 | `CommonStockA` | A类普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 9 | `RestrictedCSA` | 其中:A类有限售股数(份) | number(16,0) | ✓ | 100.0% |  |
| 10 | `NonRestrictedCSA` | 其中:A类无限售股数(份) | number(16,0) | ✓ | 100.0% |  |
| 11 | `CommonStockB` | B类普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 12 | `RestrictedCSB` | 其中:B类有限售股数(份) | number(16,0) | ✓ | 100.0% |  |
| 13 | `NonRestrictedCSB` | 其中:B类无限售股数(份) | number(16,0) | ✓ | 0.0% |  |
| 14 | `CommonStockC` | C类普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 15 | `CommonStockD` | D类普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 16 | `CommonStockOther` | 其他类普通股股数(份) | number(16,0) | ✓ | 100.0% |  |
| 17 | `AuthorPreferStock` | 法定优先股股数(份) | number(16,0) | ✓ | 0.0% |  |
| 18 | `PaidinPreferStock` | 实收优先股股数(份) | number(16,0) | ✓ | 0.0% |  |
| 19 | `ChangeReason` | 股本变动原因说明 | varchar2(2000) | ✓ | 55.36% |  |
| 20 | `ChangePaidinCommon` | 实收普通股变动股数(份) | number(16,0) | ✓ | 100.0% |  |
| 21 | `ChangePaidinCommonA` | (1)A类普通股变动(份) | number(16,0) | ✓ | 100.0% |  |
| 22 | `ChangePaidinCommonB` | (2)B类普通股变动(份) | number(16,0) | ✓ | 100.0% |  |
| 23 | `ChangePaidinCommonC` | (3)C类普通股变动(份) | number(16,0) | ✓ | 0.0% |  |
| 24 | `ChangePaidinCommonD` | (4)D类普通股变动(份) | number(16,0) | ✓ | 0.0% |  |
| 25 | `ChangePaidinCommonO` | (5)其他类普通股变动股数(份) | number(16,0) | ✓ | 0.0% |  |
| 26 | `ChangePaidinPrefer` | 实收优先股变动股数(份) | number(16,0) | ✓ | 0.0% |  |
| 27 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 28 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 29 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 科创板CDR股权层级 数据
SELECT *
FROM lc_stibcdrshrights
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
