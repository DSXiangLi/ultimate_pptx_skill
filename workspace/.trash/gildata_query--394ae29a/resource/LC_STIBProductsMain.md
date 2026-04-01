# LC_STIBProductsMain

**中文名**: 科创板产品主表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBProductsMain` |
| MySQL表名 | `lc_stibproductsmain` |
| 中文名 | 科创板产品主表 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 产品供销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 6 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录产品的基本信息，包括产品名称、编码；
2.信息来源：招股说明书，定期报告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 产品内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `ProductName` | 产品名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 5 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 6 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 科创板产品主表 数据
SELECT *
FROM lc_stibproductsmain
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
