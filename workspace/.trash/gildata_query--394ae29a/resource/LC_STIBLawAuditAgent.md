# LC_STIBLawAuditAgent

**中文名**: 科创板法律与审计中介机构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBLawAuditAgent` |
| MySQL表名 | `lc_stiblawauditagent` |
| 中文名 | 科创板法律与审计中介机构 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：收录了科创板上市公司自公开发行以来所有聘请的法律、审计中介机构及变更情况。
2.数据范围：科创板上市至今
3.信息来源：招股说明书、董事会公告、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `ChangeDate` | 变动日期 | date | ✗ | 100.0% |  |
| 6 | `AgentType` | 机构类别 | number(10) | ✗ | 100.0% | 机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1115 AND DM ... |
| 7 | `AgentCode` | 机构编码 | number(10) | ✗ | 100.0% | 机构编码（AgentCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCod... |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取“上市板块(ListedSector)”=7-科创板且“证券类别(SecuCategory)”=1-A股，得到上市公司的交易代码、简称等。

### AgentType (机构类别)

机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1115 AND DM in (1,3,4,14,15,17)，得到机构类别的具体描述：1-发行人法律顾问，3-会计师事务所，4-财务顾问，14-境外财务顾问，15-境外律师事务所，17-境外会计师事务所。

### AgentCode (机构编码)

机构编码（AgentCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到法律与审计机构的基本资料。

## SQL示例

```sql
-- 查询 科创板法律与审计中介机构 数据
SELECT *
FROM lc_stiblawauditagent
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
