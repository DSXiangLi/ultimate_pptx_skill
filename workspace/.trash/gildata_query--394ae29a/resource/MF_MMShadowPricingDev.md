# MF_MMShadowPricingDev

**中文名**: 货币基金影价偏离度惩罚因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MMShadowPricingDev` |
| MySQL表名 | `mf_mmshadowpricingdev` |
| 中文名 | 货币基金影价偏离度惩罚因子 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 季更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：货币型基金的风险评价指标。影价偏离度反映了采用摊余成本法和影子定价法对货币型基金估值的差异，差异越大表示用摊余成本法得到的基金净值偏离公允价值的程度越大，基金更容易产生浮盈浮亏，货币基金的风险就相对更高，若影价偏离度惩罚因子为0，表示基金净资产未发生偏离，基金浮盈浮亏的风险较小。
2.数据范围：2010年1月起-至今。
3.信息来源：基金公司披露的定期报告计算而得。季报披露定值定价偏离度，令期内偏离度在0.25%-0.5%之间的次数为X，期内偏离度在0.5%以上的次数为Y，指标周期为N（月），当前时点的最新季报时间为t，Z_t=X_t+Y_t*3，Z_t-1=X_t-1+Y_t-1*3……，表示偏离度百分比越高，则其偏离次数被惩罚的力度相对更大，当N=3，影价偏离度惩罚因子=Z_t，当N=6，影价偏离度惩罚因子=Z_t*W_t+Z_t-1*W_t-1，当N=12，影价偏离度惩罚因子= Z_t*W_t+Z_t-1*W_t-1+Z_t-2*W_t-2+Z_t-3*W_t-3，当N=36, 影价偏离度惩罚因子= Z_t*W_t+Z_t-1*W_t-1+ ……+Z_t-10*W_t-10+Z_t-11*W_t-11，W_t为当前时点权重，W_t为上一季报时点权重，……，W(t)随历史倒推衰减，表示距离当前时点越近，则被惩罚的权重越高，∑{W(t)}=1，若Z为空则表示成立不满周期要求，则不生成数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCode` | 指标内码 | number(10) | ✗ | 100.0% | 指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标... |
| 5 | `IndexName` | 指标名称 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 7 | `DataValue` | 指标值 | number(18,9) | ✗ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。
由于基金定报只在主基金披露，本表只显示主基金指标值，以报告期”2020-3-31’、 指标周期=近3个月为例，子基金的指标值可用如下语句提取：
select c.ChiName,b.RelatedInnerCode 子基金内码,a.DataValue 指标值 from MF_MMShadowPricingDev a
join MF_CodeRelationshipNew b
on a.InnerCode=b.InnerCode and '2020-3-31' between b.StartDate and isnull(b.EndDate,'9999-9-9') 
and b.CodeDefine in(21,22,37,76)
join SecuMain c
on c.InnerCode=b.RelatedInnerCode
where a.EndDate='2020-3-31' and a.IndexCycle=3

### IndexCode (指标内码)

指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(3,6,12,36)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 货币基金影价偏离度惩罚因子 数据
SELECT *
FROM mf_mmshadowpricingdev
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
