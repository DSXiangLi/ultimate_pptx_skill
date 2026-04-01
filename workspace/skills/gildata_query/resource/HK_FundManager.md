# HK_FundManager

**中文名**: 香港基金经理

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundManager` |
| MySQL表名 | `hk_fundmanager` |
| 中文名 | 香港基金经理 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.本表记录香港互认基金的历任基金经理、基金经理助理的任职起止日期、管理时间等信息。
2.历史数据：1999年11月起--至今。
3.数据来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `PersonalCode` | 所属人员代码 | number(19) | ✗ | 100.0% | 所属人员代码（PersonalCode）：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码... |
| 6 | `ManagerName` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 7 | `PostName` | 职位名称 | number(10) | ✓ | 100.0% | 职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具... |
| 8 | `Incumbent` | 在任与否 | number(3) | ✓ | 100.0% | 在任与否（Incumbent），该字段固定以下常量： 1-在任；0-离任 |
| 9 | `AccessionDate` | 到任日期 | date | ✗ | 100.0% | 当数据为‘1900-01-01’时，表示无法确认变更日期 |
| 10 | `DimissionDate` | 离职日期 | date | ✓ | 13.85% | 当数据为‘1900-01-01’时，表示无法确认变更日期 |
| 11 | `ManagementTime` | 任职天数(天) | number(10) | ✓ | 100.0% |  |
| 12 | `Performance` | 任职期间基金净值增长率 | number(18,6) | ✓ | 100.0% |  |
| 13 | `Notes` | 备注说明 | varchar2(250) | ✓ | 15.2% |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |
| 15 | `UpdateTime` | 更新日期 | date | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### PersonalCode (所属人员代码)

所属人员代码（PersonalCode）：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。

### PostName (职位名称)

职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具体描述：1-基金经理，2-基金经理助理。

### Incumbent (在任与否)

在任与否（Incumbent），该字段固定以下常量： 1-在任；0-离任

### AccessionDate (到任日期)

当数据为‘1900-01-01’时，表示无法确认变更日期

### DimissionDate (离职日期)

当数据为‘1900-01-01’时，表示无法确认变更日期

## SQL示例

```sql
-- 查询 香港基金经理 数据
SELECT *
FROM hk_fundmanager
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
