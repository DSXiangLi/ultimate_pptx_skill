# MF_FundStyleIndexQuote

**中文名**: 基金概念行业指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundStyleIndexQuote` |
| MySQL表名 | `mf_fundstyleindexquote` |
| 中文名 | 基金概念行业指数行情 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：记录聚源基金风格指数（基金组合）的行情。目前包括概念主题标签、行业穿透标签。主要应用于，判断属于XX行业（属于XX概念主题）的基金组合的整体表现。
2.数据范围：2017年5月-至今。
3.信息来源：加权方式等权，基点为1000点。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TagCategory` | 标签种类 | number(10) | ✗ | 100.0% | 标签种类(TagCategory): 1-热点概念板块，取自于<MF_ThemeTagChange>概念标签-FundT... |
| 3 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金主题... |
| 4 | `FundTagName` | 标签名称 | varchar2(500) | ✗ | 100.0% |  |
| 5 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 6 | `ChangePCT` | 日涨跌幅(%) | number(18,6) | ✓ | 99.91% | 日涨跌幅(%)(ChangePCT)：对应概念/行业下，基金日涨跌幅的算数平均值。 |
| 7 | `ClosePrice` | 收盘价(点) | number(14,4) | ✓ | 100.0% | 收盘价(点)(ClosePrice)：基点设为1000，通过本表ChangePCT-日涨跌幅(%)累乘，拟合出收盘价。 |
| 8 | `ChangeOF` | 日涨跌 | number(14,4) | ✓ | 99.91% |  |
| 9 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期（IndexCycle): 当标签种类（TagCategory）=1， IndexCycle=990, 表示空值... |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TagCategory (标签种类)

标签种类(TagCategory): 1-热点概念板块，取自于<MF_ThemeTagChange>概念标签-FundTagCode以及2级概念标签-SubclassCode；2-中证一级行业穿透，取自于<MF_IndustryTagChange>行业标签-FundTagCode.

### FundTagCode (标签代码)

标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金主题标签变动(MF_ThemeTagChange)的标签代码(FundTagCode)和所属2级概念代码(SubclassCode) 关联。当标签种类（TagCategory)=2， 则FundTagCode跟公募基金行业标签变动(MF_IndustryTagChange)的标签代码(FundTagCode)关联。


### ChangePCT (日涨跌幅(%))

日涨跌幅(%)(ChangePCT)：对应概念/行业下，基金日涨跌幅的算数平均值。

### ClosePrice (收盘价(点))

收盘价(点)(ClosePrice)：基点设为1000，通过本表ChangePCT-日涨跌幅(%)累乘，拟合出收盘价。

### IndexCycle (指标周期)

指标周期（IndexCycle): 当标签种类（TagCategory）=1， IndexCycle=990, 表示空值。当标签种类（TagCategory）=2，与公募基金行业标签变动(MF_IndustryTagChange)的指标周期（IndexCycle)关联。

## SQL示例

```sql
-- 查询 基金概念行业指数行情 数据
SELECT *
FROM mf_fundstyleindexquote
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
