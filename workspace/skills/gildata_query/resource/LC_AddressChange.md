# LC_AddressChange

**中文名**: 公司地址变更明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AddressChange` |
| MySQL表名 | `lc_addresschange` |
| 中文名 | 公司地址变更明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定时更新 |
| 字段数量 | 32 |
| 版本 | 1 |

## 表描述

1.收录上市公司公告中披露的公司地址变更等重大事项描述说明。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `AnnouncementType` | 公告类型 | number(10) | ✓ | 100.0% | 公告类型(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 1109，... |
| 7 | `DisclosureMethod` | 披露方式 | number(10) | ✓ | 100.0% | 披露方式(DisclosureMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1221，... |
| 8 | `EventContent` | 事件内容 | clob | ✓ | 2.24% |  |
| 9 | `ActionDesc` | 行为描述 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `NewestAdvance` | 最新进展状态描述 | varchar2(200) | ✓ | 25.42% |  |
| 11 | `EventSubject` | 事件主体 | number(10) | ✓ | 100.0% | 事件主体(EventSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1246，得到事件... |
| 12 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AN... |
| 13 | `ActionWays` | 行为方式 | number(10) | ✓ | 100.0% | 行为方式(ActionWays)与(CT_SystemConst)表中的DM字段关联，令LB = 1063 AND DM... |
| 14 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 0.0% |  |
| 15 | `SubjectName` | 事件主体名称 | varchar2(100) | ✓ | 100.0% |  |
| 16 | `SubjectCode` | 事件主体企业编号 | number(10) | ✓ | 1.35% | 事件主体企业编号(SubjectCode)和机构基本资料表(CompanyCode)关联 |
| 17 | `SubjectAssociation` | 与上市公司关联关系 | number(10) | ✓ | 100.0% | 与上市公司关联关系(SubjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 18 | `ObjectName` | 交易对象名称 | varchar2(100) | ✓ | 0.0% |  |
| 19 | `ObjectCode` | 交易对象企业编号 | number(10) | ✓ | 0.0% | 交易对象企业编号(ObjectCode)和机构基本资料表(CompanyCode)关联 |
| 20 | `ObjectAssociation` | 与上市公司关联关系 | number(10) | ✓ | 0.0% | 与上市公司关联关系(ObjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 21 | `AgreementDate` | 协议签署日期 | date | ✓ | 0.17% |  |
| 22 | `IfEnded` | 是否终止 | number(10) | ✓ | 0.25% | 是否终止(IfEnded)固定常量：0->否1->是 |
| 23 | `Note` | 备注 | varchar2(300) | ✓ | 0.0% |  |
| 24 | `AddressChangeType` | 地址变更类型 | number(10) | ✓ | 100.0% | 地址变更类型(AddressChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 11... |
| 25 | `AddressPreChange` | 变更前地址 | varchar2(100) | ✓ | 100.0% |  |
| 26 | `CodePreChange` | 变更前邮编 | varchar2(6) | ✓ | 100.0% |  |
| 27 | `RegionPreChange` | 变更前所属地区 | number(10) | ✓ | 100.0% | 变更前所属地区(RegionPreChange)：优先关联系统常量表中的DM字段关联，令LB = 1145，得到所属地区... |
| 28 | `AddressAfterChange` | 变更后地址 | varchar2(100) | ✓ | 100.0% |  |
| 29 | `CodeAfterChange` | 变更后邮编 | varchar2(6) | ✓ | 100.0% |  |
| 30 | `RegionAfterChange` | 变更后所属地区 | number(10) | ✓ | 100.0% | 变更后所属地区(RegionAfterChange)：优先关联系统常量表中的DM字段关联，令LB = 1145，得到所属... |
| 31 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### AnnouncementType (公告类型)

公告类型(AnnouncementType)与(CT_SystemConst)表中的DM字段关联，令LB = 1109，得到公告类型的具体描述：1-董事会公告，2-股东大会公告，3-监事会公告，4-公司公告，5-法律意见书，6-财务报告，7-中国证监会公告，8-交易所公告，9-中介机构公告，10-基金投资组合公告，11-回访报告，12-独立董事声明，13-债券公告，14-三板市场公司公告，15-基金公告，18-收购报告书，30-新股发行公告，31-增发发行公告，32-债券发行公告，33-基金发行公告，34-配股发行公告，40-增发股本变动公告，41-配股股本变动公告，43-债券上市公告，50-分红公告，60-期货公告，61-股权分置改革说明书，99-其它。

### DisclosureMethod (披露方式)

披露方式(DisclosureMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1221，得到披露方式的具体描述：1-正常披露，2-事后披露。

### EventSubject (事件主体)

事件主体(EventSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1246，得到事件主体的具体描述：1-上市公司，2-下属公司，3-公司股东，4-债券发行人。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN ( 1004,1001,1007)，得到事件进程的具体描述：1001-预案，1004-决案，1007-否决。

### ActionWays (行为方式)

行为方式(ActionWays)与(CT_SystemConst)表中的DM字段关联，令LB = 1063 AND DM IN (2501,2504,2507)，得到行为方式的具体描述：2501-注册地址变更，2504-办公地址变更，2507-联系地址变更。

### SubjectCode (事件主体企业编号)

事件主体企业编号(SubjectCode)和机构基本资料表(CompanyCode)关联

### SubjectAssociation (与上市公司关联关系)

与上市公司关联关系(SubjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接兄弟企业，80-间接控股股东，83-潜在控股股东，84-潜在非控股股东，86-转让前控股股东，87-转让前非控股股东，121-股权受托管理人，122-受同一方控制，999-无关联关系。

### ObjectCode (交易对象企业编号)

交易对象企业编号(ObjectCode)和机构基本资料表(CompanyCode)关联

### ObjectAssociation (与上市公司关联关系)

与上市公司关联关系(ObjectAssociation)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到与上市公司关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接兄弟企业，80-间接控股股东，83-潜在控股股东，84-潜在非控股股东，86-转让前控股股东，87-转让前非控股股东，121-股权受托管理人，122-受同一方控制，999-无关联关系。

## SQL示例

```sql
-- 查询 公司地址变更明细 数据
SELECT *
FROM lc_addresschange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
