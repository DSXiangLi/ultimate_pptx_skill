# MF_FundSizeValueStyle

**中文名**: 基金规模价值风格归因

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundSizeValueStyle` |
| MySQL表名 | `mf_fundsizevaluestyle` |
| 中文名 | 基金规模价值风格归因 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：通过传统的线性回归模型，把基金收益分解为大盘价值、大盘成长、中盘价值、中盘成长、小盘价值、小盘成长6个巨潮风格指数收益率的贡献和基金自身超额收益(alpha)的贡献，从而评价基金的规模、价值风格
2.数据范围：2006年2月-至今。
3.信息来源：	根据证监会分类，选取股票型基金和混合型基金，应用传统的线性回归模型：
y_t- rf_t=α+β_BL (x_BLt- rf_t )+β_BH (x_BHt- rf_t )+β_ML (x_MLt- rf_t )+β_MH (x_MHt- rf_t )+β_SL (x_SLt- rf_t )+β_SH (x_SHt- rf_t )+ϵ_t
其中， y_t表示基金周度收益率， rf_t表示一年期国债收益率/52，x_BLt 表示大盘价值股指数周收益率，x_BHt 表示大盘成长股指数周收益率，x_MLt 表示中盘价值股指数周收益率，x_MHt 表示中盘成长股指数周收益率，x_SLt 表示小盘价值股指数周收益率，x_SHt 表示小盘成长股指数周收益率，ϵ_t表示干扰项，β越大，表示该因子的暴露程度越大，对产品收益的影响也就越大，因此可推测基金的规模和价值风格

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `largeCapValueSensi` | 大盘价值敏感度 | number(18,9) | ✗ | 100.0% |  |
| 6 | `largeCapValuePVal` | 大盘价值P值 | number(18,9) | ✗ | 100.0% |  |
| 7 | `largeCapGrowthSensi` | 大盘成长敏感度 | number(18,9) | ✗ | 100.0% |  |
| 8 | `largeCapGrowthPVal` | 大盘成长P值 | number(18,9) | ✗ | 100.0% |  |
| 9 | `MidCapValueSensi` | 中盘价值敏感度 | number(18,9) | ✗ | 100.0% |  |
| 10 | `MidCapValuePVal` | 中盘价值P值 | number(18,9) | ✗ | 100.0% |  |
| 11 | `MidCapGrowthSensi` | 中盘成长敏感度 | number(18,9) | ✗ | 100.0% |  |
| 12 | `MidCapGrowthPVal` | 中盘成长P值 | number(18,9) | ✗ | 100.0% |  |
| 13 | `SmallCapValueSensi` | 小盘价值敏感度 | number(18,9) | ✗ | 100.0% |  |
| 14 | `SmallCapValuePVal` | 小盘价值P值 | number(18,9) | ✗ | 100.0% |  |
| 15 | `SmallCapGrowthSensi` | 小盘成长敏感度 | number(18,9) | ✗ | 100.0% |  |
| 16 | `SmallCapGrowthPVal` | 小盘成长P值 | number(18,9) | ✗ | 100.0% |  |
| 17 | `AdjRSquare` | 拟合度 | number(18,9) | ✗ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,36)，得到指标周期的具体描述：6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 基金规模价值风格归因 数据
SELECT *
FROM mf_fundsizevaluestyle
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
