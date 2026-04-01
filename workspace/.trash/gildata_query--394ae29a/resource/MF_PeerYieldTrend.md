# MF_PeerYieldTrend

**中文名**: 同类基金收益率走势曲线

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PeerYieldTrend` |
| MySQL表名 | `mf_peeryieldtrend` |
| 中文名 | 同类基金收益率走势曲线 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.本表用于绘制同类基金的复权累计收益率走势曲线，从0开始，体现周期内基金的收益变动过程。数据每日刷新，只储存最新数据。累计收益率的周期包括近一个月、三个月、六个月、一年、三年、五年、今年以来。基金产品的收益率走势参见<公募基金收益率走势 MF_NetValueYieldTrend>。
关于基金类别：目前基金分类口径包含了证监会基金分类。查询基金所属类别（同类标准）的样例语句：select b.MS from MF_FundArchivesAttach a join CT_SystemConst b on a.DataCode=b.DM where a.TypeCode=10 and b.LB=1737 and '截止日期'>=StartDate and '截止日期' < isnull(EndDate,'9999-9-9') and a.InnerCode=’基金内码‘
算法说明：以证监会分类股票型基金近一个月收益为例，SQL查询语句如下：
select avg(RRInSingleMonth) from MF_NetValueYieldTrend where TradingDay='2020-11-6' and InnerCode in
(select InnerCode from MF_FundArchivesAttach where TypeCode=10 and DataCode=1101 and '截止日期'<isnull(EndDate,'9999-9-9') and
'截止日期'>StartDate)
2.历史数据：至今
3.信息来源：每一个交易日取所有同类基金的算数平均值计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 3 | `TypeCode` | 基金分类代码 | number(10) | ✓ | 100.0% |  |
| 4 | `TypeName` | 基金分类描述 | varchar2(100) | ✗ | 100.0% | 基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类，聚源一级、二级分类” |
| 5 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTy... |
| 6 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 1.89% |  |
| 8 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 5.1% |  |
| 9 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 10.77% |  |
| 10 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 19.12% |  |
| 11 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 21.01% |  |
| 12 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 63.27% |  |
| 13 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 92.58% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TypeName (基金分类描述)

基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类，聚源一级、二级分类”

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述。当基金分类口径描述(TypeName)=聚源一级分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=2197，IVALUE=1，得到聚源基金一级分类的具体描述。当基金分类口径描述(TypeName)=聚源二级分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=2197，IVALUE=2，得到聚源基金二级分类的具体描述。

## SQL示例

```sql
-- 查询 同类基金收益率走势曲线 数据
SELECT *
FROM mf_peeryieldtrend
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
