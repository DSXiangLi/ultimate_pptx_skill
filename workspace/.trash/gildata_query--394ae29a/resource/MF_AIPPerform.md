# MF_AIPPerform

**中文名**: 公募基金定投收益表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AIPPerform` |
| MySQL表名 | `mf_aipperform` |
| 中文名 | 公募基金定投收益表现 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1.01 |

## 表描述

1.本表记录非货币基金&短期理财债券型基金的定投收益情况，包括一年、两年、三年、五年、七年、十年的定投收益率情况，以及开放定投以来的收益率情况。
2.本表假定投资日期为每月1日，若1日为非交易日，向后顺延。
3.历史数据：2017-06-01起-至今。
4.数据来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值(元) | number(18,6) | ✓ | 100.0% |  |
| 5 | `IRInSixMonth` | 六个月定投收益率(%) | number(18,10) | ✓ | 91.47% |  |
| 6 | `IRInSingleYear` | 一年定投收益率(%) | number(18,10) | ✓ | 81.33% |  |
| 7 | `IRInTwoYear` | 二年定投收益率(%) | number(18,10) | ✓ | 63.09% |  |
| 8 | `IRInThreeYear` | 三年定投收益率(%) | number(18,10) | ✓ | 47.69% |  |
| 9 | `IRInFiveYear` | 五年定投收益率(%) | number(18,10) | ✓ | 26.98% |  |
| 10 | `IRInSevenYear` | 七年定投收益率(%) | number(18,10) | ✓ | 15.88% |  |
| 11 | `IRInTenYear` | 十年定投收益率(%) | number(18,10) | ✓ | 7.15% |  |
| 12 | `IRSinceAIP` | 开放定投以来收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 13 | `AnnualizedIRSinceAIP` | 开放定投以来年化收益率(%) | number(18,10) | ✓ | 99.99% | 开放定投以来年化收益率(%)(AnnualizedIRSinceAIP):由于超短期内收益率存在较大偶然性（如1天的收益... |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |
| 16 | `IRInFourYear` | 四年定投收益率(%) | number(18,10) | ✓ | 35.69% |  |
| 17 | `IRInSixYear` | 六年定投收益率(%) | number(18,10) | ✓ | 20.7% |  |
| 18 | `IRInEightYear` | 八年定投收益率(%) | number(18,10) | ✓ | 12.21% |  |
| 19 | `IRInNineYear` | 九年定投收益率(%) | number(18,10) | ✓ | 9.32% |  |
| 20 | `InsertTime` | 发布时间 | date | ✓ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### AnnualizedIRSinceAIP (开放定投以来年化收益率(%))

开放定投以来年化收益率(%)(AnnualizedIRSinceAIP):由于超短期内收益率存在较大偶然性（如1天的收益率），年化收益率数据较大且不具有参考性，故该字段从基金第一个定投日后7日开始计算。

## SQL示例

```sql
-- 查询 公募基金定投收益表现 数据
SELECT *
FROM mf_aipperform
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
