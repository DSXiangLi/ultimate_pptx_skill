# MF_RatioSubscribe

**中文名**: 公募基金比例认购结果

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_RatioSubscribe` |
| MySQL表名 | `mf_ratiosubscribe` |
| 中文名 | 公募基金比例认购结果 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 不定期更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.本表用于记录公募基金比例配售相关信息，包括比例配售方法、配售结果等。
2.数据范围：1998年-至今
3.信息来源：基金发布的比例配售结果公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `RatioSubscribeObject` | 比例配售对象 | number(10) | ✗ | 100.0% | 比例配售对象(RatioSubscribeObject)与(CT_SystemConst)表中的DM字段关联，令LB=1... |
| 5 | `OriginIssueEndDate` | 原定发行截止日 | date | ✓ | 100.0% |  |
| 6 | `ActualIssueEndDate` | 实际发行截止日 | date | ✓ | 96.09% |  |
| 7 | `RatioSubscribeMethod` | 比例配售方法 | number(10) | ✓ | 95.16% | 比例配售方法(RatioSubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2... |
| 8 | `EffSubsApplyAmount` | 有效认购申请金额 | number(20,4) | ✓ | 3.19% |  |
| 9 | `EffSubsAmount` | 有效认购金额 | number(20,4) | ✓ | 2.94% |  |
| 10 | `ConfirmRatio` | 确认比例(%) | number(20,4) | ✓ | 50.98% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RatioSubscribeObject (比例配售对象)

比例配售对象(RatioSubscribeObject)与(CT_SystemConst)表中的DM字段关联，令LB=1608，得到比例配售对象的具体描述：1-机构，2-个人，3-机构和个人，4-网下投资者，5-公众投资者，6-网上现金，7-网下现金，8-网下证券，9-战略投资者。

### RatioSubscribeMethod (比例配售方法)

比例配售方法(RatioSubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2636，得到比例配售方法的具体描述：1-全程比例配售，2-末日比例配售。

## SQL示例

```sql
-- 查询 公募基金比例认购结果 数据
SELECT *
FROM mf_ratiosubscribe
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
