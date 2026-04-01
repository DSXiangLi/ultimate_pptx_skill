# MF_PortfolioPublished

**中文名**: 公募基金投资组合披露状况表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PortfolioPublished` |
| MySQL表名 | `mf_portfoliopublished` |
| 中文名 | 公募基金投资组合披露状况表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录季报基金投资组合相关披露与不披露的数据及对应数据代码。
2.数据范围：1998年6月起-至今。
3.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 5 | `IfPublish` | 是否披露投资组合数据 | number(10) | ✓ | 100.0% | 是否披露投资组合数据(IfPublish)：1-是；0-否 |
| 6 | `IfReplace` | 是否需填充数据 | number(10) | ✓ | 100.0% | 是否需填充数据(IfReplace)：1-是；0-否 |
| 7 | `RelatedCode` | 提供数据代码 | number(10) | ✗ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfPublish (是否披露投资组合数据)

是否披露投资组合数据(IfPublish)：1-是；0-否

### IfReplace (是否需填充数据)

是否需填充数据(IfReplace)：1-是；0-否

## SQL示例

```sql
-- 查询 公募基金投资组合披露状况表 数据
SELECT *
FROM mf_portfoliopublished
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
