# MF_HolderInfo

**中文名**: 公募基金持有人结构信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_HolderInfo` |
| MySQL表名 | `mf_holderinfo` |
| 中文名 | 公募基金持有人结构信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 不定时更新 |
| 字段数量 | 27 |
| 版本 | 1.03 |

## 表描述

1.本表记录基金份额持有人户数、持有人结构，包括机构、个人持有份额的详细数据、占比等。前十大持有的持有份额合计、占比等数据。
2.历史数据：2004年6月起-至今，其中前十大持有份额合计及占比合计自1998年4月起-至今。
3.数据来源：基金公司披露的上市公告书、半年报、年报、合同生效公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `HolderAccountNumber` | 持有人户数 | number(10) | ✓ | 92.47% |  |
| 8 | `AverageHoldShares` | 户均持有份额(份) | number(18,4) | ✓ | 92.47% |  |
| 9 | `InstitutionHoldShares` | 机构持有份额(份) | number(18,4) | ✓ | 83.27% |  |
| 10 | `InstitutionHoldRatio` | 机构持有比例(%) | number(18,6) | ✓ | 83.86% |  |
| 11 | `IndividualHoldshares` | 个人持有份额(份) | number(18,4) | ✓ | 90.79% |  |
| 12 | `IndividualHoldRatio` | 个人持有比例(%) | number(18,6) | ✓ | 90.61% |  |
| 13 | `UndefinedHoldShares` | 未明确投资者持有份额(份) | number(18,4) | ✓ | 0.02% |  |
| 14 | `UndefinedHoldRatio` | 未明确投资者持有比例(%) | number(18,6) | ✓ | 0.02% |  |
| 15 | `Top10HolderAmount` | 前十大持有人持有份额合计(份) | number(18,4) | ✓ | 11.35% |  |
| 16 | `Top10HoldersProportion` | 前十大持有人持有比例合计(%) | number(18,4) | ✓ | 11.35% | 前十大持有人持有比例合计（Top10HoldersProportion）：上市基金一般披露上市份额内按持有数量从大到小排... |
| 17 | `ProfessionalHoldShares` | 基金从业人员持有份额(份) | number(18,4) | ✓ | 84.52% |  |
| 18 | `ProfessionalHoldRatio` | 基金从业人员持有比例(%) | number(18,6) | ✓ | 84.49% |  |
| 19 | `ETFFeederHoldShares` | ETF联接基金持有份额 | number(18,4) | ✓ | 2.02% |  |
| 20 | `ETFFeederHoldRatio` | ETF联接基金持有占总份额比例(%) | number(18,6) | ✓ | 2.02% |  |
| 21 | `SeniorManagementStart` | 高级管理人员、基金投资和研究部门负责人持有份额区间下限(份) | number(18,4) | ✓ | 59.75% |  |
| 22 | `SeniorManagementEnd` | 高级管理人员、基金投资和研究部门负责人持有份额区间上限(份) | number(18,4) | ✓ | 56.86% |  |
| 23 | `FundManagerStart` | 基金经理持有份额区间下限(份) | number(18,4) | ✓ | 59.83% |  |
| 24 | `FundManagerEnd` | 基金经理持有份额区间上限(份) | number(18,4) | ✓ | 57.41% |  |
| 25 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 26 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### Top10HoldersProportion (前十大持有人持有比例合计(%))

前十大持有人持有比例合计（Top10HoldersProportion）：上市基金一般披露上市份额内按持有数量从大到小排序的前十，此时前十比例合计=SUM(第X名持有人持有上市份额/上市总份额*100%)（注：第X名持有人持有上市份额/上市总份额*100%--该结果直取MF_TopTenHolder的HoldingRatio）；
有极少部分上市基金披露总份额内按持有数量从大到小排序的前十，此时前十比例合计=SUM(第X名持有人持有份额/总份额*100%)（注：第X名持有人持有份额/总份额*100%--该结果直取MF_TopTenHolder的HoldingRatio）；
货币基金一般披露总份额内持有按持有数量从大到小排序的前十，此时前十比例合计=SUM(第X名持有人持有份额/总份额*100%)（注：第X名持有人持有份额/总份额*100%--该结果直取MF_TopTenHolder的HoldingRatio）；
另，对于同时为上市基金和货币基金的，此处的前十会优先取上市基金的结果

## SQL示例

```sql
-- 查询 公募基金持有人结构信息 数据
SELECT *
FROM mf_holderinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
