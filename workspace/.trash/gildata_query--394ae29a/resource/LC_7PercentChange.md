# LC_7PercentChange

**中文名**: 交易所日公开信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_7PercentChange` |
| MySQL表名 | `lc_7percentchange` |
| 中文名 | 交易所日公开信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1.03 |

## 表描述

1.收录交易所公布的，触发日涨跌幅偏离值达到7％、日价格振幅达到15%、日换手率达到20％、连续三个交易日内收盘价格涨幅偏离值累计达到20%等各类披露条件的个股成交信息，包括个股总成交量、成交金额以及成交金额在前五名的营业部的成交明细等。
2.数据范围：1997-02-26至今
3.信息来源：上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部代码 | number(10) | ✗ | 100.0% | 证券内部编码(InnerCode)与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.99% |  |
| 4 | `AbnormalType` | 异动类型 | number(10) | ✓ | 100.0% | 异动类型(AbnormalType)：仅展示其中一种异动类型，获取完整异动类型需关联从表使用，以从表异动类型(TypeC... |
| 5 | `TypeCode` | 异动类型 | number(10) | ✓ |  | 异动类型(TypeCode)：全面实行注册制后，异动类型新增常量：316-'连续三个交易日内，收盘价跌幅偏离值累计达到1... |
| 6 | `TradingStartDate` | 交易起始日期 | date | ✓ | 100.0% |  |
| 7 | `TradingDay` | 交易(截止)日期 | date | ✗ | 100.0% |  |
| 8 | `SerialNum` | 序号 | number(3) | ✗ | 100.0% |  |
| 9 | `SalesDepartmentName` | 营业部名称 | varchar2(200) | ✗ | 100.0% |  |
| 10 | `BOCode` | 营业部编号 | number(10) | ✓ | 99.82% | 营业部编号(BOCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联... |
| 11 | `SecuCoBelongedCode` | 营业部所属券商编号 | number(10) | ✓ | 99.92% | 营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编... |
| 12 | `SecuCoBelonged` | 营业部所属券商 | varchar2(80) | ✓ | 99.92% |  |
| 13 | `TurnoverVolume` | 成交量(股) | number(16,0) | ✓ | 99.99% |  |
| 14 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 99.99% |  |
| 15 | `ChangePCT` | 涨跌幅 | number(9,6) | ✓ | 7.57% |  |
| 16 | `ChangePCTOffset` | 涨跌幅偏离值 | number(9,6) | ✓ | 61.48% |  |
| 17 | `FluctuatingAmptitude` | 振幅 | number(9,6) | ✓ | 8.97% |  |
| 18 | `TurnoverRate` | 换手率 | number(9,6) | ✓ | 23.6% |  |
| 19 | `TurnoverProp` | 成交占比(%) | number(7,4) | ✓ | 0.34% |  |
| 20 | `TotalBuySaleSum` | 买卖合计金额(元) | number(19,4) | ✓ | 99.88% |  |
| 21 | `BuySum` | #买入金额(元) | number(19,4) | ✓ | 81.21% |  |
| 22 | `SaleSum` | #卖出金额(元) | number(19,4) | ✓ | 81.32% |  |
| 23 | `StatType` | 统计方式 | number(10) | ✓ | 100.0% | 统计方式(StatType)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式的具... |
| 24 | `InvestorType` | 投资者类型 | number(10) | ✓ | 0.12% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND D... |
| 25 | `AccuBuySum` | 累计买入金额(元) | number(19,4) | ✓ | 0.12% |  |
| 26 | `AccuSaleSum` | 累计卖出金额(元) | number(19,4) | ✓ | 0.12% |  |
| 27 | `BuyingRatio` | 买入占比(%) | number(7,4) | ✓ | 0.12% |  |
| 28 | `SellingRatio` | 卖出占比(%) | number(7,4) | ✓ | 0.12% |  |
| 29 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 30 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部代码)

证券内部编码(InnerCode)与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到证券的交易代码、简称等

### AbnormalType (异动类型)

异动类型(AbnormalType)：仅展示其中一种异动类型，获取完整异动类型需关联从表使用，以从表异动类型(TypeCode)为准

### TypeCode (异动类型)

异动类型(TypeCode)：全面实行注册制后，异动类型新增常量：316-'连续三个交易日内，收盘价跌幅偏离值累计达到12%的ST证券、*ST证券'；317-'连续三个交易日内，收盘价涨幅偏离值累计达到12%的ST证券、*ST证券'；318-'连续10个交易日内4次出现正向异常波动情形'；319-'连续10个交易日内4次出现负向异常波动情形'；2023年3月3日全面实行注册制，历史披露异动类型归类210，3月3日后日增数据异动类型归类317

### BOCode (营业部编号)

营业部编号(BOCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部的具体信息；与“企业数据-名称更改(LC_NameHistorical)”中的企业编号(CompanyCode)关联，得到营业部名称变革信息，不同历史阶段可能存在营业部同名情况，需结合名称更改判断是否为同一营业部

### SecuCoBelongedCode (营业部所属券商编号)

营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到所属券商的具体信息；与“企业数据-名称更改(LC_NameHistorical)”中的企业编号(CompanyCode)关联，得到所属券商名称变革信息

### StatType (统计方式)

统计方式(StatType)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式的具体描述：10-买卖金额，11-买入金额，13-卖出金额。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND DM IN (1,4,100,101)，得到投资者类型的具体描述：1-自然人，4-机构，100-中小投资者，101-其他自然人。

## SQL示例

```sql
-- 查询 交易所日公开信息 数据
SELECT *
FROM lc_7percentchange
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
