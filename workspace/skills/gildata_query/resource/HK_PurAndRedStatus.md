# HK_PurAndRedStatus

**中文名**: 香港基金销售状态更改

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_PurAndRedStatus` |
| MySQL表名 | `hk_purandredstatus` |
| 中文名 | 香港基金销售状态更改 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.本表记录香港互认基金从对象、场所、渠道等维度申赎状态更改的情况，包括（大额）申购、赎回、（大额）定投、（大额）转换转入等。
2.历史数据：2016年1月起-至今。
3.信息来源：基金公司官网披露的产品说明书及相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% |  |
| 3 | `ChangeDate` | 变更日期 | date | ✗ | 100.0% |  |
| 4 | `ChangeType` | 变更类型 | number(10) | ✗ | 100.0% | 变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB=1184 AND DM I... |
| 5 | `AppliObject` | 适用对象 | number(10) | ✗ | 100.0% | 适用对象(AppliObject)与(CT_SystemConst)表中的DM字段关联，令LB=1608，得到适用对象的... |
| 6 | `ApplyingMarket` | 适用场所 | number(10) | ✗ | 100.0% | 适用场所(ApplyingMarket)与(CT_SystemConst)表中的DM字段关联，令LB=1652，得到适用... |
| 7 | `AppliChannel` | 基金适用渠道 | number(10) | ✗ | 100.0% | 基金适用渠道(AppliChannel)与(CT_SystemConst)表中的DM字段关联，令LB=2021 AND ... |
| 8 | `PlatformType` | 平台类型 | number(10) | ✗ | 100.0% | 平台类型(PlatformType)与(CT_SystemConst)表中的DM字段关联，令LB=2457，得到平台类型... |
| 9 | `PlatformName` | 平台名称 | varchar2(1000) | ✓ | 0.11% |  |
| 10 | `LargeApplyingMax` | 变更业务大额上限 | number(19,2) | ✓ | 0.02% |  |
| 11 | `Unit` | 变更业务大额上限单位 | number(10) | ✓ | 0.02% |  |
| 12 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` |  | number(19) | ✗ |  |  |

## 字段说明

### ChangeType (变更类型)

变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB=1184 AND DM IN (13,14,15,16,18,19,52,53,55,56)，得到变更类型的具体描述：13-暂停日常申购(前端)，14-暂停日常赎回，15-恢复日常申购(前端)，16-恢复日常赎回，18-暂停定期定投，19-恢复定期定投，52-暂停转换转入业务，53-恢复转换转入业务，55-暂停转换转出业务，56-恢复转换转出业务。

### AppliObject (适用对象)

适用对象(AppliObject)与(CT_SystemConst)表中的DM字段关联，令LB=1608，得到适用对象的具体描述：1-机构，2-个人，3-机构和个人，4-网下投资者，5-公众投资者，6-网上现金，7-网下现金，8-网下证券，9-战略投资者。

### ApplyingMarket (适用场所)

适用场所(ApplyingMarket)与(CT_SystemConst)表中的DM字段关联，令LB=1652，得到适用场所的具体描述：1-场内，2-场外，3-场内和场外。

### AppliChannel (基金适用渠道)

基金适用渠道(AppliChannel)与(CT_SystemConst)表中的DM字段关联，令LB=2021 AND DM IN (1,10,11,12,20)，得到基金适用渠道的具体描述：1-全渠道，10-直销，11-直销柜台，12-直销网上，20-代销。

### PlatformType (平台类型)

平台类型(PlatformType)与(CT_SystemConst)表中的DM字段关联，令LB=2457，得到平台类型的具体描述：1-全平台，2-特殊平台。

## SQL示例

```sql
-- 查询 香港基金销售状态更改 数据
SELECT *
FROM hk_purandredstatus
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
