# HK_StoDiscDerRights

**中文名**: 港股披露衍生权益

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_StoDiscDerRights` |
| MySQL表名 | `hk_stodiscderrights` |
| 中文名 | 港股披露衍生权益 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.07 |

## 表描述

1.记录港股披露权益持有人持有衍生权益的进一步信息，包含内容有：持仓类型、切合身份、行权日期、行权价格、转让价格、授予价格、股份数目等。该表为港股披露权益系列表的附表之一。
2.数据范围：1997年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联 |
| 3 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到持仓... |
| 4 | `HoldStatus` | 切合身份 | number(10) | ✗ | 100.0% | 切合身份（HoldStatus）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=... |
| 5 | `EDay` | 行权起始日 | date | ✓ | 36.53% |  |
| 6 | `EndDateOfExercise` | 行权截止日 | date | ✓ | 35.74% |  |
| 7 | `ExerCurrencyUnit` | 行权价格货币单位 | number(10) | ✓ | 11.15% |  |
| 8 | `ExercisePrice` | 行权价格(元) | number(18,9) | ✓ | 32.1% |  |
| 9 | `TransCurrencyUnit` | 转让价格货币单位 | number(10) | ✓ | 1.23% |  |
| 10 | `TransferPrice` | 转让价格(元) | number(18,9) | ✓ | 3.79% |  |
| 11 | `GrantCurrencyUnit` | 授予价格货币单位 | number(10) | ✓ | 9.63% |  |
| 12 | `GrantPrice` | 授予价格(元) | number(18,9) | ✓ | 27.2% |  |
| 13 | `ShareAmount` | 股份数目(股) | number(19) | ✓ | 99.88% |  |
| 14 | `NumberOfExer` | 行权次数 | number(10) | ✓ | 100.0% |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联

### PosCharacter (持仓类型)

持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。

### HoldStatus (切合身份)

切合身份（HoldStatus）与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1701”，得到切合身份的具体描述。因港交所网页内容做过优化，在2017年7月3日前后使用的权益身份编码不一致。其中：2017年7月3日前，201-实益拥有人，202-投资经理，203-对股分持有保证权益的人，204-你未满18岁的子女或配偶的权益等；2017年7月3日后，2101-实益拥有人，2102-投资经理，2106-持有股份的保证权益的人，2203-你未满18岁的子女或配偶的权益等。

## SQL示例

```sql
-- 查询 港股披露衍生权益 数据
SELECT *
FROM hk_stodiscderrights
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
