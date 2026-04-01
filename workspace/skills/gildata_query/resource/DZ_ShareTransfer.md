# DZ_ShareTransfer

**中文名**: 股东股权变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_ShareTransfer` |
| MySQL表名 | `dz_sharetransfer` |
| 中文名 | 股东股权变动 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股东股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 50 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录 上市公司股东股权转让、二级市场买卖、股权拍卖、股东重组等引起股东股权变动方面的明细资料。
2.数据范围：1996-01-26至今
3.信息来源：上交所和深交所大宗交易公开信息、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `ContractSignDate` | 股权转让协议签署日 | date | ✓ | 0.95% |  |
| 8 | `ApprovedDate` | 转让批准日期 | date | ✓ | 0.18% |  |
| 9 | `TranStartDate` | 股权变动起始日 | date | ✓ | 99.32% |  |
| 10 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 11 | `TranDate` | 股权正式变动日期/过户日期 | date | ✓ | 99.32% |  |
| 12 | `TransfererName` | 股权出让方名称 | varchar2(100) | ✓ | 82.91% |  |
| 13 | `TransfererAttribute` | 股权出让方所属性质 | number(10) | ✓ | 82.92% | 股权出让方所属性质(TransfererAttribute)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 14 | `TransfererCode` | 股权出让方编码 | number(10) | ✓ | 52.05% |  |
| 15 | `TansfererEcoNature` | 股权出让方经济性质 | number(10) | ✓ | 82.69% | 股权出让方经济性质(TansfererEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 16 | `TranShareType` | 出让股权性质 | number(10) | ✓ | 70.91% | 出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得... |
| 17 | `SumBeforeTran` | 出让前持股数量(股/份) | number(16,0) | ✓ | 18.7% |  |
| 18 | `PCTBeforeTran` | 出让前持股比例 | number(19,8) | ✓ | 18.7% |  |
| 19 | `SNBeforeTran` | 出让前股东序号 | number(10) | ✓ | 18.7% |  |
| 20 | `SumAfterTran` | 出让后持股数量(股/份) | number(16,0) | ✓ | 18.69% |  |
| 21 | `ResSumAfterTran` | 其中:出让后有限售股数(股/份) | number(16,0) | ✓ | 4.91% |  |
| 22 | `NonResSumAfterTran` | 其中:出让后无限售股数(股/份) | number(16,0) | ✓ | 14.58% |  |
| 23 | `PCTAfterTran` | 出让后持股比例 | number(19,8) | ✓ | 18.47% |  |
| 24 | `SNAfterTran` | 出让后股东序号 | number(10) | ✓ | 16.4% |  |
| 25 | `ReceiverName` | 股权受让方名称 | varchar2(100) | ✓ | 74.18% |  |
| 26 | `ReceiverAttribute` | 股权受让方所属性质 | number(10) | ✓ | 74.19% | 股权受让方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 27 | `ReceiverCode` | 股权受让方编码 | number(10) | ✓ | 45.38% |  |
| 28 | `ReceiverEcoNature` | 股权受让方经济性质 | number(10) | ✓ | 74.12% |  |
| 29 | `SumBeforeRece` | 受让前持股数量(股/份) | number(16,0) | ✓ | 7.59% |  |
| 30 | `PCTBeforerRece` | 受让前持股比例 | number(19,8) | ✓ | 7.59% |  |
| 31 | `SumAfterRece` | 受让后持股数量(股/份) | number(16,0) | ✓ | 8.37% |  |
| 32 | `ResSumAfterRece` | 其中:受让后有限售股数(股/份) | number(16,0) | ✓ | 1.47% |  |
| 33 | `NonResSumAfterRece` | 其中:受让后无限售股数(股/份 | number(16,0) | ✓ | 6.55% |  |
| 34 | `PCTAfterRece` | 受让后持股比例 | number(19,8) | ✓ | 8.37% |  |
| 35 | `SNAfterRece` | 受让后股东序号 | number(10) | ✓ | 8.39% |  |
| 36 | `TranMode` | 股权转让方式 | number(10) | ✗ | 100.0% | 股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM... |
| 37 | `InvolvedSum` | 涉及股数(股/份) | number(16,0) | ✓ | 100.0% |  |
| 38 | `PCTOfTansferer` | 占出让方原持股数比例 | number(19,8) | ✓ | 18.7% |  |
| 39 | `PCTOfTotalShares` | 占总股本比例 | number(19,8) | ✓ | 39.75% |  |
| 40 | `DealPrice` | 每股/份交易价格(元) | number(19,4) | ✓ | 74.55% |  |
| 41 | `DealTurnover` | 交易金额(元) | number(19,4) | ✓ | 76.0% | 在股权转发让方式为大宗交易(TranMode=11)条件下，当交易金额(DealTurnover)未公布时，根据交易价格... |
| 42 | `ValidCondition` | 生效条件 | varchar2(100) | ✓ | 0.09% |  |
| 43 | `TranStatement` | 事项描述与进展说明 | clob | ✓ | 99.95% |  |
| 44 | `IfSuspended` | 是否终止实施 | number(10) | ✓ | 3.22% | 是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否 |
| 45 | `SuspendedPublDate` | 终止实施公告日期 | date | ✓ | 0.27% |  |
| 46 | `IfSPBlockTradeCode` | 是否专场大宗交易代码 | number(10) | ✓ | 60.25% |  |
| 47 | `IfSPBlockTrade` | 是否专场大宗交易 | varchar2(10) | ✓ | 60.25% |  |
| 48 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 49 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 50 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### TransfererAttribute (股权出让方所属性质)

股权出让方所属性质(TransfererAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3,99)，得到股权出让方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### TansfererEcoNature (股权出让方经济性质)

股权出让方经济性质(TansfererEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1096，得到股权出让方经济性质的具体描述：1-国家单位，2-国有独资，3-国有控股，4-中外合资，5-外资独资，6-民营，7-集体企业，8-自然人，9-其他，10-中央国有企业，11-国有企业，12-地方国有企业，13-其他外资企业，14-其他公司，15-其他证券品种，16-公众企业。

### TranShareType (出让股权性质)

出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得到出让股权性质的具体描述：1-国家股，2-国有法人股，3-外资法人股，4-其他法人股，5-流通A股，6-B股，7-H股，8-转配股，9-专项资产管理计划转让，10-资产支持证券转让，11-中小企业私募债转让，12-中国存托凭证，13-可转换公司债券。

### ReceiverAttribute (股权受让方所属性质)

股权受让方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3,99)，得到股权受让方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### TranMode (股权转让方式)

股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM NOT IN ( 8,51,55,57,98)，得到股权转让方式的具体描述：1-协议转让，2-国有股行政划转或变更，3-执行法院裁定，4-以资抵债，5-二级市场买卖，6-其他-股东重组，7-股东更名，9-其他-要约收购，10-以股抵债，11-大宗交易(席位)，12-大宗交易，13-其他-ETF换购，14-其他-行权买入，15-集中竞价，16-定向可转债转让，17-集合竞价，18-连续竞价，19-做市，20-询价转让，21-赠与，22-继承，24-间接方式转让，53-股改后间接股东增持，56-交易所集中交易，59-股权激励，70-国有股转持，71-老股转让，80-司法拍卖，99-其他。

### DealTurnover (交易金额(元))

在股权转发让方式为大宗交易(TranMode=11)条件下，当交易金额(DealTurnover)未公布时，根据交易价格(DealPrice)与涉及股数(InvolvedSum)相乘计算。

### IfSuspended (是否终止实施)

是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 股东股权变动 数据
SELECT *
FROM dz_sharetransfer
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
