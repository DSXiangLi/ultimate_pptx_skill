# Bond_NoteInfo

**中文名**: 票据基本信息表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_NoteInfo` |
| MySQL表名 | `bond_noteinfo` |
| 中文名 | 票据基本信息表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 票据基本信息 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

内容说明：记录票据的票面金额、出票日期、出票人等基本信息
数据范围：2019年开始
信息来源：目前维护标准化票据的基础资产清单票据信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 票据内部编码 | number(10) | ✗ | 100.0% | 票据内部编码(InnerCode)：内码范围从15500000开始 |
| 3 | `NoteCode` | 票据号码 | varchar2(50) | ✗ | 100.0% | 票据号码(NoteCode)：披露的票据号码 |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=201 and DM in... |
| 5 | `TypeCode` | 票据类别 | number(10) | ✓ | 100.0% | 票据类别(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2280，得到票据类别的具... |
| 6 | `Medium` | 票据介质 | number(10) | ✓ | 98.78% | 票据介质(Medium)与(CT_SystemConst)表中的DM字段关联，令LB = 2279，得到票据介质的具体描... |
| 7 | `BeginDate` | 出票日期 | date | ✓ | 100.0% |  |
| 8 | `MaturityDate` | 到期日 | date | ✓ | 100.0% |  |
| 9 | `TotalSize` | 票据金额(万元) | number(15,6) | ✓ | 100.0% |  |
| 10 | `DrawerName` | 出票人名称 | varchar2(100) | ✓ | 100.0% | 出票人名称(DrawerName)：仅披露值，如想获得准确的机构名称，可根据出票人字段关联机构表取值 |
| 11 | `Drawer` | 出票人 | number(10) | ✓ | 100.0% | 出票人(Drawer)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关... |
| 12 | `AcceptorName` | 承兑人名称 | varchar2(100) | ✓ | 100.0% | 承兑人名称(AcceptorName)：仅披露值，如想获得准确的机构名称，可根据承兑人字段关联机构表取值 |
| 13 | `Acceptor` | 承兑人 | number(10) | ✓ | 100.0% | 承兑人(Acceptor)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）... |
| 14 | `MarginRatio` | 保证金比例 | number(12,6) | ✓ | 9.53% | 保证金比例(MarginRatio)：披露值 |
| 15 | `SInnerCode` | 对应标准化票据内码 | number(10) | ✓ | 100.0% | 对应标准化票据内码(SInnerCode)：如果票据作为标准化票据基础资产，有对应标准化票据内码。与“债券代码对照表（B... |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (票据内部编码)

票据内部编码(InnerCode)：内码范围从15500000开始

### NoteCode (票据号码)

票据号码(NoteCode)：披露的票据号码

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=201 and DM in (16)，得到信息来源的具体描述：16-上海票据交易所。

### TypeCode (票据类别)

票据类别(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2280，得到票据类别的具体描述：1001-银行承兑汇票，1002-商业承兑汇票。

### Medium (票据介质)

票据介质(Medium)与(CT_SystemConst)表中的DM字段关联，令LB = 2279，得到票据介质的具体描述：1-电票，2-纸票。

### DrawerName (出票人名称)

出票人名称(DrawerName)：仅披露值，如想获得准确的机构名称，可根据出票人字段关联机构表取值

### Drawer (出票人)

出票人(Drawer)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### AcceptorName (承兑人名称)

承兑人名称(AcceptorName)：仅披露值，如想获得准确的机构名称，可根据承兑人字段关联机构表取值

### Acceptor (承兑人)

承兑人(Acceptor)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### MarginRatio (保证金比例)

保证金比例(MarginRatio)：披露值

## SQL示例

```sql
-- 查询 票据基本信息表 数据
SELECT *
FROM bond_noteinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
