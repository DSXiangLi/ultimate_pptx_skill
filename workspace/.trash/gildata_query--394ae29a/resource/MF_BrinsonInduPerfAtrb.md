# MF_BrinsonInduPerfAtrb

**中文名**: 基金Brinson行业业绩归因

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BrinsonInduPerfAtrb` |
| MySQL表名 | `mf_brinsoninduperfatrb` |
| 中文名 | 基金Brinson行业业绩归因 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 季更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1. 内容说明：基金行业Brinson模型，用于评价基金的行业配置能力、行业内的个股选择能力、基金的总超额收益，（剔除新股）。
2. 数据范围：1998年至今
3. 信息来源：如果持仓类型为明细，根据中报年报披露的持仓明细及申万行业分类计算而得，如果持仓类型为重仓，根据季报披露的前十大重仓股及申万行业分类计算而得，持仓明细数据半年度更新，重仓数据季度更新。具体算法如下：首先构造四个组合收益：业绩基准组合P1=∑(W(b,i)*R_(b,i))，主动行业配置组合P2=∑(W(p,i)*R(b,i))，主动择券组合P3=∑W(b,i)*R(p,i))，实际基金组合P4=∑W(p,i)* R(p,i))。其中，Wp,i表示组合中行业i的权重，Wb,i表示基准中行业i的权重，Rp,i表示组合中行业i的收益率，Rb,i表示基准中行业i的收益率。其中，行业分类采用申万一级行业分类，Rp,i通过该基金持有行业i下全部个股的收益率算数平均值计算而得，Wp,i通过该基金持有行业i下的个股总市值占基金持股总市值比计算而得。业绩基准组合R_(b,i)、W(b,i)通过全部A股计算，算法同上，W(b,i)采用最新总股本计算。各期行业配置收益(IndustryAllocation)IAA=P2-P1，个股选择收益(StockSelection)RSS=P3-P1，交互作用收益(Interaction)，即由大类资产配置和择券两者产生的收益，RIN=P4-P2-P3+P1，总互动作用(TotalValueAdded)RTotal=P4-P1。除六个月周期收益率外，其他周期区间收益率采用复利方式计算区间收益率，

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter): 1-重仓股， 2-持仓明细 |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 6 | `IndustryAllocation` | 行业配置 | number(18,9) | ✓ | 100.0% |  |
| 7 | `StockSelection` | 个股选择 | number(18,9) | ✓ | 100.0% |  |
| 8 | `Interaction` | 交互作用 | number(18,9) | ✓ | 100.0% |  |
| 9 | `TotalValueAdded` | 总互动作用 | number(18,9) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### PosCharacter (持仓类型)

持仓类型(PosCharacter): 1-重仓股， 2-持仓明细

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(3,6,12,36)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 基金Brinson行业业绩归因 数据
SELECT *
FROM mf_brinsoninduperfatrb
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
