# MF_FundProdName

**中文名**: 公募基金产品名称

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundProdName` |
| MySQL表名 | `mf_fundprodname` |
| 中文名 | 公募基金产品名称 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金的交易所披露简称、集中申购简称、ETF申购赎回简称等基金相关的名称类信息。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。其中，4-证监会简称处理的是资本市场电子化信息披露平台-公募基金净值日报的简称；6-公告披露简称处理的是基金产品资料概要和定报披露的简称；8-基金全称处理的是发售公告或是资本市场电子化信息披露平台-基金概况的全称，是将基金的多个份额合并的基金全称。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✓ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `InfoType` | 信息类别 | number(10) | ✓ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1850，得到信息类别的具... |
| 7 | `DisclName` | 披露名称 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `ChiSpelling` | 拼音证券简称 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `EffectiveDate` | 生效日期 | date | ✓ | 100.0% |  |
| 10 | `ExpiryDate` | 失效日期 | date | ✓ | 28.99% |  |
| 11 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 12 | `Remark` | 备注说明 | varchar2(500) | ✓ | 0.08% |  |
| 13 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1850，得到信息类别的具体描述：1-证券交易所简称，2-集中申购简称，3-ETF申购赎回简称，4-证监会简称，5-扩位证券简称，6-公告披露简称，8-基金全称。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金产品名称 数据
SELECT *
FROM mf_fundprodname
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
