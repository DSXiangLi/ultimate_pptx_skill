# HK_RaiseFundsInvest

**中文名**: 港股募集资金投向表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_RaiseFundsInvest` |
| MySQL表名 | `hk_raisefundsinvest` |
| 中文名 | 港股募集资金投向表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.02 |

## 表描述

1.内容说明：新建港股募集资金投向，记录港股发行筹资资金的使用情况。
2.数据范围：2016-06-30至今。
3.信息来源：港交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `IssueType` | 发行类别 | number(10) | ✗ | 100.0% | 发行类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1329，得到发行类别的... |
| 5 | `EventNumber` | 事项编号 | number(10) | ✓ | 100.0% |  |
| 6 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AN... |
| 7 | `ProjectName` | 募集投向项目名称 | varchar2(200) | ✗ | 100.0% |  |
| 8 | `RefIssuePrice` | 参考发行价类型 | number(10) | ✓ | 100.0% | 参考发行价类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 2151，得到参考... |
| 9 | `PInvRaiFCeiling` | 计划投入募集资金上限 | number(18,2) | ✓ | 99.56% |  |
| 10 | `PInvRaiFFloor` | 计划投入募集资金下限 | number(18,2) | ✓ | 99.17% |  |
| 11 | `PInvRaiFRatio` | 计划投入募集资金占比(%) | number(18,6) | ✓ | 99.41% |  |
| 12 | `ActInvRaiFunds` | 实际投入募集资金 | number(18,2) | ✓ | 88.26% |  |
| 13 | `ActInvRaiFRatio` | 实际投入募集资金占比(%) | number(18,6) | ✓ | 87.97% |  |
| 14 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=... |
| 15 | `ConAmount` | 换算金额 | number(18,2) | ✓ | 8.5% |  |
| 16 | `ConCurrency` | 换算币种 | number(10) | ✓ | 8.5% | 换算币种（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=... |
| 17 | `RecPurposes` | 募集目的 | varchar2(2000) | ✓ | 100.0% |  |
| 18 | `IFSchemeChange` | 是否变更 | number(10) | ✓ | 100.0% | 是否变更（IFSchemeChange）：1-是，2-否。 |
| 19 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.61% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### IssueType (发行类别)

发行类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1329，得到发行类别的具体描述：1-首发，3-增发，9-股东转让配售，10-基金营销。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1000,1001,1004,1007,1016,1022,3121,3125,3131,3304)，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1016-未实施终止，1022-实施完成，3121-股东大会通过，3125-股东大会否决，3131-方案实施，3304-提前终止。

### RefIssuePrice (参考发行价类型)

参考发行价类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 2151，得到参考发行价类型的具体描述：10-发行最高最低价，20-发行中间价，30-配售价。

### CurrencyUnit (货币单位)

货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“货币单位”的描述。 
       1000-美元，1100-港元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元

### ConCurrency (换算币种)

换算币种（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“换算币种”的描述。 
       1000-美元，1100-港元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元

### IFSchemeChange (是否变更)

是否变更（IFSchemeChange）：1-是，2-否。

## SQL示例

```sql
-- 查询 港股募集资金投向表 数据
SELECT *
FROM hk_raisefundsinvest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
