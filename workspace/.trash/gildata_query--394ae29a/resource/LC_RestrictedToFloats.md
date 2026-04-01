# LC_RestrictedToFloats

**中文名**: 限售股票解禁明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_RestrictedToFloats` |
| MySQL表名 | `lc_restrictedtofloats` |
| 中文名 | 限售股票解禁明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 43 |
| 版本 | 1.07 |

## 表描述

1.收录上市公司股东历次限售股票解禁明细，包括流通起始日、股东名称、股东持股总数、新增可售A股、新增可售B股、股本变动原因等指标。
2.数据范围：2006-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `RestrictedDate` | 限售起始日期 | date | ✓ | 71.56% |  |
| 7 | `EstimateActual` | 解禁日期类型(预计\实际) | number(10) | ✓ | 100.0% | 解禁日期类型(预计\实际) （EstimateActual）：该字段固定以下常量：1-预计 ；2-实际 |
| 8 | `EndDate` | 截止日期(流通起始日) | date | ✓ | 100.0% | 截止日期(流通起始日)（EndDate）：当【EstimateActual】=1时，【EndDate】为“预计解禁日期”... |
| 9 | `LimitSalePeriod` | 限售期(月) | number(19,4) | ✓ | 71.51% |  |
| 10 | `InfoType` | 信息类别 | number(10) | ✓ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM I... |
| 11 | `SHSN` | 股东序号 | number(10) | ✓ | 100.0% |  |
| 12 | `SHName` | 股东名称 | varchar2(200) | ✓ | 100.0% |  |
| 13 | `SHAttribute` | 股东属性 | number(10) | ✓ | 98.38% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and D... |
| 14 | `CompanyNumber` | 企业编号 | number(10) | ✓ | 69.33% | 当股东属性(SHAttribute)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(Company... |
| 15 | `Afloats` | 流通A股(股) | number(18,2) | ✓ | 100.0% |  |
| 16 | `AFloatListed` | 无限售流通A股(股) | number(18,2) | ✓ | 100.0% |  |
| 17 | `ManagementShares` | 高管股(股) | number(18,2) | ✓ | 0.0% |  |
| 18 | `RestrictedAFloatShares` | 有限售流通A股(股) | number(18,2) | ✓ | 89.98% |  |
| 19 | `RestrinctStaffShares` | 有限售职工股(股) | number(18,2) | ✓ | 0.0% |  |
| 20 | `Bshares` | B股(股) | number(18,2) | ✓ | 0.0% |  |
| 21 | `RestrictedBFloatShares` | 有限售B股(股) | number(18,2) | ✓ | 0.0% |  |
| 22 | `Hshares` | H股(股) | number(18,2) | ✓ | 0.0% |  |
| 23 | `OtherFloatShares` | 其他流通股(股) | number(18,2) | ✓ | 0.0% |  |
| 24 | `Sshares` | S股(股) | number(18,2) | ✓ | 0.0% |  |
| 25 | `Nshares` | N股(股) | number(18,2) | ✓ | 0.0% |  |
| 26 | `HoldSum` | 股东持股总数(股) | number(18,2) | ✓ | 100.0% |  |
| 27 | `NewAFloatListed` | 新增可售A股(股) | number(18,2) | ✓ | 100.0% |  |
| 28 | `NewBFloatListed` | 新增可售B股(股) | number(18,2) | ✓ | 0.01% |  |
| 29 | `ActualFloatListedSH` | 实际上市流通数量(股) | number(18,2) | ✓ | 36.82% |  |
| 30 | `ActionWays` | 解禁行为 | number(10) | ✓ | 63.82% | 解禁行为(ActionWays)与(CT_SystemConst)表中的DM字段关联，令LB = 2371 AND DM... |
| 31 | `FloatsNum` | 流通数量(份) | number(18,2) | ✓ | 0.0% |  |
| 32 | `FloatListedNum` | 无限售流通数量(份) | number(18,2) | ✓ | 0.0% |  |
| 33 | `RestrictedSharesNum` | 有限售流通数量(份) | number(18,2) | ✓ | 0.0% |  |
| 34 | `HoldShareNum` | 股东持股总数(份 | number(18,2) | ✓ | 0.0% |  |
| 35 | `NewAFloatListedNum` | 新增可售数量(份) | number(18,2) | ✓ | 0.0% |  |
| 36 | `ActualFloatListedNum` | 实际上市流通数量(份) | number(18,2) | ✓ | 0.0% |  |
| 37 | `ChangeType` | 股本变动原因类别 | number(10) | ✓ | 100.0% | 股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AN... |
| 38 | `ChangeReason` | 股本变动原因说明 | varchar2(200) | ✓ | 99.98% |  |
| 39 | `RestrictedCondition` | 限售条件说明 | clob | ✓ | 91.5% |  |
| 40 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效（IfEffected）：该字段固定以下常量：1-是，3-已失效（预计的数据值在实际解除后会标识为已失效）。 |
| 41 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 42 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 43 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### EstimateActual (解禁日期类型(预计\实际))

解禁日期类型(预计\实际) （EstimateActual）：该字段固定以下常量：1-预计 ；2-实际

### EndDate (截止日期(流通起始日))

截止日期(流通起始日)（EndDate）：当【EstimateActual】=1时，【EndDate】为“预计解禁日期”；当【EstimateActual】=2时，【EndDate】为“实际解禁日期”。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM IN (10,11)，得到信息类别的具体描述：10-有限售股份，11-有限售股东。

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3)，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种。

### CompanyNumber (企业编号)

当股东属性(SHAttribute)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当股东属性(SHAttribute)=2时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### ActionWays (解禁行为)

解禁行为(ActionWays)与(CT_SystemConst)表中的DM字段关联，令LB = 2371 AND DM NOT IN (20)，得到解禁行为的具体描述：10-到期解禁，21-业绩补偿(被动解禁)，22-司法拍卖(被动解禁)，23-被动解禁(其他)。

### ChangeType (股本变动原因类别)

股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM IN ('4','24','25','45','47','51','73','75','78','79','80','81','82','83','90')，得到股本变动原因类别的具体描述：4-A股发行法人配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，45-职工股上市，47-外资法人股上市，51-其他，73-股权分置股份追送，75-股权分置限售流通，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，90-延长限售锁定期流通。

### IfEffected (是否有效)

是否有效（IfEffected）：该字段固定以下常量：1-是，3-已失效（预计的数据值在实际解除后会标识为已失效）。

## SQL示例

```sql
-- 查询 限售股票解禁明细 数据
SELECT *
FROM lc_restrictedtofloats
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
