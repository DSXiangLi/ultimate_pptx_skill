# HK_CStoneInvestor

**中文名**: 港股基石投资者

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CStoneInvestor` |
| MySQL表名 | `hk_cstoneinvestor` |
| 中文名 | 港股基石投资者 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.02 |

## 表描述

1.新建港股基石投资者表，记录港股新股发行中的基石投资者信息。
2.历史数据：2010年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `CStoneInvName` | 基础投资者名称 | varchar2(200) | ✗ | 100.0% |  |
| 5 | `CStoneInvCode` | 基础投资者公司代码 | number(10) | ✓ | 85.36% | 基础投资者公司代码（CStoneInvCode）：与“港股企业概况（HK_CompanyArchives）”中的“公司代... |
| 6 | `CStoneInvConName` | 基础投资者实际控制人 | varchar2(200) | ✓ | 75.94% |  |
| 7 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=... |
| 8 | `SubscribeValue` | 认购金额(元) | number(18,2) | ✓ | 96.67% |  |
| 9 | `TotalNumSubCeiling` | 认购股数上限(股) | number(18,2) | ✓ | 83.09% |  |
| 10 | `TotalNumSubMedian` | 认购股数中位数(股) | number(18,2) | ✓ | 94.52% |  |
| 11 | `TotalNumSubFloor` | 认购股数下限(股) | number(18,2) | ✓ | 83.8% |  |
| 12 | `GlobalSalesRatioP` | 预计全球发售比例(%) | number(18,8) | ✓ | 99.88% |  |
| 13 | `IssuedCapitalRatioP` | 预计已发行股本比例(%) | number(18,8) | ✓ | 99.88% |  |
| 14 | `TotalNumSubActual` | 实际认购总股数(股) | number(18,2) | ✓ | 96.49% |  |
| 15 | `GlobalSalesRatio` | 全球发售比例(%) | number(18,8) | ✓ | 91.61% |  |
| 16 | `IssuedCapitalRatio` | 已发行股本比例(%) | number(18,8) | ✓ | 92.11% |  |
| 17 | `LimitSalePeriod` | 限售期 | number(10) | ✓ | 100.0% | 限售期(LimitSalePeriod)与(CT_SystemConst)表中的DM字段关联，令LB=2000，得到限售... |
| 18 | `RestrictedEndDate` | 限售截止日 | date | ✓ | 99.44% |  |
| 19 | `Precondition` | 先决条件 | varchar2(2000) | ✓ | 98.17% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### CStoneInvCode (基础投资者公司代码)

基础投资者公司代码（CStoneInvCode）：与“港股企业概况（HK_CompanyArchives）”中的“公司代码 （CompanyCode）”关联，得到企业的基本信息。

### CurrencyUnit (货币单位)

货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“货币单位”的描述。 
       1000-美元，1100-港元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元

### LimitSalePeriod (限售期)

限售期(LimitSalePeriod)与(CT_SystemConst)表中的DM字段关联，令LB=2000，得到限售期的具体描述：1-3个月，2-6个月，3-9个月，4-12个月，5-15个月，6-18个月，7-2个月，8-4个月，9-5个月，10-7个月，11-8个月，12-10个月，13-11个月，14-14个月，15-16个月，16-17个月，17-24个月，18-30个月，19-36个月，20-42个月，21-48个月，22-54个月，23-60个月，99-其他。

## SQL示例

```sql
-- 查询 港股基石投资者 数据
SELECT *
FROM hk_cstoneinvestor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
