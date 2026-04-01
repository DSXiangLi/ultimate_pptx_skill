# MF_FundZZIndustrySensi

**中文名**: 基金中证行业敏感度

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundZZIndustrySensi` |
| MySQL表名 | `mf_fundzzindustrysensi` |
| 中文名 | 基金中证行业敏感度 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 28 |
| 版本 | 1 |

## 表描述

1.内容说明：通过传统的线性回归模型，把基金收益分解为能源、原材料、工业、可选消费、主要消费、医药卫生、金融地产、信息技术、电信业务和公用事业10个中证一级行业指数收益率的贡献和基金自身超额收益(alpha)的贡献，从而评价基金的行业风格
2.数据范围：2006年2月-至今。
3.信息来源：	根据证监会分类，选取股票型基金和混合型基金，应用传统的线性回归模型：
y(t)- rf(t)=α+∑β(i) *(x(it-) rf(t) )+ϵ(t)
其中，y(t) 表示基金周涨跌幅， rf表示无风险收益率（一年期国债收益率/52），x(it) 表示中证行业指数的收益率， βi表示行业i对基金收益的贡献， β越大表示该行业的暴露程度越大，对产品收益的贡献就相对越大

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `EnergySensi` | 能源敏感度 | number(18,9) | ✗ | 100.0% |  |
| 6 | `EnergyPVal` | 能源P值 | number(18,9) | ✗ | 100.0% |  |
| 7 | `MaterialsSensi` | 原材料敏感度 | number(18,9) | ✗ | 100.0% |  |
| 8 | `MaterialsPVal` | 原材料P值 | number(18,9) | ✗ | 100.0% |  |
| 9 | `IndustrialsSensi` | 工业敏感度 | number(18,9) | ✗ | 100.0% |  |
| 10 | `IndustrialsPVal` | 工业P值 | number(18,9) | ✗ | 100.0% |  |
| 11 | `ConsumerSensi` | 可选消费敏感度 | number(18,9) | ✗ | 100.0% |  |
| 12 | `ConsumerPVal` | 可选消费P值 | number(18,9) | ✗ | 100.0% |  |
| 13 | `ConsumerStaplesSensi` | 主要消费敏感度 | number(18,9) | ✗ | 100.0% |  |
| 14 | `ConsumerStaplesPVal` | 主要消费P值 | number(18,9) | ✗ | 100.0% |  |
| 15 | `HealthCareSensi` | 医药卫生敏感度 | number(18,9) | ✗ | 100.0% |  |
| 16 | `HealthCarePVal` | 医药卫生P值 | number(18,9) | ✗ | 100.0% |  |
| 17 | `FinancialsSensi` | 金融地产敏感度 | number(18,9) | ✗ | 100.0% |  |
| 18 | `FinancialsPVal` | 金融地产P值 | number(18,9) | ✗ | 100.0% |  |
| 19 | `ITSensi` | 信息技术敏感度 | number(18,9) | ✗ | 100.0% |  |
| 20 | `ITPVal` | 信息技术P值 | number(18,9) | ✗ | 100.0% |  |
| 21 | `TelecommunicationSensi` | 电信业务敏感度 | number(18,9) | ✗ | 100.0% |  |
| 22 | `TelecommunicationPVal` | 电信业务P值 | number(18,9) | ✗ | 100.0% |  |
| 23 | `UtilitiesSensi` | 公用事业敏感度 | number(18,9) | ✗ | 100.0% |  |
| 24 | `UtilitiesPVal` | 公用事业P值 | number(18,9) | ✗ | 100.0% |  |
| 25 | `AdjRSquare` | 拟合度 | number(18,9) | ✗ | 100.0% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,36)，得到指标周期的具体描述：6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 基金中证行业敏感度 数据
SELECT *
FROM mf_fundzzindustrysensi
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
