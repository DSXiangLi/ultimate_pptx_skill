# MF_FundStyleIndexGR

**中文名**: 基金概念行业指数收益表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundStyleIndexGR` |
| MySQL表名 | `mf_fundstyleindexgr` |
| 中文名 | 基金概念行业指数收益表现 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：计算聚源基金风格指数（基金组合）的收益表现。应用场景为，获取 <公募基金主题标签变动 MF_ThemeTagChange> 、<公募基金行业标签变动MF_IndustryTagChange>中，所有概念板块下的基金，看基金近期的收益表现。包括日、周、月、季、半年、一年、二年、三年等周期表现。
2.数据范围：2016年8月-至今。
3.信息来源：根据行情数据<基金风格指数行情表MF_FundStyleIndexQuote>计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TagCategory` | 标签种类 | number(10) | ✗ | 100.0% | 标签种类(TagCategory): 1-热点概念板块，2-中证一级行业穿透 |
| 3 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金主题... |
| 4 | `FundTagName` | 标签名称 | varchar2(500) | ✗ | 100.0% |  |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期（IndexCycle): 当标签种类（TagCategory）=1， IndexCycle=990, 表示空值... |
| 6 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 7 | `DailyGR` | 日收益率(%) | number(18,6) | ✓ | 100.0% |  |
| 8 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,6) | ✓ | 99.91% |  |
| 9 | `RRInSingleWeek` | 一周回报率(%) | number(18,6) | ✓ | 99.75% |  |
| 10 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,6) | ✓ | 99.32% |  |
| 11 | `RRInSingleMonth` | 一个月回报率(%) | number(18,6) | ✓ | 98.36% |  |
| 12 | `RRInThreeMonth` | 三个月回报率(%) | number(18,6) | ✓ | 95.11% |  |
| 13 | `RRInSixMonth` | 六个月回报率(%) | number(18,6) | ✓ | 90.67% |  |
| 14 | `RRInNineMonth` | 九个月回报率(%) | number(18,6) | ✓ | 86.35% |  |
| 15 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,6) | ✓ | 88.37% |  |
| 16 | `RRInSingleYear` | 一年回报率(%) | number(18,6) | ✓ | 82.12% |  |
| 17 | `RRSinceStart` | 设立以来回报率(%) | number(18,6) | ✓ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TagCategory (标签种类)

标签种类(TagCategory): 1-热点概念板块，2-中证一级行业穿透

### FundTagCode (标签代码)

标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金主题标签变动(MF_ThemeTagChange)的标签代码(FundTagCode)和所属2级概念代码(SubclassCode) 关联。当标签种类（TagCategory)=2， 则FundTagCode跟公募基金行业标签变动(MF_IndustryTagChange)的标签代码(FundTagCode)关联。

### IndexCycle (指标周期)

指标周期（IndexCycle): 当标签种类（TagCategory）=1， IndexCycle=990, 表示空值。当标签种类（TagCategory）=2，与公募基金行业标签变动(MF_IndustryTagChange)的指标周期（IndexCycle)关联。

## SQL示例

```sql
-- 查询 基金概念行业指数收益表现 数据
SELECT *
FROM mf_fundstyleindexgr
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
