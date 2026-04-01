# LC_STIBShareTransfer

**中文名**: 科创板股东股权变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBShareTransfer` |
| MySQL表名 | `lc_stibsharetransfer` |
| 中文名 | 科创板股东股权变动 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 46 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录科创板公司股东股权转让、二级市场买卖、股权拍卖、股东重组等引起股东股权变动方面的明细资料。
2.数据范围：2019年至今
3.信息来源：上交所科创板临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ContractSignDate` | 股权转让协议签署日 | date | ✓ | 0.99% |  |
| 7 | `ApprovedDate` | 转让批准日期 | date | ✓ | 0.03% |  |
| 8 | `TranStartDate` | 股权变动起始日 | date | ✓ | 97.27% |  |
| 9 | `TranDate` | 股权正式变动日期/过户日期 | date | ✓ | 98.73% |  |
| 10 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 11 | `TransfererName` | 股权出让方名称 | varchar2(100) | ✓ | 79.65% |  |
| 12 | `TransfererAttribute` | 股权出让方所属性质 | number(10) | ✓ | 79.65% | 股权出让方所属性质(TransfererAttribute)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 13 | `TransfererCode` | 股权出让方编码 | number(10) | ✓ | 52.76% | 股权出让方编码  (TransfererCode)  :	 当股权出让方所属性质(TransfererAttribute... |
| 14 | `TansfererEcoNature` | 股权出让方经济性质 | number(10) | ✓ | 74.59% | 股权出让方经济性质(TansfererEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 15 | `TranShareType` | 出让股权性质 | number(10) | ✓ | 100.0% | 出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得... |
| 16 | `SumBeforeTran` | 出让前持股数量(股/份) | number(16,0) | ✓ | 70.17% |  |
| 17 | `PCTBeforeTran` | 出让前持股比例(%) | number(19,8) | ✓ | 70.17% |  |
| 18 | `SNBeforeTran` | 出让前股东序号 | number(10) | ✓ | 70.17% |  |
| 19 | `SumAfterTran` | 出让后持股数量(股/份) | number(16,0) | ✓ | 70.17% |  |
| 20 | `ResSumAfterTran` | 其中:出让后有限售股数(股/份) | number(16,0) | ✓ | 0.8% |  |
| 21 | `NonResSumAfterTran` | 其中:出让后无限售股数(股/份) | number(16,0) | ✓ | 57.73% |  |
| 22 | `PCTAfterTran` | 出让后持股比例(%) | number(19,8) | ✓ | 68.54% |  |
| 23 | `SNAfterTran` | 出让后股东序号 | number(10) | ✓ | 64.22% |  |
| 24 | `ReceiverName` | 股权受让方名称 | varchar2(100) | ✓ | 36.37% |  |
| 25 | `ReceiverAttribute` | 股权受让方所属性质 | number(10) | ✓ | 36.37% | 股权受让方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 26 | `ReceiverCode` | 股权受让方编码 | number(10) | ✓ | 13.9% | 股权受让方编码  (ReceiverCode)  : 当股权受让方所属性质(ReceiverAttribute)=2时，... |
| 27 | `ReceiverEcoNature` | 股权受让方经济性质 | number(10) | ✓ | 34.12% | 股权受让方经济性质(ReceiverEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 28 | `SumBeforeRece` | 受让前持股数量(股/份) | number(16,0) | ✓ | 9.41% |  |
| 29 | `PCTBeforerRece` | 受让前持股比例(%) | number(19,8) | ✓ | 9.41% |  |
| 30 | `SumAfterRece` | 受让后持股数量(股/份) | number(16,0) | ✓ | 12.06% |  |
| 31 | `ResSumAfterRece` | 其中:受让后有限售股数(股/份) | number(16,0) | ✓ | 1.36% |  |
| 32 | `NonResSumAfterRece` | 其中:受让后无限售股数(股/份) | number(16,0) | ✓ | 10.09% |  |
| 33 | `PCTAfterRece` | 受让后持股比例(%) | number(19,8) | ✓ | 12.06% |  |
| 34 | `SNAfterRece` | 受让后股东序号 | number(10) | ✓ | 12.21% |  |
| 35 | `TranMode` | 股权转让方式 | number(10) | ✗ | 100.0% | 股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202，得到股权转让... |
| 36 | `InvolvedSum` | 涉及股数(股/份) | number(16,0) | ✓ | 100.0% |  |
| 37 | `PCTOfTansferer` | 占出让方原持股数比例(%) | number(19,8) | ✓ | 70.17% |  |
| 38 | `PCTOfTotalShares` | 占总股本比例(%) | number(19,8) | ✓ | 100.0% |  |
| 39 | `DealPrice` | 每股/份交易价格(元) | number(19,4) | ✓ | 29.49% |  |
| 40 | `DealTurnover` | 交易金额(元) | number(19,4) | ✓ | 41.38% |  |
| 41 | `TranStatement` | 事项描述与进展说明 | clob | ✓ | 100.0% |  |
| 42 | `IfSuspended` | 是否终止实施 | number(10) | ✓ | 0.08% | 是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否 |
| 43 | `SuspendedPublDate` | 终止实施公告日期 | date | ✓ | 0.08% |  |
| 44 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 45 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 46 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### TransfererAttribute (股权出让方所属性质)

股权出让方所属性质(TransfererAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3,99)，得到股权出让方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### TransfererCode (股权出让方编码)

股权出让方编码  (TransfererCode)  :	
当股权出让方所属性质(TransfererAttribute)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当股权出让方所属性质(TransfererAttribute)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息

### TansfererEcoNature (股权出让方经济性质)

股权出让方经济性质(TansfererEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1096，得到股权出让方经济性质的具体描述：1-国家单位，2-国有独资，3-国有控股，4-中外合资，5-外资独资，6-民营，7-集体企业，8-自然人，9-其他，10-中央国有企业，11-国有企业，12-地方国有企业，13-其他外资企业，14-其他公司，15-其他证券品种，16-公众企业。

### TranShareType (出让股权性质)

出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得到出让股权性质的具体描述：1-国家股，2-国有法人股，3-外资法人股，4-其他法人股，5-流通A股，6-B股，7-H股，8-转配股，9-专项资产管理计划转让，10-资产支持证券转让，11-中小企业私募债转让，12-中国存托凭证，13-可转换公司债券。

### ReceiverAttribute (股权受让方所属性质)

股权受让方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3,99)，得到股权受让方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### ReceiverCode (股权受让方编码)

股权受让方编码  (ReceiverCode)  : 当股权受让方所属性质(ReceiverAttribute)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当股权受让方所属性质(ReceiverAttribute)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### ReceiverEcoNature (股权受让方经济性质)

股权受让方经济性质(ReceiverEcoNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1096，得到股权受让方经济性质的具体描述：1-国家单位，2-国有独资，3-国有控股，4-中外合资，5-外资独资，6-民营，7-集体企业，8-自然人，9-其他，10-中央国有企业，11-国有企业，12-地方国有企业，13-其他外资企业，14-其他公司，15-其他证券品种，16-公众企业。

### TranMode (股权转让方式)

股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202，得到股权转让方式的具体描述：1-协议转让，2-国有股行政划转或变更，3-执行法院裁定，4-以资抵债，5-二级市场买卖，6-其他-股东重组，7-股东更名，8-大宗交易，9-其他-要约收购，10-以股抵债，11-大宗交易(席位)，12-大宗交易，13-其他-ETF换购，14-其他-行权买入，15-集中竞价，16-定向可转债转让，17-集合竞价，18-连续竞价，19-做市，20-询价转让，21-赠与，22-继承，24-间接方式转让，51-股改后股东增持，53-股改后间接股东增持，55-股改后高管增持，56-交易所集中交易，57-股改后股东增持股出售，59-股权激励，70-国有股转持，71-老股转让，80-司法拍卖，98-多种交易方式，99-其他。

### IfSuspended (是否终止实施)

是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 科创板股东股权变动 数据
SELECT *
FROM lc_stibsharetransfer
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
