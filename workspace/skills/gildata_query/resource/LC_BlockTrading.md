# LC_BlockTrading

**中文名**: 大宗交易成交明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_BlockTrading` |
| MySQL表名 | `lc_blocktrading` |
| 中文名 | 大宗交易成交明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录大宗交易每日成交信息，包括成交价，成交量，成交金额，以及买入营业部和卖出营业部等信息；
2.数据范围：股票上市之日起；
3.信息来源：上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `TradingType` | 大宗交易方式 | number(10) | ✗ | 100.0% | 大宗交易方式(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=2258，得到大宗交... |
| 7 | `TurnoverPrice` | 成交价格(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `PreCloseDiscountRate` | 相对昨收折价率(%) | number(19,8) | ✓ | 100.0% | 相对昨收折价率(%)(PreCloseDiscountRate)：[1-(大宗交易成交价/当日前收盘价)]*100 |
| 9 | `CloseDiscountRate` | 相对收盘折价率(%) | number(19,8) | ✓ | 100.0% | 相对收盘折价率(%)(CloseDiscountRate)：[1-(大宗交易成交价/当日收盘价)]*100 |
| 10 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValueRatio` | 成交额占比(%) | number(19,8) | ✓ | 100.0% | 成交额占比(%)(TurnoverValueRatio)：沪深市场:单笔大宗交易成交额/(当日此只股票大宗交易成交额之和... |
| 12 | `TurnoverVolume` | 成交量(股) | number(16,0) | ✓ | 100.0% |  |
| 13 | `VolumeUnit` | 成交量单位 | number(10) | ✓ | 100.0% | 成交量单位(VolumeUnit)：该字段固定为 2-股票(股) |
| 14 | `BuySalesDepartment` | 买入营业部 | varchar2(200) | ✓ | 95.16% |  |
| 15 | `BuyBOCode` | 买入营业部编码 | number(10) | ✓ | 95.15% | 买入营业部编码(BuyBOCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(Company... |
| 16 | `SellSalesDepartment` | 卖出营业部 | varchar2(200) | ✓ | 95.16% |  |
| 17 | `SalesBOCode` | 卖出营业部编码 | number(10) | ✓ | 95.16% | 卖出营业部编码(SalesBOCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(Compa... |
| 18 | `IfExclusiveTrading` | 是否为专场 | number(10) | ✓ | 100.0% | 是否为专场(IfExclusiveTrading)：该字段固定为以下常量：1-是 ；2-否 |
| 19 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### TradingType (大宗交易方式)

大宗交易方式(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=2258，得到大宗交易方式的具体描述：1-协议交易，2-盘后定价交易。

### PreCloseDiscountRate (相对昨收折价率(%))

相对昨收折价率(%)(PreCloseDiscountRate)：[1-(大宗交易成交价/当日前收盘价)]*100

### CloseDiscountRate (相对收盘折价率(%))

相对收盘折价率(%)(CloseDiscountRate)：[1-(大宗交易成交价/当日收盘价)]*100

### TurnoverValueRatio (成交额占比(%))

成交额占比(%)(TurnoverValueRatio)：沪深市场:单笔大宗交易成交额/(当日此只股票大宗交易成交额之和+当日交易所公布成交额)*100；北交所:单笔大宗交易成交额/当日交易所公布成交额*100(北交所公布的成交额包含当天的大宗交易成交额)

### VolumeUnit (成交量单位)

成交量单位(VolumeUnit)：该字段固定为 2-股票(股)

### BuyBOCode (买入营业部编码)

买入营业部编码(BuyBOCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到营业部具体信息。

### SalesBOCode (卖出营业部编码)

卖出营业部编码(SalesBOCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到营业部具体信息。

### IfExclusiveTrading (是否为专场)

是否为专场(IfExclusiveTrading)：该字段固定为以下常量：1-是 ；2-否

## SQL示例

```sql
-- 查询 大宗交易成交明细 数据
SELECT *
FROM lc_blocktrading
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
