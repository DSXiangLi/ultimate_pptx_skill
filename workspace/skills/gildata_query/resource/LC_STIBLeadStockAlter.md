# LC_STIBLeadStockAlter

**中文名**: 科创板高管及相关人员股份变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBLeadStockAlter` |
| MySQL表名 | `lc_stibleadstockalter` |
| 中文名 | 科创板高管及相关人员股份变动 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 人力资源 |
| 更新频率 | 日更新 |
| 字段数量 | 23 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录深沪交易所披露的科创板上市公司领导人及其亲属买卖所在公司股份的情况。
2.数据范围：2019年至今
3.信息来源：交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上... |
| 4 | `AlternationDate` | 变动日期 | date | ✗ | 100.0% |  |
| 5 | `ReportDate` | 填报日期 | date | ✓ | 100.0% |  |
| 6 | `LeaderName` | 领导人姓名 | varchar2(100) | ✗ | 100.0% |  |
| 7 | `PersonalCode` | 人员编码 | number(10) | ✓ | 0.0% |  |
| 8 | `PositionDesc` | 职务描述 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `StockHolder` | 股份变动人姓名 | varchar2(100) | ✗ | 100.0% |  |
| 10 | `ConnectionDesc` | 与领导人关系描述 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `Connection` | 与领导人关系 | number(10) | ✓ | 100.0% | 与领导人关系(Connection)与(CT_SystemConst)表中的DM字段关联，令LB = 1499，得到与领... |
| 12 | `Number` | 变动次数 | number(10) | ✗ | 100.0% |  |
| 13 | `HoldSumBeforAlter` | 变动前持股数(股) | number(19,2) | ✓ | 100.0% |  |
| 14 | `StockSumChanging` | 变动股数(股) | number(19,2) | ✓ | 100.0% |  |
| 15 | `AvgPrice` | 变动均价(元/股) | number(19,4) | ✓ | 99.93% |  |
| 16 | `ChangeProportion` | 变动比例(%) | number(19,8) | ✓ | 100.0% |  |
| 17 | `HoldSumAfterAlter` | 变动后持股数(股) | number(19,2) | ✓ | 100.0% |  |
| 18 | `AlternationReasonDesc` | 变动原因描述 | varchar2(100) | ✓ | 100.0% |  |
| 19 | `AlternationReason` | 变动原因 | number(10) | ✓ | 100.0% | 变动原因(AlternationReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1500... |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |
| 23 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.47% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到科创板上市公司的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

### Connection (与领导人关系)

与领导人关系(Connection)与(CT_SystemConst)表中的DM字段关联，令LB = 1499，得到与领导人关系的具体描述：1-本人，2-父母，3-配偶，4-子女，5-兄弟姐妹，6-受控法人，9-其他，11-上市公司股东的关联人，12-上市公司的关联人。

### AlternationReason (变动原因)

变动原因(AlternationReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1500，得到变动原因的具体描述：11-竞价交易，12-二级市场买卖，21-分红送转，22-老股东配售，23-大宗交易，31-股权激励，32-股改对价，41-新股申购，42-增发配股，51-协议转让，52-盘后定价，53-可转债转股，99-其他，100-股权分置改革，101-配售，102-增发，103-配股，104-送转股，105-个人原因，106-股份回购，200-质押平仓，201-司法转让。

## SQL示例

```sql
-- 查询 科创板高管及相关人员股份变动 数据
SELECT *
FROM lc_stibleadstockalter
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
