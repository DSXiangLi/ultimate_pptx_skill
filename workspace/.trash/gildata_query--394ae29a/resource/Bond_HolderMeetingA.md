# Bond_HolderMeetingA

**中文名**: 债券持有人大会附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_HolderMeetingA` |
| MySQL表名 | `bond_holdermeetinga` |
| 中文名 | 债券持有人大会附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 日更新 |
| 字段数量 | 23 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录债券持有人大会的召集人和详细的议案情况以及议案是否通过等信息。
本表通过内部代码和首次会议通知公告日和债券持有人大会主表进行关联取得详细的会议通知决议信息。
2.数据范围：2015年至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InitialInfoPublDate` | 首次会议通知公告日 | date | ✗ | 100.0% |  |
| 4 | `EventType` | 事件类型 | number(10) | ✗ | 100.0% | 事件类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2203，得到事件类型的... |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `CompanyCode` | 召集人企业编号 | number(10) | ✓ | 22.76% | 召集人企业编号(CompanyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 7 | `MotionTitle` | 议案标题 | varchar2(1000) | ✓ | 37.08% |  |
| 8 | `MotionType` | 议案分类 | number(10) | ✓ | 33.65% | 议案分类(MotionType)与(CT_SystemConst)表中的DM字段关联，令LB = 2278，得到议案分类... |
| 9 | `IfPassed` | 是否通过 | number(10) | ✓ | 34.51% | 是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN... |
| 10 | `ReasonDesc` | 未通过原因描述 | varchar2(2000) | ✓ | 9.4% |  |
| 11 | `IssuerIfPassed` | 发行人是否同意 | number(10) | ✓ | 8.32% | 发行人是否同意(IssuerIfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 ... |
| 12 | `IssuerReplyInfo` | 发行人回复情况 | varchar2(2000) | ✓ | 9.43% |  |
| 13 | `Contactman` | 联系人 | varchar2(400) | ✓ | 35.45% |  |
| 14 | `ContactTel` | 联系电话 | varchar2(200) | ✓ | 35.16% |  |
| 15 | `ContactFax` | 传真 | varchar2(200) | ✓ | 6.97% |  |
| 16 | `ContactAddr` | 联系地址 | varchar2(400) | ✓ | 32.29% |  |
| 17 | `ContactZipCode` | 邮政编码 | varchar2(200) | ✓ | 18.09% |  |
| 18 | `ContactEmail` | 邮箱 | varchar2(400) | ✓ | 38.35% |  |
| 19 | `ContactWebsite` | 网址 | varchar2(400) | ✓ | 0.07% |  |
| 20 | `Remarks` | 备注 | varchar2(2000) | ✓ | 74.23% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### EventType (事件类型)

事件类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2203，得到事件类型的具体描述：1-召集人，2-议案，10-表决联系方式，11-登记联系方式，12-其他联系方式。

### CompanyCode (召集人企业编号)

召集人企业编号(CompanyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到企业的基本信息。

### MotionType (议案分类)

议案分类(MotionType)与(CT_SystemConst)表中的DM字段关联，令LB = 2278，得到议案分类的具体描述：1001-减资，1002-分立，1003-合并，1004-解散，1005-破产重组或申请破产，1006-实际控制人变更，1007-债务重组，1008-债务置换或转移，1009-资产重组、置换、划转，1010-出售或转移资产，1011-财务承担或减免，1012-对外提供大额担保，2001-变更赎回回售票面利率选择权条款，2002-变更其他权利条款，2003-变更担保措施，2004-债券展期兑付，2005-债券提前兑付，2006-债券转股，2007-调整票面利率，2008-变更债券其他条款，2009-变更发行主体，2010-变更募集资金用途，2011-债券持有人会议规则，2012-变更其他中介机构，2013-信息披露，9099-其他。

### IfPassed (是否通过)

是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否通过的具体描述：1-是，2-否。

### IssuerIfPassed (发行人是否同意)

发行人是否同意(IssuerIfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到发行人是否同意的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 债券持有人大会附表 数据
SELECT *
FROM bond_holdermeetinga
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
