# Bond_SystemConst

**中文名**: 债券项目编码表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SystemConst` |
| MySQL表名 | `bond_systemconst` |
| 中文名 | 债券项目编码表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 资产支持证券信息 |
| 更新频率 | 滚动更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

本表目前主要用于对债券分类的编码和资产支持证券资产池的总体信息和分布提供标准化的常量编码信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `LB` | 常量分类编码 | number(10) | ✗ | 100.0% |  |
| 3 | `LBMC` | 常量分类名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `MS` | 常量描述 | varchar2(300) | ✓ | 100.0% |  |
| 5 | `DM` | 常量代码 | number(19) | ✗ | 100.0% |  |
| 6 | `CVALUE` | 字符值 | varchar2(2000) | ✓ | 25.23% |  |
| 7 | `IVALUE` | 整型值 | number(10) | ✓ | 25.23% |  |
| 8 | `InfoLevel` | 当前层级 | number(10) | ✓ | 46.06% |  |
| 9 | `FatherCode` | 父类代码 | number(19) | ✓ | 16.14% |  |
| 10 | `EffectiveDate` | 生效日期 | date | ✓ | 0.0% |  |
| 11 | `ExpiryDate` | 失效日期 | date | ✓ | 0.19% |  |
| 12 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 债券项目编码表 数据
SELECT *
FROM bond_systemconst
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
