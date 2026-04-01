# LC_ActualController

**中文名**: 公司实际控制人

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ActualController` |
| MySQL表名 | `lc_actualcontroller` |
| 中文名 | 公司实际控制人 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1.01 |

## 表描述

1.收录根据上市公司在招投说明书、定期报告、及临时公告中披露的实际控制人结构图判断的上市公司实际控制人信息。
2.目前只处理实际控制人有变动的数据，下期和本期相比如无变化，则不做处理。
3.数据范围：2004-12-31至今
4.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `ControllerCode` | 实际控制人代码 | number(10) | ✓ | 27.73% | 实际控制人代码（ControllerCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Co... |
| 6 | `ControllerName` | 实际控制人 | varchar2(120) | ✗ | 100.0% |  |
| 7 | `ControllerNature` | 实际控制人所属性质 | number(10) | ✓ | 100.0% | 实际控制人所属性质(ControllerNature)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 8 | `EconomicNature` | 实际控制人经济性质 | number(10) | ✓ | 100.0% | 实际控制人经济性质(EconomicNature)与(CT_SystemConst)表中的DM字段关联，令LB = 15... |
| 9 | `NationalityCode` | 国籍代码 | number(10) | ✓ | 65.05% | 国籍代码（NationalityCode）：与“系统常量表”中的“代码（DM）”关联，令“LB=1023”，得到实际控制... |
| 10 | `NationalityDesc` | 国籍描述 | varchar2(50) | ✓ | 65.05% |  |
| 11 | `PermanentResidency` | 永久其他国家或地区居留权 | varchar2(100) | ✓ | 21.08% |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ControllerCode (实际控制人代码)

实际控制人代码（ControllerCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到实际控制人的名称，企业性质等信息。

### ControllerNature (实际控制人所属性质)

实际控制人所属性质(ControllerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到实际控制人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### EconomicNature (实际控制人经济性质)

实际控制人经济性质(EconomicNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1581，得到实际控制人经济性质的具体描述：1-中央企业，2-地方国有企业，3-民营企业，4-集体企业，5-大学，6-外资，7-工会，99-其它。

### NationalityCode (国籍代码)

国籍代码（NationalityCode）：与“系统常量表”中的“代码（DM）”关联，令“LB=1023”，得到实际控制人的国籍编码。

## SQL示例

```sql
-- 查询 公司实际控制人 数据
SELECT *
FROM lc_actualcontroller
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
