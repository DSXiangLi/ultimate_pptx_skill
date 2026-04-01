# MF_FundSWSensiII

**中文名**: 基金申万行业敏感度II

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundSWSensiII` |
| MySQL表名 | `mf_fundswsensiii` |
| 中文名 | 基金申万行业敏感度II |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 40 |
| 版本 | 1 |

## 表描述

1.内容说明：通过线性回归模型，把基金收益分解为31个（新）申万一级行业指数收益率的贡献和基金自身超额收益(alpha)的贡献，从而评价基金的行业风格。
2.数据范围：2006年2月-至今。
3.信息来源：根据证监会分类，选取股票型基金和混合型基金，应用传统的线性回归模型：
y(t)- rf(t)=α+∑β(i) *(x(it-) rf(t) )+ϵ(t)
其中，y(t) 表示基金周涨跌幅， rf表示无风险收益率(一年期国债收益率)，x(it) 表示申万行业指数的收益率， βi表示行业i对基金收益的贡献， β越大表示该行业的暴露程度越大，对产品收益的贡献就相对越大。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `IndiCategory` | 指标 | number(10) | ✗ | 100.0% | 指标(IndiCategory)：1-β系数；2-P值 |
| 6 | `Agriculture` | 农林牧渔 | number(18,9) | ✓ | 100.0% |  |
| 7 | `BasicChemicals` | 基础化工 | number(18,9) | ✓ | 100.0% |  |
| 8 | `Steel` | 钢铁 | number(18,9) | ✓ | 100.0% |  |
| 9 | `NonFerrousMetals` | 有色金属 | number(18,9) | ✓ | 100.0% |  |
| 10 | `Electronics` | 电子 | number(18,9) | ✓ | 100.0% |  |
| 11 | `Automobiles` | 汽车 | number(18,9) | ✓ | 100.0% |  |
| 12 | `HomeAppliances` | 家用电器 | number(18,9) | ✓ | 100.0% |  |
| 13 | `FoodBeverage` | 食品饮料 | number(18,9) | ✓ | 100.0% |  |
| 14 | `TextilesApparel` | 纺织服饰 | number(18,9) | ✓ | 100.0% |  |
| 15 | `LightIndustry` | 轻工制造 | number(18,9) | ✓ | 100.0% |  |
| 16 | `PharmBiotech` | 医药生物 | number(18,9) | ✓ | 100.0% |  |
| 17 | `Utilities` | 公用事业 | number(18,9) | ✓ | 100.0% |  |
| 18 | `Transportation` | 交通运输 | number(18,9) | ✓ | 100.0% |  |
| 19 | `RealEstate` | 房地产 | number(18,9) | ✓ | 100.0% |  |
| 20 | `CommerceRetailng` | 商贸零售 | number(18,9) | ✓ | 100.0% |  |
| 21 | `SocialServices` | 社会服务 | number(18,9) | ✓ | 100.0% |  |
| 22 | `Bank` | 银行 | number(18,9) | ✓ | 100.0% |  |
| 23 | `NonBankingFinancials` | 非银金融 | number(18,9) | ✓ | 100.0% |  |
| 24 | `Conglomerates` | 综合 | number(18,9) | ✓ | 100.0% |  |
| 25 | `BuildingMaterials` | 建筑材料 | number(18,9) | ✓ | 100.0% |  |
| 26 | `ConstDecoration` | 建筑装饰 | number(18,9) | ✓ | 100.0% |  |
| 27 | `ElectricalEquipment` | 电力设备 | number(18,9) | ✓ | 100.0% |  |
| 28 | `CapitalEquipment` | 机械设备 | number(18,9) | ✓ | 100.0% |  |
| 29 | `Defence` | 国防军工 | number(18,9) | ✓ | 100.0% |  |
| 30 | `Computer` | 计算机 | number(18,9) | ✓ | 100.0% |  |
| 31 | `Media` | 传媒 | number(18,9) | ✓ | 100.0% |  |
| 32 | `Communications` | 通信 | number(18,9) | ✓ | 100.0% |  |
| 33 | `Coal` | 煤炭 | number(18,9) | ✓ | 100.0% |  |
| 34 | `Petro` | 石油石化 | number(18,9) | ✓ | 100.0% |  |
| 35 | `EP` | 环保 | number(18,9) | ✓ | 100.0% |  |
| 36 | `BeautyCare` | 美容护理 | number(18,9) | ✓ | 100.0% |  |
| 37 | `AdjRSquare` | 拟合度 | number(18,9) | ✓ | 100.0% |  |
| 38 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 39 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 40 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(12,24,36)，得到指标周期的具体描述：12-一年，24-两年，36-三年。

### IndiCategory (指标)

指标(IndiCategory)：1-β系数；2-P值

## SQL示例

```sql
-- 查询 基金申万行业敏感度II 数据
SELECT *
FROM mf_fundswsensiii
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
