# CS_RiskWarningAnnounce

**中文名**: 股票风险警示提示表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_RiskWarningAnnounce` |
| MySQL表名 | `cs_riskwarningannounce` |
| 中文名 | 股票风险警示提示表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1. 内容说明：收录可能被风险警示、可能被终止上市、被风险警示、终止上市的相关公告信息。终止上市后数据在【终止上市基本资料表，CS_DelistingBasicInfo】中提示
2. 数据范围：2024年7月至今
3. 信息来源：公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `InfoSource` | 信息来源 | varchar2(300) | ✓ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 6 | `RiskWarningAnnounceType` | 风险提示类型 | number(10) | ✗ | 100.0% | 风险提示类型(RiskWarningAnnounceType)与(CT_SystemConst)表中的DM字段关联，令L... |
| 7 | `AnnounceNumber` | 提示次数 | number(10) | ✓ | 100.0% |  |
| 8 | `TextAnnID` | 风险预警非文本ID | number(19) | ✓ | 93.22% | 风险预警非文本ID(TextAnnID)：可关联公司公告原文非文本(DZ_NotTextAnnouncement)的ID... |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### RiskWarningAnnounceType (风险提示类型)

风险提示类型(RiskWarningAnnounceType)与(CT_SystemConst)表中的DM字段关联，令LB=2629，得到风险提示类型的具体描述：1-可能被实施其他风险警示，2-可能被实施退市风险警示，3-可能被终止上市风险警示，4-可能被叠加实施退市风险警示，5-可能被叠加实施其他风险警示，6-被实施其他风险警示，7-被实施退市风险警示，8-被终止上市风险警示，9-主动终止上市风险警示，10-被叠加实施其他风险警示，11-被叠加实施退市风险警示，12-撤销其他风险警示，13-撤销退市风险警示，14-暂停上市风险警示，15-恢复上市风险警示，16-可能被实施退市风险警示及其他风险警示，17-被实施退市风险警示及其他风险警示，18-被叠加实施退市风险警示及其他风险警示，19-可能被叠加实施退市风险警示及其他风险警示，20-撤销退市风险警示及其他风险警示，21-撤销终止上市，99-其他。

### TextAnnID (风险预警非文本ID)

风险预警非文本ID(TextAnnID)：可关联公司公告原文非文本(DZ_NotTextAnnouncement)的ID，获取对应的公告

## SQL示例

```sql
-- 查询 股票风险警示提示表 数据
SELECT *
FROM cs_riskwarningannounce
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
