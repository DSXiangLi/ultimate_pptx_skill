# LC_STIBNameChange

**中文名**: 科创板公司名称更改

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBNameChange` |
| MySQL表名 | `lc_stibnamechange` |
| 中文名 | 科创板公司名称更改 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：收录科创板公司上市后的名称历次变更情况，包括：中英文名称、中英文缩写名称、更改日期等内容。
2.数据范围：2019年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上... |
| 3 | `InitialInfoPublDate` | 首次信息日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% | 信息发布日期（InfoPublDate）：跟随“事件进程”定义 |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 15.08% |  |
| 6 | `ChangeDate` | 全称更改日期 | date | ✓ | 4.84% |  |
| 7 | `ChiName` | 中文名称 | varchar2(200) | ✗ | 100.0% |  |
| 8 | `ChiNameAbbr` | 中文名称缩写 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `EngName` | 英文名称 | varchar2(200) | ✓ | 99.72% |  |
| 10 | `EngNameAbbr` | 英文名称缩写 | varchar2(50) | ✓ | 33.14% |  |
| 11 | `BeforeChiName` | 变更前中文 | varchar2(200) | ✓ | 15.08% |  |
| 12 | `BeforeEngName` | 变更前英文 | varchar2(200) | ✓ | 15.08% |  |
| 13 | `EventProcedure` | 事件进程 | number(10) | ✗ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AN... |
| 14 | `AID` | 公告ID | number(19) | ✓ | 0.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

### InfoPublDate (信息发布日期)

信息发布日期（InfoPublDate）：跟随“事件进程”定义

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1001,3120,3121,3125,3131,1016,3305)，得到事件进程的具体描述：1001-预案，1016-未实施终止，3120-董事会否决，3121-股东大会通过，3125-股东大会否决，3131-方案实施，3305-放弃。

## SQL示例

```sql
-- 查询 科创板公司名称更改 数据
SELECT *
FROM lc_stibnamechange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
