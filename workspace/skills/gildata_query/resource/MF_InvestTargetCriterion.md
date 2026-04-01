# MF_InvestTargetCriterion

**中文名**: 公募基金投资目标比例

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InvestTargetCriterion` |
| MySQL表名 | `mf_investtargetcriterion` |
| 中文名 | 公募基金投资目标比例 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金投资的资产类别及规定比例、基金参照的业绩比较基准(InvestTarget=90)、指数及指增基金所跟踪的投资标的（InvestTarget=7），及所对应的起始日期、终止日期等信息。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `IfExecuted` | 是否执行 | char(2) | ✓ | 100.0% | 是否执行(IfExecuted)，该字段固定以下常量：1-是；0-否 |
| 7 | `ExecuteDate` | 执行日期 | date | ✓ | 100.0% |  |
| 8 | `CancelDate` | 取消日期 | date | ✓ | 23.19% |  |
| 9 | `InvestTarget` | 投资标的 | varchar2(20) | ✓ | 100.0% | 投资标的(InvestTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 1091 AND ... |
| 10 | `TracedIndexCode` | 参照基准指数内部编码 | number(10) | ✓ | 46.23% | 参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（Inner... |
| 11 | `TopInvestRatio` | 投资比例最高值 | number(18,6) | ✓ | 70.9% |  |
| 12 | `MinimumInvestRatio` | 投资比例最低值 | number(18,6) | ✓ | 74.96% |  |
| 13 | `InvestRatioBenchmark` | 投资比例基准 | varchar2(50) | ✓ | 57.35% | 投资比例基准(InvestRatioBenchmark)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 14 | `Notes` | 备注说明 | clob | ✓ | 25.84% |  |
| 15 | `InvestRatioDescription` | 投资比例描述 | varchar2(250) | ✓ | 57.35% |  |
| 16 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 17 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfExecuted (是否执行)

是否执行(IfExecuted)，该字段固定以下常量：1-是；0-否

### InvestTarget (投资标的)

投资标的(InvestTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 1091 AND DM IN (10,11,13,14,19,2,20,200,3,300,301,302,303,304,305,306,307,308,309,310,314,315,318,4,402,405,7,700,9,90,91,95)，得到投资标的的具体描述：2-股票，3-债券，4-国债，7-指数投资，9-债券回购，10-短期资金市场金融品种，11-基金，13-权证，14-商品，19-港股通，20-新三板股票，90-业绩比较标准，91-日跟踪误差，95-年跟踪误差，200-权益类资产投资，300-可转债及信用债，301-短期债券，302-信用债，303-可转换债券，304-金融债券，305-企业债券，306-央行票据，307-资产支持证券，308-国有企业债券，309-产业债，310-实业债，314-中小企业私募债券，315-高票息债券，318-基础设施资产支持证券，402-同业存单，405-固定收益类资产，700-主题行业。

### TracedIndexCode (参照基准指数内部编码)

参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基准指数的交易代码、交易简称等。

### InvestRatioBenchmark (投资比例基准)

投资比例基准(InvestRatioBenchmark)与(CT_SystemConst)表中的DM字段关联，令LB = 1092 AND DM IN(1,2,4,6,9)，得到投资比例基准的具体描述：1-基金资产净值，2-基金资产总额，4-股票投资总额，6-非现金基金资产，9-债券投资总额。

## SQL示例

```sql
-- 查询 公募基金投资目标比例 数据
SELECT *
FROM mf_investtargetcriterion
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
