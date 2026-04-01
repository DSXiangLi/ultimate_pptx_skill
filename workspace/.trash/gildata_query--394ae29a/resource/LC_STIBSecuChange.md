# LC_STIBSecuChange

**中文名**: 科创板证券简称更改

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSecuChange` |
| MySQL表名 | `lc_stibsecuchange` |
| 中文名 | 科创板证券简称更改 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录了科创板公司的证券简称，历次变更情况及被特别处理(或撤销)的相关信息，包括：简称更改日期、证券简称、简称变更原因等内容。
2.数据范围：2019年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% | 信息发布日期（InfoPublDate）：跟随“事件进程”定义 |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 7.15% |  |
| 6 | `ChangeDate` | 简称更改日期 | date | ✓ | 4.98% |  |
| 7 | `SecuAbbr` | 证券简称 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `ChiSpelling` | 拼音证券简称 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `ExtendedAbbr` | 扩位简称 | varchar2(100) | ✓ | 6.84% |  |
| 10 | `ExtendedSpelling` | 拼音扩位简称 | varchar2(50) | ✓ | 6.84% |  |
| 11 | `BeforeSecuAbbr` | 变动前证券简称 | varchar2(100) | ✓ | 7.15% |  |
| 12 | `BeforeChiSpel` | 变动前拼音证券简称 | varchar2(50) | ✓ | 7.15% |  |
| 13 | `ExtendedSpellingBef` | 变动前扩位简称 | varchar2(100) | ✓ | 5.75% |  |
| 14 | `BeforeExtendedSpel` | 变动前拼音扩位简称 | varchar2(50) | ✓ | 5.75% |  |
| 15 | `ChangeType` | 变更类型 | number(10) | ✗ | 100.0% | 变更类型(ChangeType)：具体描述 1-ST，2-撤销ST，3-PT，4-撤销PT，5-*ST，6-撤销*ST，... |
| 16 | `ChangeCause` | 变更原因说明 | varchar2(400) | ✓ | 3.27% |  |
| 17 | `EventProcedure` | 事件进程 | number(10) | ✗ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AN... |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到科创板上市公司的交易代码、简称等。

### InfoPublDate (信息发布日期)

信息发布日期（InfoPublDate）：跟随“事件进程”定义

### ChangeType (变更类型)

变更类型(ChangeType)：具体描述 1-ST，2-撤销ST，3-PT，4-撤销PT，5-*ST，6-撤销*ST，7-撤消*ST并实行ST，8-从ST变为*ST，9-退市整理期，10-高风险警示，11-撤销高风险警示，12-叠加ST，13-撤销叠加ST，14-叠加*ST，15-撤销叠加*ST，99-其他。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1001,3120,3121,3125,3131,1016,3305)，得到事件进程的具体描述：1001-预案，1016-未实施终止，3120-董事会否决，3121-股东大会通过，3125-股东大会否决，3131-方案实施，3305-放弃。

## SQL示例

```sql
-- 查询 科创板证券简称更改 数据
SELECT *
FROM lc_stibsecuchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
