# MF_REITsAddOffering

**中文名**: 基础设施基金(REITs)扩募信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsAddOffering` |
| MySQL表名 | `mf_reitsaddoffering` |
| 中文名 | 基础设施基金(REITs)扩募信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 不定期更新 |
| 字段数量 | 32 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录基础设施基金(REITs)扩募信息，包括：扩募发售价格、金额、不同投资者配售份额、扩募份额上市日期等信息
2.数据范围：2023年6月至今
3.信息来源：基金扩募相关公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `AddOfferingTimes` | 扩募次数 | number(10) | ✗ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `AddOfferingMethod` | 扩募方式 | number(10) | ✓ | 100.0% | 扩募方式(AddOfferingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2666，得... |
| 7 | `ContractEffectiveDate` | 扩募决议生效日期 | date | ✓ | 77.78% |  |
| 8 | `IssueBeginDate` | 扩募发售起始日期 | date | ✓ | 77.78% |  |
| 9 | `IssueEndDate` | 扩募发售截止日期 | date | ✓ | 77.78% |  |
| 10 | `ListedDate` | 扩募份额上市日期 | date | ✓ | 66.67% |  |
| 11 | `IssuePrice` | 扩募发售价(元/份) | number(19,6) | ✓ | 77.78% |  |
| 12 | `PlannedIssueValueUpper` | 扩募拟发售金额上限(元) | number(19,2) | ✓ | 100.0% |  |
| 13 | `PlannedIssueValueFloor` | 扩募拟发售金额下限(元) | number(19,2) | ✓ | 22.22% |  |
| 14 | `PlannedIssueShareUpper` | 扩募拟发售份额上限(份) | number(19,2) | ✓ | 100.0% |  |
| 15 | `ActualIssueValue` | 实际扩募发售金额(元) | number(19,2) | ✓ | 66.67% |  |
| 16 | `ActualIssueShare` | 实际扩募发售份额(份) | number(19,2) | ✓ | 66.67% |  |
| 17 | `ReDate` | 配售权益登记日 | date | ✓ | 11.11% |  |
| 18 | `Proportion` | 配售比例 | number(10,4) | ✓ | 11.11% |  |
| 19 | `OnExchangeSubCode` | 场内认购代码 | varchar2(20) | ✓ | 22.22% |  |
| 20 | `OnExchangeSubName` | 场内认购简称 | varchar2(40) | ✓ | 22.22% |  |
| 21 | `OffExchangeSubCode` | 场外认购代码 | varchar2(20) | ✓ | 11.11% |  |
| 22 | `OffExchangeSubName` | 场外认购简称 | varchar2(40) | ✓ | 11.11% |  |
| 23 | `ExRightDate` | 除权基准日 | date | ✓ | 11.11% |  |
| 24 | `OriginatorShare` | 原始权益人及同一控制下关联方配售份额(份) | number(19,2) | ✓ | 44.44% |  |
| 25 | `OriginatorShareRatio` | 原始权益人或同一控制下关联方配售份额占比(%) | number(19,4) | ✓ | 44.44% |  |
| 26 | `OtherStraInvestorShare` | 其他战略投资者扩募配售份额(份) | number(19,2) | ✓ | 44.44% |  |
| 27 | `OtherStraInvestorShareRatio` | 其他战略投资者扩募配售份额占比(%) | number(19,4) | ✓ | 44.44% |  |
| 28 | `PrivatePlacementShare` | 定向扩募竞价投资者扩募配售份额(份) | number(19,2) | ✓ | 0.0% |  |
| 29 | `PrivatePlacementShareRatio` | 定向扩募竞价投资者扩募配售份额占比(%) | number(19,4) | ✓ | 0.0% |  |
| 30 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 31 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### AddOfferingMethod (扩募方式)

扩募方式(AddOfferingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2666，得到扩募方式的具体描述：1-定向扩募，2-向原持有人配售，3-公开扩募。

## SQL示例

```sql
-- 查询 基础设施基金(REITs)扩募信息 数据
SELECT *
FROM mf_reitsaddoffering
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
