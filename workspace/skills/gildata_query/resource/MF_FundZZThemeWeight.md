# MF_FundZZThemeWeight

**中文名**: 基金中证主题指数持仓比重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundZZThemeWeight` |
| MySQL表名 | `mf_fundzzthemeweight` |
| 中文名 | 基金中证主题指数持仓比重 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周度计算 |
| 字段数量 | 11 |
| 版本 | 1.02 |

## 表描述

1.内容说明：包含偏股型基金在中证200多个主题指数成分股的持仓比重，以及中证主题指数成分股占全市场总股本的比重，用于判断基金的主题风格，如中证红利、科技100、5G通信、光伏产业等，新主题的新增以中证指数的发布为准。
2.数据范围：2014年11月-至今。
3.信息来源：中证主题指数成分股取自< 指数成分 LC_IndexComponent > ；基金成分股持仓数据取自基金最新定期报告；主题指数的市场占有率等于(成分股_收盘价*成分股_总股本)/(全部A股_收盘价*全部A股_总股本)，其中，股票收盘价取自<=报告期的最新交易日收盘价，总股本取自上个报告期（半年报/年报）至当前报告期最新披露的总股本

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 4 | `IndexCode` | 主题指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode): 与“指数基本情况(LC_IndexBasicInfo)”中的“指数内部编码(Ind... |
| 5 | `IndexName` | 主题指数简称 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `PosCharacter` | 持仓类型 | number(10) | ✓ | 89.7% | 持仓类型(PosCharacter): 1-重仓股，2-股票明细 |
| 7 | `HoldingWeight` | 持有比重 | number(18,9) | ✗ | 100.0% |  |
| 8 | `IndexMktWeight` | 主题指数市场占有率 | number(18,9) | ✗ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。
由于基金定报的持仓数据披露在主基金，因此本表只显示主基金数据，子基金的数据可用如下语句提取，以报告期’2020-3-31‘，主题指数=’量子通信‘为例，

select c.SecuCode 子基金交易代码,a.HoldingWeight 持有比重 from MF_FundZZThemeWeight a 
join MF_CodeRelationshipNew b 
on a.InnerCode=b.InnerCode and '2020-3-31' between b.StartDate and isnull(b.EndDate,'9999-9-9') and
 b.CodeDefine in(21,22,37,76) 
 join SecuMain c 
 on c.InnerCode=b.RelatedInnerCode 
 where a.EndDate='2020-3-31' and IndexName='量子通信' and a.PosCharacter=1

### IndexCode (主题指数内部编码)

指数内部编码(IndexCode): 与“指数基本情况(LC_IndexBasicInfo)”中的“指数内部编码(IndexCode)”关联。

### PosCharacter (持仓类型)

持仓类型(PosCharacter): 1-重仓股，2-股票明细

## SQL示例

```sql
-- 查询 基金中证主题指数持仓比重 数据
SELECT *
FROM mf_fundzzthemeweight
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
