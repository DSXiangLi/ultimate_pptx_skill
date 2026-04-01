# Index_MSCISecuDividend

**中文名**: MSCI指数成份分红

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_MSCISecuDividend` |
| MySQL表名 | `index_mscisecudividend` |
| 中文名 | MSCI指数成份分红 |
| 路径 | 聚源新版数据库 > 产品代理 > MSCI代理数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 29 |
| 版本 | 1 |

## 表描述

内容说明：收录个股分红数据，包括除息日、红利再投资日、总股息/税后股息金额、分红股本基数等。
数据范围：2024年至今
信息来源：MSCI

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 	 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `MSCode` | MS成份券内码 | number(10) | ✗ | 100.0% |  |
| 5 | `DividendType` | 股息类型 | number(10) | ✗ | 100.0% | 股息类型(DividendType)与(CT_SystemConst)表中的DM字段关联，令LB=2309 AND DM... |
| 6 | `DividendDetail` | 股息详情 | varchar2(50) | ✗ | 100.0% |  |
| 7 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 8 | `MSDividendCode` | MS分红内码 | number(10) | ✗ | 100.0% |  |
| 9 | `RIC` | 路孚特代码 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 72.06% | 证券内部编码(InnerCode)：关联不同主表，查询证券代码、证券简称等基本信息。当0<SecuInnerCode<=... |
| 11 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% |  |
| 12 | `EngName` | 英文名称 | varchar2(100) | ✓ | 100.0% |  |
| 13 | `ReinvestDay` | 红利再投资日 | date | ✓ | 100.0% |  |
| 14 | `IfCorrection` | 是否修正 | number(10) | ✓ | 100.0% |  |
| 15 | `DeclaredDividend` | 公告股息金额 | number(20,5) | ✓ | 100.0% |  |
| 16 | `GrossDividend` | 总股息金额 | number(20,5) | ✓ | 100.0% |  |
| 17 | `DividendAdjFactor` | 股息调整因子 | number(20,5) | ✓ | 100.0% |  |
| 18 | `PurifiedGrossDividend` | 总股息金额(purified) | number(20,5) | ✓ | 7.12% |  |
| 19 | `PurifiedDIVAjdFactor` | 股息调整因子(purified) | number(20,5) | ✓ | 7.12% |  |
| 20 | `NetDividend_INT` | 净股息金额(国际税率) | number(20,5) | ✓ | 83.15% |  |
| 21 | `NetDividend_INT_P` | 净股息金额(国际税率_purified) | number(20,5) | ✓ | 13.28% |  |
| 22 | `NetDividend_DOM` | 净股息金额(国内税率) | number(20,5) | ✓ | 46.2% |  |
| 23 | `NetDividend_DOM_P` | 净股息金额(国内税率_purified) | number(20,5) | ✓ | 0.07% |  |
| 24 | `DividendCurrency` | 股息币种 | number(10) | ✓ | 99.87% |  |
| 25 | `DividendUnit` | 股息单位 | number(10,3) | ✓ | 100.0% |  |
| 26 | `DiviBase` | 分红股本基数 | number(22,4) | ✓ | 24.51% |  |
| 27 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

	
指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### DividendType (股息类型)

股息类型(DividendType)与(CT_SystemConst)表中的DM字段关联，令LB=2309 AND DM IN (10,20,30,40,60,70)，得到股息类型的具体描述：10-临时付款，20-最后一笔付款，30-月度付款，40-季度付款，60-年度付款，70-额外付款。

### InnerCode (证券内部编码)

证券内部编码(InnerCode)：关联不同主表，查询证券代码、证券简称等基本信息。当0<SecuInnerCode<=1000000时，与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联；当1000000<SecuInnerCode<=2000000时，与“港股证券主表(HK_SecuMain)”中的“证券内部编码(InnerCode)”关联；当7000000<SecuInnerCode<=10000000时，与“ 美股证券主表(US_SecuMain)”中的“证券内部编码(InnerCode)”关联。

## SQL示例

```sql
-- 查询 MSCI指数成份分红 数据
SELECT *
FROM index_mscisecudividend
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
