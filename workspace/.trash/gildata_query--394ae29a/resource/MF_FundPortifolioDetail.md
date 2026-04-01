# MF_FundPortifolioDetail

**中文名**: 公募基金投资基金明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundPortifolioDetail` |
| MySQL表名 | `mf_fundportifoliodetail` |
| 中文名 | 公募基金投资基金明细 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 不定时 |
| 字段数量 | 15 |
| 版本 | 1.05 |

## 表描述

1.本表记录公募基金投资基金的明细。
2.历史数据：2009年12月起-至今。
3.数据来源：基金公司披露的定期报告、上市交易公告书等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `FundInnerCode` | 投资基金内部编码 | number(10) | ✗ | 100.0% | 投资基金内部编码（FundInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode... |
| 9 | `SharesHolding` | 持有数量(份) | number(18,4) | ✓ | 94.48% |  |
| 10 | `MarketValue` | 公允价值(元) | number(18,4) | ✓ | 100.0% |  |
| 11 | `RatioInNV` | 占资产净值比例(%) | number(18,6) | ✓ | 99.99% |  |
| 12 | `IfManagerFund` | 是否管理人及关联方管理基金 | number(10) | ✓ | 95.98% | 是否管理人及关联方管理基金(IfManagerFund)与(CT_SystemConst)表中的DM字段关联，令LB=9... |
| 13 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN(17,20,23,61,63,5,6)，得到信息来源的具体描述：5-年度报告，6-中期报告，17-第一季度报告，20-基金上市公告书，23-第三季度报告，61-第二季度报告，63-第四季度报告。

### FundInnerCode (投资基金内部编码)

投资基金内部编码（FundInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得投资基金的交易代码、简称等。香港基金与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### IfManagerFund (是否管理人及关联方管理基金)

是否管理人及关联方管理基金(IfManagerFund)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否管理人及关联方管理基金的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金投资基金明细 数据
SELECT *
FROM mf_fundportifoliodetail
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
