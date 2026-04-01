# Bond_NoteInfoA

**中文名**: 票据基本信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_NoteInfoA` |
| MySQL表名 | `bond_noteinfoa` |
| 中文名 | 票据基本信息附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 票据基本信息 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

内容说明：票据基本信息附表，记录票据其他的基本信息，如持票人、是否已贴现、贴现人等数据
数据范围：2019年开始
信息来源：目前维护标准化票据的基础资产清单票据信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 票据内部编码 | number(10) | ✗ | 100.0% | 票据内部编码(InnerCode)：内码范围从15500000开始 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `IndicatorCode` | 指标代码 | number(10) | ✗ | 100.0% | 指标代码(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2281，得到指... |
| 5 | `DataValue` | 指标数据 | number(10) | ✓ | 100.0% | 指标数据(DataValue)：当IndicatorCode 以“10”开头，与“机构基本资料（LC_InstiArch... |
| 6 | `Content` | 指标文本 | varchar2(500) | ✓ | 0.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (票据内部编码)

票据内部编码(InnerCode)：内码范围从15500000开始

### IndicatorCode (指标代码)

指标代码(IndicatorCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2281，得到指标代码的具体描述：1001-贴现人，1002-持票人，1003-承兑保证人，1004-贴现保证人，2001-是否已贴现，3001-对应标准化票据INBBM。

### DataValue (指标数据)

指标数据(DataValue)：当IndicatorCode 以“10”开头，与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。当IndicatorCode=2001，与 系统常量表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否贴现的具体描述：1-是，2-否。当Indicator=3001，与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到标准化票据的交易代码、债券简称等

## SQL示例

```sql
-- 查询 票据基本信息附表 数据
SELECT *
FROM bond_noteinfoa
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
