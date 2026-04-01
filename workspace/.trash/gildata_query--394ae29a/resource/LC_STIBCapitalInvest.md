# LC_STIBCapitalInvest

**中文名**: 科创板资金投向说明

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCapitalInvest` |
| MySQL表名 | `lc_stibcapitalinvest` |
| 中文名 | 科创板资金投向说明 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

1.内容说明：科创板公司自有资金、通过发行新股、增发新股、配股等方式所得募集资金的项目投资情况以及运用进展和改投状况。
2.数据范围：科创板上市至今
3.信息来源：董事会公告、招股意向书、招股说明书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `RaisingMethod` | 募资方式 | number(10) | ✗ | 100.0% | 募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令 LB = 1021 AN... |
| 7 | `RaisingPurpose` | 募资用途 | number(10) | ✓ | 99.97% | 募资用途(RaisingPurpose)与(CT_SystemConst)表中的DM字段关联，令LB = 2208，得到... |
| 8 | `ProjectNumber` | 募投项目序号 | number(10) | ✗ | 100.0% |  |
| 9 | `InvestProject` | 募资投向项目名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `ProjectStatement` | 项目内容 | clob | ✓ | 2.72% |  |
| 11 | `PlannedSum` | 计划投入金额(元) | number(19,4) | ✓ | 96.48% |  |
| 12 | `ActualInvestEndDate` | 实际投入截至日期 | date | ✓ | 29.75% |  |
| 13 | `ActualSum` | 实际投入金额(元) | number(19,4) | ✓ | 29.16% |  |
| 14 | `ProceedingStatement` | 进展和收益说明 | clob | ✓ | 20.06% |  |
| 15 | `IfSwitched` | 改投与否 | number(10) | ✓ | 31.67% | 改投与否(IfSwitched)与(CT_SystemConst)表中的DM字段关联，令LB = 1219，得到改投与否... |
| 16 | `SwitchedDate` | 改投公告日期 | date | ✓ | 8.2% |  |
| 17 | `ProjectSwitchedTo` | 改投项目 | varchar2(255) | ✓ | 6.34% |  |
| 18 | `SumSwitched` | 改投金额(元) | number(19,4) | ✓ | 1.02% |  |
| 19 | `SwitchedRemark` | 改投说明 | varchar2(2000) | ✓ | 19.62% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，取“上市板块(ListedSector)”=7-科创板，得到证券的交易代码、简称等。

### RaisingMethod (募资方式)

募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令 LB = 1021 AND DM NOT IN (19,20,21,22,14,23)，得到募资方式的具体描述：1-新股发行，2-历史遗留，3-增发新股，4-配股，5-发行可转换债券，6-发行企业债券，7-募资改投，8-非募集资金，9-发行权证，10-吸收合并，11-发行分离可转债，12-发行金融债，13-老股转让，15-CDR首发，16-CDR增发，17-CDR配股，31-预先披露，32-优先股发行，33-地方政府债发行，34-后续发行，99-其他。

### RaisingPurpose (募资用途)

募资用途(RaisingPurpose)与(CT_SystemConst)表中的DM字段关联，令LB = 2208，得到募资用途的具体描述：1-投资主营业务项目，2-投资新项目，3-项目前期投入，4-补充流动资金，5-补充募投项目资金缺口，6-购买银行理财产品，7-进行现金管理，8-偿还银行贷款，9-偿还非银行有息负债，10-向子公司增资，11-设立公司或分支机构，12-购置研发设备，13-购买土地及土地使用权，14-收购兼并，15-支付现金对价。

### IfSwitched (改投与否)

改投与否(IfSwitched)与(CT_SystemConst)表中的DM字段关联，令LB = 1219，得到改投与否的具体描述：1-否，2-全部改投，3-部分改投。

## SQL示例

```sql
-- 查询 科创板资金投向说明 数据
SELECT *
FROM lc_stibcapitalinvest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
