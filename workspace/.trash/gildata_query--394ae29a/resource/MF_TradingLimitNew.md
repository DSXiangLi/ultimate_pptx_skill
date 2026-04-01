# MF_TradingLimitNew

**中文名**: 公募基金交易限额表(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_TradingLimitNew` |
| MySQL表名 | `mf_tradinglimitnew` |
| 中文名 | 公募基金交易限额表(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录基金交易限额数据，包括认购、定投、申赎、转入转出的最低金额，份额、级差等
2.数据范围：2022年9月起-至今
3.信息来源：基金公司官网披露的产品说明书、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `LimitType` | 限额类型 | number(10) | ✗ | 100.0% | 限额类型(LimitType)与(CT_SystemConst)表中的DM字段关联，令LB = 2514，得到限额类型的... |
| 4 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `ExpireDate` | 取消日期 | date | ✓ | 23.23% |  |
| 6 | `AppliMarket` | 适用市场 | number(10) | ✗ | 100.0% | 适用市场(AppliMarket)与(CT_SystemConst)表中的DM字段关联，令LB= 1652，得到适用市场... |
| 7 | `AppliObject` | 适用对象 | number(10) | ✗ | 100.0% | 适用对象(AppliObject)与(CT_SystemConst)表中的DM字段关联，令LB= 1608 AND DM... |
| 8 | `Channel` | 渠道 | number(10) | ✗ | 100.0% | 渠道(Channel)与(CT_SystemConst)表中的DM字段关联，令LB= 2021 AND DM IN  (... |
| 9 | `Unit` | 单位 | number(10) | ✓ | 100.0% | 单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB= 1208 AND DM IN  (7,1... |
| 10 | `Lowerlimit` | 下限 | number(18,4) | ✓ | 98.98% |  |
| 11 | `IfLowboundaryIn` | 下边界是否包含 | number(10) | ✓ | 98.98% | 下边界是否包含(IfLowboundaryIn)与(CT_SystemConst)表中的DM字段关联，令LB= 999 ... |
| 12 | `Upperlimit` | 上限 | number(18,4) | ✓ | 3.01% |  |
| 13 | `IfUpboundaryIn` | 上边界是否包含 | number(10) | ✓ | 2.77% | 上边界是否包含(IfUpboundaryIn)与(CT_SystemConst)表中的DM字段关联，令LB= 999 A... |
| 14 | `Difference` | 级差 | number(18,4) | ✓ | 7.62% |  |
| 15 | `IfEffective` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffective)与(CT_SystemConst)表中的DM字段关联，令LB= 999 AND DM ... |
| 16 | `Remark` | 备注说明 | varchar2(1000) | ✓ | 0.62% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### LimitType (限额类型)

限额类型(LimitType)与(CT_SystemConst)表中的DM字段关联，令LB = 2514，得到限额类型的具体描述：10110-单笔认购，10111-追加单笔认购，10120-累计认购，10210-网上现金单笔认购，10211-网上现金追加单笔认购，10220-网上现金累计认购，10310-网下现金单笔认购，10311-网下现金追加单笔认购，10320-网下现金累计认购，10410-网下证券单笔认购，10411-网下证券追加单笔认购，10412-网下证券单只成份券单笔认购，10420-网下证券累计认购，20110-单笔申购，20111-追加单笔申购，20120-累计申购，30110-单笔赎回，40110-单笔定投，50110-单笔转换转入，50210-单笔转换转出，60110-单笔跨系统转托管，60210-单笔系统内转托管，70100-单一账户持有。

### AppliMarket (适用市场)

适用市场(AppliMarket)与(CT_SystemConst)表中的DM字段关联，令LB= 1652，得到适用市场的具体描述：1-场内，2-场外，3-场内和场外。

### AppliObject (适用对象)

适用对象(AppliObject)与(CT_SystemConst)表中的DM字段关联，令LB= 1608 AND DM IN (1,2,3,4,5)，得到适用对象的具体描述：1-机构，2-个人，3-机构和个人，4-网下投资者，5-公众投资者。

### Channel (渠道)

渠道(Channel)与(CT_SystemConst)表中的DM字段关联，令LB= 2021 AND DM IN  (1,10,11,12,20) ，得到渠道的具体描述：1-全渠道，10-直销，11-直销柜台，12-直销网上，20-代销。

### Unit (单位)

单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB= 1208 AND DM IN  (7,14,15,16,31) OR LB= 102 AND DM IN  (2)，得到单位的具体描述：2-股，7-元，14-美元，15-港元，16-份。

### IfLowboundaryIn (下边界是否包含)

下边界是否包含(IfLowboundaryIn)与(CT_SystemConst)表中的DM字段关联，令LB= 999 AND DM IN  (1,2)，得到下边界是否包含的具体描述：1-是，2-否。

### IfUpboundaryIn (上边界是否包含)

上边界是否包含(IfUpboundaryIn)与(CT_SystemConst)表中的DM字段关联，令LB= 999 AND DM IN  (1,2)，得到上边界是否包含的具体描述：1-是，2-否。

### IfEffective (是否有效)

是否有效(IfEffective)与(CT_SystemConst)表中的DM字段关联，令LB= 999 AND DM IN  (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金交易限额表(新) 数据
SELECT *
FROM mf_tradinglimitnew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
