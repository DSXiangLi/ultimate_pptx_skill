# HK_PurchaseAndRedeem

**中文名**: 香港基金申赎状态表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_PurchaseAndRedeem` |
| MySQL表名 | `hk_purchaseandredeem` |
| 中文名 | 香港基金申赎状态表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 30 |
| 版本 | 1 |

## 表描述

1.本表记录不同对象、场所、渠道组合下的香港互认基金的认购期、封闭期、申购、大额申购、赎回、终止状态。
2.历史数据：2016年起-至今。
3.信息来源：证监会官网，基金公司官网。
表数据更新频率： 日更新

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `ApplyingTypeI` | 个人场内申购状态 | varchar2(100) | ✓ | 0.0% |  |
| 5 | `RedeemTypeI` | 个人场内赎回状态 | varchar2(100) | ✓ | 0.0% |  |
| 6 | `ApplyingMaxI` | 个人场内单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 7 | `ApplyingTypeII` | 个人场外直销柜台申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `RedeemTypeII` | 个人场外直销柜台赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `ApplyingMaxII` | 个人场外直销柜台单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 10 | `ApplyingTypeIII` | 个人场外直销网上申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `RedeemTypeIII` | 个人场外直销网上赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `ApplyingMaxIII` | 个人场外直销网上单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 13 | `ApplyingTypeIV` | 个人场外代销申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `RedeemTypeIV` | 个人场外代销赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 15 | `ApplyingMaxIV` | 个人场外代销单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 16 | `ApplyingTypeV` | 机构场内申购状态 | varchar2(100) | ✓ | 0.0% |  |
| 17 | `RedeemTypeV` | 机构场内赎回状态 | varchar2(100) | ✓ | 0.0% |  |
| 18 | `ApplyingMaxV` | 机构场内单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 19 | `ApplyingTypeVI` | 机构场外直销柜台申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 20 | `RedeemTypeVI` | 机构场外直销柜台赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 21 | `ApplyingMaxVI` | 机构场外直销柜台单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 22 | `ApplyingTypeVII` | 机构场外直销网上申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 23 | `RedeemTypeVII` | 机构场外直销网上赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 24 | `ApplyingMaxVII` | 机构场外直销网上单日申购上限 | number(19,2) | ✓ | 0.0% |  |
| 25 | `ApplyingTypeVIII` | 机构场外代销申购状态 | varchar2(100) | ✓ | 100.0% |  |
| 26 | `RedeemTypeVIII` | 机构场外代销赎回状态 | varchar2(100) | ✓ | 100.0% |  |
| 27 | `ApplyingMaxVIII` | 机构场外代销单日申购上限 | number(19,2) | ✓ | 0.38% |  |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 30 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 香港基金申赎状态表 数据
SELECT *
FROM hk_purchaseandredeem
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
