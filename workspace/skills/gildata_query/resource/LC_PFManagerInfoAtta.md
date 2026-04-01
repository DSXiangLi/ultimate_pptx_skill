# LC_PFManagerInfoAtta

**中文名**: 私募基金管理人-公示信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PFManagerInfoAtta` |
| MySQL表名 | `lc_pfmanagerinfoatta` |
| 中文名 | 私募基金管理人-公示信息附表 |
| 路径 | 聚源新版数据库 > 机构数据库 > 私募基金管理人 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1. 内容说明：本表为“协会私募基金管理人公示信息”LC_PFManagerInfo”的衍生表，具体收录私募基金管理人公示信息中的业务类型
2. 数据范围：最新数据
3. 信息来源：中国证券投资基金业协会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“私募基金管理人公示信息（LC_PFManagerInfo）”中的“ID”关联。 |
| 3 | `IndicatorType` | 指标类型 | number(10) | ✗ | 100.0% | 指标类型（IndicatorType）：该字段固定以下常量：1-业务类型代码。 |
| 4 | `IndicatorCode` | 指标代码 | number(10) | ✗ | 100.0% | 指标代码(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2502 AND... |
| 5 | `IfEffected` | 是否有效 | number(10) | ✓ | 99.99% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“私募基金管理人公示信息（LC_PFManagerInfo）”中的“ID”关联。

### IndicatorType (指标类型)

指标类型（IndicatorType）：该字段固定以下常量：1-业务类型代码。

### IndicatorCode (指标代码)

指标代码(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2502 AND DM  IN (13,15,23,24,14,7,25,16,11,98,97)，得到指标代码的具体描述：7-创业投资基金，11-私募证券投资基金，13-私募资产配置基金，14-私募股权投资基金，15-创业投资类FOF基金，16-私募股权投资类FOF基金，23-私募证券投资类FOF基金，24-QDLP等试点机构，25-其他私募投资基金，97-未确认，98-其他私募投资类FOF基金。

## SQL示例

```sql
-- 查询 私募基金管理人-公示信息附表 数据
SELECT *
FROM lc_pfmanagerinfoatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
