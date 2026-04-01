# MF_FundZXSensi

**中文名**: 基金中信行业敏感度

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundZXSensi` |
| MySQL表名 | `mf_fundzxsensi` |
| 中文名 | 基金中信行业敏感度 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 39 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录基金通过传统的线性回归模型，把基金收益分解为30个中信一级行业指数收益率的贡献和基金自身超额收益(alpha)的贡献，从而评价基金的行业风格。
选取股票型基金和混合型基金，应用传统的线性回归模型：
y(t)- rf(t)=α+∑β(i) *(x(it-) rf(t) )+ϵ(t)
其中，y(t) 表示基金周涨跌幅， rf表示无风险收益率（一年期国债收益率/52），x(it) 表示中信行业指数的收益率， βi表示行业i对基金收益的贡献， β越大表示该行业的暴露程度越大，对产品收益的贡献就相对越大。
2.数据范围：1990年1月起-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截至日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `IndiCategory` | 指标 | number(10) | ✗ | 100.0% | 指标(IndiCategory)：1-β系数；2-P值。 |
| 6 | `Petro` | 石油石化 | number(18,9) | ✓ | 100.0% |  |
| 7 | `Coal` | 煤炭 | number(18,9) | ✓ | 100.0% |  |
| 8 | `NonFerrousMetals` | 有色金属 | number(18,9) | ✓ | 100.0% |  |
| 9 | `ElectricalEquipment` | 电力及公用事业 | number(18,9) | ✓ | 100.0% |  |
| 10 | `Steel` | 钢铁 | number(18,9) | ✓ | 100.0% |  |
| 11 | `BasicChemicals` | 基础化工 | number(18,9) | ✓ | 100.0% |  |
| 12 | `Building` | 建筑 | number(18,9) | ✓ | 100.0% |  |
| 13 | `BuildingMaterials` | 建材 | number(18,9) | ✓ | 100.0% |  |
| 14 | `LightIndustry` | 轻工制造 | number(18,9) | ✓ | 100.0% |  |
| 15 | `CapitalEquipment` | 机械 | number(18,9) | ✓ | 100.0% |  |
| 16 | `NewEnergy` | 电力设备及新能源 | number(18,9) | ✓ | 100.0% |  |
| 17 | `Defence` | 国防军工 | number(18,9) | ✓ | 100.0% |  |
| 18 | `Automobiles` | 汽车 | number(18,9) | ✓ | 100.0% |  |
| 19 | `CommerceRetailng` | 商贸零售 | number(18,9) | ✓ | 100.0% |  |
| 20 | `Services` | 消费者服务 | number(18,9) | ✓ | 100.0% |  |
| 21 | `HomeAppliances` | 家电 | number(18,9) | ✓ | 100.0% |  |
| 22 | `TextilesApparel` | 纺织服装 | number(18,9) | ✓ | 100.0% |  |
| 23 | `PharmBiotech` | 医药 | number(18,9) | ✓ | 100.0% |  |
| 24 | `FoodBeverage` | 食品饮料 | number(18,9) | ✓ | 100.0% |  |
| 25 | `Agriculture` | 农林牧渔 | number(18,9) | ✓ | 100.0% |  |
| 26 | `Bank` | 银行 | number(18,9) | ✓ | 100.0% |  |
| 27 | `NonBankingFinancials` | 非银行金融 | number(18,9) | ✓ | 100.0% |  |
| 28 | `RealEstate` | 房地产 | number(18,9) | ✓ | 100.0% |  |
| 29 | `Transportation` | 交通运输 | number(18,9) | ✓ | 100.0% |  |
| 30 | `Electronics` | 电子 | number(18,9) | ✓ | 100.0% |  |
| 31 | `Communications` | 通信 | number(18,9) | ✓ | 100.0% |  |
| 32 | `Computer` | 计算机 | number(18,9) | ✓ | 100.0% |  |
| 33 | `Media` | 传媒 | number(18,9) | ✓ | 100.0% |  |
| 34 | `Conglomerates` | 综合 | number(18,9) | ✓ | 100.0% |  |
| 35 | `ComprehensiveFinancial` | 综合金融 | number(18,9) | ✓ | 100.0% |  |
| 36 | `AdjRSquare` | 拟合度 | number(18,9) | ✓ | 100.0% |  |
| 37 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 38 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 39 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(12,24,36)，得到指标周期的具体描述：12-一年，24-两年，36-三年。

### IndiCategory (指标)

指标(IndiCategory)：1-β系数；2-P值。

## SQL示例

```sql
-- 查询 基金中信行业敏感度 数据
SELECT *
FROM mf_fundzxsensi
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
