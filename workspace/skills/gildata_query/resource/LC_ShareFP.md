# LC_ShareFP

**中文名**: 股东股权冻结和质押

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ShareFP` |
| MySQL表名 | `lc_sharefp` |
| 中文名 | 股东股权冻结和质押 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 32 |
| 版本 | 1.07 |

## 表描述

1.收录股东股权被冻结和质押及进展情况，包括被冻结质押股东、被接受股权质押方、涉及股数以及冻结质押期限起始和截止日等内容。
2.数据范围：1999-09-30至今
3.信息来源：股权质押公告、股权冻结公告、解除质押冻结公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `TypeSelect` | 类别选择 | number(10) | ✓ | 100.0% | 类别选择(TypeSelect)与(CT_SystemConst)表中的DM字段关联，令LB = 1201 AND DM... |
| 7 | `FPSHName` | 股权被冻结质押股东名称 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `SHAttribute` | 股权被冻结质押股东所属性质 | number(10) | ✓ | 99.96% | 股权被冻结质押股东所属性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 9 | `SHID` | 股权被冻结质押股东ID | number(10) | ✓ | 52.41% | 股权被冻结质押股东ID(SHID)：当股权被冻结质押股东所属性质(SHAttribute)=2时，与企业码表（EP_Co... |
| 10 | `SHSN` | 股权被冻结质押股东序号 | number(10) | ✓ | 98.32% |  |
| 11 | `ReceiverName` | 接受股权质押方 | varchar2(100) | ✓ | 88.78% |  |
| 12 | `ReceiverAttribute` | 接受股权质押方所属性质 | number(10) | ✓ | 88.78% | 接受股权质押方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 13 | `ReceiverID` | 接受股权质押方ID | number(10) | ✓ | 86.67% | 接受股权质押方ID(ReceiverID)：当接受股权质押方所属性质(ReceiverAttribute)=2时，与企业... |
| 14 | `InvolvedSum` | 涉及股数(股) | number(16,0) | ✓ | 100.0% |  |
| 15 | `InitialPledgeSum` | 初始质押股数(股) | number(19,2) | ✓ | 98.7% |  |
| 16 | `UnstintedTShare` | 其中:无限售股数(股) | number(19) | ✓ | 14.06% |  |
| 17 | `RestrainedTShare` | 其中:有限售股数(股) | number(19) | ✓ | 3.27% |  |
| 18 | `PCTOfPledger` | 占冻结质押方持股数比例 | number(9,6) | ✓ | 99.55% |  |
| 19 | `PCTOfTotalShares` | 占总股本比例 | number(9,6) | ✓ | 100.0% |  |
| 20 | `RPPCTOfPledger` | 解押股数占冻结质押方持股数比例 | number(9,6) | ✓ | 75.42% |  |
| 21 | `RPPCTOfTotalShares` | 解押股数占总股本比例 | number(9,6) | ✓ | 75.43% |  |
| 22 | `FPReason` | 股权冻结质押原因 | varchar2(255) | ✓ | 68.16% |  |
| 23 | `StartDate` | 冻结质押期限起始日 | date | ✓ | 98.28% |  |
| 24 | `EndDate` | 冻结质押期限截止日 | date | ✓ | 76.9% |  |
| 25 | `EstimateReleaseDate` | 预计解押日期 | date | ✓ | 52.19% |  |
| 26 | `Statement` | 事项描述与进展说明 | clob | ✓ | 0.69% |  |
| 27 | `EventCode` | 事项编码 | varchar2(12) | ✓ | 100.0% |  |
| 28 | `EventDate` | 事项日期 | date | ✓ | 100.0% |  |
| 29 | `CompletelyRelease` | 是否完全解押 | number(10) | ✓ | 89.23% |  |
| 30 | `IFSupplyPledge` | 是否为补充质押 | number(10) | ✓ | 89.23% |  |
| 31 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### TypeSelect (类别选择)

类别选择(TypeSelect)与(CT_SystemConst)表中的DM字段关联，令LB = 1201 AND DM IN (2,3,5)，得到类别选择的具体描述：2-股权冻结，3-股权质押，5-股票质押式回购。

### SHAttribute (股权被冻结质押股东所属性质)

股权被冻结质押股东所属性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM IN (1,2,3,99)，得到股权被冻结质押股东所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHID (股权被冻结质押股东ID)

股权被冻结质押股东ID(SHID)：当股权被冻结质押股东所属性质(SHAttribute)=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联

### ReceiverAttribute (接受股权质押方所属性质)

接受股权质押方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM IN (1,2,3,99)，得到接受股权质押方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### ReceiverID (接受股权质押方ID)

接受股权质押方ID(ReceiverID)：当接受股权质押方所属性质(ReceiverAttribute)=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联

## SQL示例

```sql
-- 查询 股东股权冻结和质押 数据
SELECT *
FROM lc_sharefp
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
