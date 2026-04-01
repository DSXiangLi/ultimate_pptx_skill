# MF_PurchaseAndRedeemN

**中文名**: 公募基金申赎状态(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PurchaseAndRedeemN` |
| MySQL表名 | `mf_purchaseandredeemn` |
| 中文名 | 公募基金申赎状态(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 30 |
| 版本 | 1 |

## 表描述

1.本表记录不同对象、场所、渠道组合下的基金的认购期、封闭期、申购、大额申购、赎回、终止状态。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书及相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `ApplyingTypeI` | 个人场内申购状态 | varchar2(100) | ✓ | 10.72% |  |
| 5 | `RedeemTypeI` | 个人场内赎回状态 | varchar2(100) | ✓ | 10.72% |  |
| 6 | `ApplyingMaxI` | 个人场内单日申购上限 | number(19,2) | ✓ | 0.71% |  |
| 7 | `ApplyingTypeII` | 个人场外直销柜台申购状态 | varchar2(100) | ✓ | 93.43% |  |
| 8 | `RedeemTypeII` | 个人场外直销柜台赎回状态 | varchar2(100) | ✓ | 93.44% |  |
| 9 | `ApplyingMaxII` | 个人场外直销柜台单日申购上限 | number(19,2) | ✓ | 13.37% |  |
| 10 | `ApplyingTypeIII` | 个人场外直销网上申购状态 | varchar2(100) | ✓ | 93.43% |  |
| 11 | `RedeemTypeIII` | 个人场外直销网上赎回状态 | varchar2(100) | ✓ | 93.44% |  |
| 12 | `ApplyingMaxIII` | 个人场外直销网上单日申购上限 | number(19,2) | ✓ | 13.23% |  |
| 13 | `ApplyingTypeIV` | 个人场外代销申购状态 | varchar2(100) | ✓ | 93.43% |  |
| 14 | `RedeemTypeIV` | 个人场外代销赎回状态 | varchar2(100) | ✓ | 93.44% |  |
| 15 | `ApplyingMaxIV` | 个人场外代销单日申购上限 | number(19,2) | ✓ | 13.91% |  |
| 16 | `ApplyingTypeV` | 机构场内申购状态 | varchar2(100) | ✓ | 10.72% |  |
| 17 | `RedeemTypeV` | 机构场内赎回状态 | varchar2(100) | ✓ | 10.72% |  |
| 18 | `ApplyingMaxV` | 机构场内单日申购上限 | number(19,2) | ✓ | 0.71% |  |
| 19 | `ApplyingTypeVI` | 机构场外直销柜台申购状态 | varchar2(100) | ✓ | 95.52% |  |
| 20 | `RedeemTypeVI` | 机构场外直销柜台赎回状态 | varchar2(100) | ✓ | 95.52% |  |
| 21 | `ApplyingMaxVI` | 机构场外直销柜台单日申购上限 | number(19,2) | ✓ | 14.86% |  |
| 22 | `ApplyingTypeVII` | 机构场外直销网上申购状态 | varchar2(100) | ✓ | 95.51% |  |
| 23 | `RedeemTypeVII` | 机构场外直销网上赎回状态 | varchar2(100) | ✓ | 95.52% |  |
| 24 | `ApplyingMaxVII` | 机构场外直销网上单日申购上限 | number(19,2) | ✓ | 14.23% |  |
| 25 | `ApplyingTypeVIII` | 机构场外代销申购状态 | varchar2(100) | ✓ | 95.51% |  |
| 26 | `RedeemTypeVIII` | 机构场外代销赎回状态 | varchar2(100) | ✓ | 95.52% |  |
| 27 | `ApplyingMaxVIII` | 机构场外代销单日申购上限 | number(19,2) | ✓ | 15.3% |  |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 30 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金申赎状态(新) 数据
SELECT *
FROM mf_purchaseandredeemn
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
