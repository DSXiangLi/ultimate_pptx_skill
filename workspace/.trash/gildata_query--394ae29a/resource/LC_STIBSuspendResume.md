# LC_STIBSuspendResume

**中文名**: 科创板停复牌

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSuspendResume` |
| MySQL表名 | `lc_stibsuspendresume` |
| 中文名 | 科创板停复牌 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上海交易所披露科创板停牌复牌信息及科创板上市公司临时公告信息，如停牌日期、停牌时间、停牌事项说明、停牌期限、复牌日期、复牌时间等，包括盘中临时停牌。
2.数据范围：科创板上市起-至今
3.信息来源：上海证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 5 | `SuspendResumpType` | 停复牌类型 | number(10) | ✗ | 100.0% | 1: 停牌     2: 复牌 |
| 6 | `SuspendResumpDate` | 停复牌日期 | date | ✗ | 100.0% |  |
| 7 | `SuspendResumpTime` | 停复牌时间 | varchar2(30) | ✗ | 100.0% |  |
| 8 | `SuspendStatement` | 停牌事项说明 | varchar2(200) | ✓ | 50.2% |  |
| 9 | `SuspendCode` | 停牌事项编码 | number(10) | ✓ | 50.2% | 停牌事项编码(SuspendCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1654，得到停... |
| 10 | `SuspendTerm` | 停牌期限 | varchar2(100) | ✓ | 50.2% |  |
| 11 | `AID` | 公告ID | number(19) | ✓ | 0.0% |  |
| 12 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM = 83，得到信息来源的具体描述：83-上海证券交易所。

### SuspendResumpType (停复牌类型)

1: 停牌     2: 复牌

### SuspendCode (停牌事项编码)

停牌事项编码(SuspendCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1654，得到停牌事项编码的具体描述：101-临时停牌，102-召开股东大会，103-重大事项，104-其它公告（停牌），105-交易异常波动，106-澄清公告，107-撤销其他特别处理公告，108-盘中临时停牌，109-撤销退市风险警示公告，110-未能如期刊登股东大会决议，111-增发提示性公告，112-续发行招投标，113-股价异动停牌公告，114-份额暂停交易公告，115-交易风险提示，116-收益分配，117-实行退市风险警示公告，118-实行其他特别处理公告，119-未按期披露定期报告，120-破产，121-拟终止挂牌，122-做市商不足2家，123-转板上市，603-刊登重要公告，604-拟筹划重大资产重组，605-重要事项未公告，606-未刊登股东大会决议公告，607-刊登股票交易异常波动公告，608-媒体报道需澄清，610-基金公司申请，611-定价增发，612-正股停牌，999-其他特别原因。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 科创板停复牌 数据
SELECT *
FROM lc_stibsuspendresume
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
