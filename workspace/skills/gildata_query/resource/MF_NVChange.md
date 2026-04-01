# MF_NVChange

**中文名**: 公募基金净值变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NVChange` |
| MySQL表名 | `mf_nvchange` |
| 中文名 | 公募基金净值变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.本表记录中报、年报中披露的基金基金净值、基金净收益、报告期内基金申购赎回、利益分配等情况。
2.历史数据：2001年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `NVAtBegin` | 期初基金净值(元) | number(19,4) | ✓ | 99.91% |  |
| 5 | `NetProfit` | 基金净收益(元) | number(19,4) | ✓ | 1.13% |  |
| 6 | `UnrealizedProfitChange` | 未实现估值增值变动数(元) | number(19,4) | ✓ | 1.04% |  |
| 7 | `NVChangeDueToOperating` | 经营活动产生的基金净值变动数(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `ApplyingMoney` | 基金申购款(元) | number(19,4) | ✓ | 93.75% |  |
| 9 | `RedemptionMoney` | 基金赎回款(元) | number(19,4) | ✓ | 92.24% |  |
| 10 | `NVChangeDueToUnitTrade` | 基金单位交易产生的基金净值变动数(元) | number(19,4) | ✓ | 95.33% |  |
| 11 | `DistributedProfit` | 本期向持有人分配收益(元) | number(19,4) | ✓ | 22.65% |  |
| 12 | `NVAtEnd` | 期末基金净值(元) | number(19,4) | ✓ | 100.0% |  |
| 13 | `PriorYearProfitAdjust` | 以前年度损益调整 | number(19,4) | ✓ | 0.09% |  |
| 14 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金净值变动 数据
SELECT *
FROM mf_nvchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
