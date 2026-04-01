# MF_CampisiPerfAtrb

**中文名**: Campisi债券型基金业绩归因

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CampisiPerfAtrb` |
| MySQL表名 | `mf_campisiperfatrb` |
| 中文名 | Campisi债券型基金业绩归因 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：基于认可度相对较高、实用性相对较强的Campisi模型，选取债券型、混合偏债型（剔除可转债）基金(MF_JYFundType.ThirdAssetCatCode in(130101,130102,130103,130201,130202,130401,130403,120301,120401) ,标准指数债券型,短期纯债型,普通债券型(二级),增强指数债券型,普通债券型(一级),中短期纯债型,偏债型,股债平衡型,长期纯债型)，将其收益分解为票息效应（Income effect）、国债变化效应（Treasury Effect）、利差变化效应（Spread Effect）。其中，票息效应是指持有票息收益所得，属于静态收益；国债效应是国债利率变动的影响，表示系统性收益；利差效应是由行业配置和个券选择所决定，属于策略收益。注意本表分析的是整体组合的票息/国债/利差效应，受债券整体配置比重影响。
2.数据范围：2014年11月-至今。
3.信息来源：债券国债效应(日)=期初修正久期*(相同Maturity的国债利率变动/365)*(-1)；债券票息效应(日)=期末票息/365/期末全价；债券利差效应(日)=债券总收益率-国债效应-票息效应。分别计算基金的国债效应、票息效应和利差效应，即∑Wj*Rj，Wj表示基金持有的第j只重仓券的权重（资产净值占比），Rj表示第j只券的国债/票息/利差效应；最后计算基金在选定样本周期的年化国债/票息/利差效应={∏(1+Ri)}^(12/N)-1，i表示周期中的第i个交易日，N表示指标周期（月），Ri表示基金每日的国债/票息/利差效应。其中：若债券的Maturity年数无法与国债利率期限匹配，则取Interpolated Yield，即插值法估算后的利率变动；债券总收益率=期末全价/期初全价-1，其中期末全价=期末净价+期末应付利息/365+截止期末累计分期还本，期初全价=期初净价+期初应付利息/365+截止期初累计分期还本。结果显示的是根据基金资产净值占比加权后累乘的年化收益率。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `DurationMagtContri` | 国债效应(%) | number(18,9) | ✗ | 100.0% | 国债效应(DurationMagtContri): 表示国债利率变动的影响，属于系统性收益。 |
| 6 | `SpreadContri` | 利差效应(%) | number(18,9) | ✗ | 100.0% | 利差效应(SpreadContri): 由行业配置和个券选择所决定，属于策略收益。 |
| 7 | `CouponContri` | 票息效应(%) | number(18,9) | ✗ | 100.0% | 票息效应（CouponContri）：指持有票息收益所得，属于静态收益。 |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。由于基金持仓数据只披露在主基金，因此以截止日期=’2020-4-30‘，指标周期=近6个月为例，子基金的指标可用以下语句提取：
select c.ChiName,b.RelatedInnerCode 子基金内码,a.DurationMagtContri 利率管理能力 from MF_CampisiPerfAtrb a
join MF_CodeRelationshipNew b
on a.InnerCode=b.InnerCode and '2020-4-30' between b.StartDate and isnull(b.EndDate,'9999-9-9') 
and b.CodeDefine in(21,22,37,76)
join SecuMain c
on c.InnerCode=b.RelatedInnerCode
where a.EndDate='2020-4-30' and a.IndexCycle=6

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,36)，得到指标周期的具体描述：6-六个月，12-一年，36-三年。

### DurationMagtContri (国债效应(%))

国债效应(DurationMagtContri): 表示国债利率变动的影响，属于系统性收益。

### SpreadContri (利差效应(%))

利差效应(SpreadContri): 由行业配置和个券选择所决定，属于策略收益。

### CouponContri (票息效应(%))

票息效应（CouponContri）：指持有票息收益所得，属于静态收益。

## SQL示例

```sql
-- 查询 Campisi债券型基金业绩归因 数据
SELECT *
FROM mf_campisiperfatrb
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
