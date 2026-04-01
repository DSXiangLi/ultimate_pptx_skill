# HK_SecuCodeTable

**中文名**: 港股证券交易代码表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SecuCodeTable` |
| MySQL表名 | `hk_secucodetable` |
| 中文名 | 港股证券交易代码表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 33 |
| 版本 | 1.02 |

## 表描述

1.内容说明：新建港股证券交易代码表，记录当前时点处于正常上市状态的港交所可交易券种的常用信息。
2.数据范围：无。
3.信息来源：恒生聚源整理。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 4 | `RelStockInnerCode` | 关联正股内部编码 | number(10) | ✓ | 100.0% | 关联正股内部编码（RelStockInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（... |
| 5 | `SecuCode` | 证券代码 | varchar2(10) | ✗ | 100.0% |  |
| 6 | `ChiNameAbbr` | 中文简称 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `EngNameAbbr` | 英文简称 | varchar2(50) | ✓ | 99.12% |  |
| 8 | `ChiSpelling` | 拼音缩写 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `SecuMarket` | 证券市场 | varchar2(20) | ✓ | 100.0% | 证券市场（SecuMarket）：包括香港联交所。 |
| 10 | `SecuCategory` | 证券类别 | varchar2(40) | ✓ | 100.0% | 证券类别（SecuCategory）：包括常见的港股证券类别，如港股、红筹股、H股、港股临时代码、ETF基金、信托基金、... |
| 11 | `ListedDate` | 上市日期 | varchar2(10) | ✓ | 99.14% |  |
| 12 | `ListedSector` | 上市板块 | varchar2(20) | ✓ | 100.0% | 上市板块（ListedSector）：包括主板、创业板。 |
| 13 | `ListedState` | 上市状态 | varchar2(20) | ✓ | 100.0% | 上市状态（ListedState）：包括正常交易、停牌、临时交易主代码停牌。 |
| 14 | `TradingUnit` | 买卖单位(股/手) | number(18,1) | ✓ | 99.14% |  |
| 15 | `Currency` | 交易货币 | varchar2(20) | ✓ | 100.0% | 交易货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM I... |
| 16 | `AccountDay` | 财年结算日 | varchar2(5) | ✓ | 15.16% |  |
| 17 | `MinPriceChg` | 最小变动价格 | number(18,3) | ✓ | 25.18% |  |
| 18 | `ControllerName` | 实际控制人 | varchar2(200) | ✓ | 15.16% |  |
| 19 | `InduCHS` | 恒生三级行业分类 | varchar2(100) | ✓ | 15.23% |  |
| 20 | `HKSTMark` | 港股通标识 | varchar2(8) | ✓ | 100.0% |  |
| 21 | `HSIndexMark` | 恒生指数成分股标识 | varchar2(8) | ✓ | 100.0% |  |
| 22 | `ShortSellMark` | 可卖空标识 | varchar2(8) | ✓ | 100.0% |  |
| 23 | `CASMark` | 收市竞价标识 | varchar2(8) | ✓ | 100.0% |  |
| 24 | `VCMMark` | 市价调节标识 | varchar2(8) | ✓ | 100.0% |  |
| 25 | `StampDutyMark` | 须缴纳印花税标识 | varchar2(8) | ✓ | 100.0% |  |
| 26 | `CCASSMark` | 纳入中央结算标识 | varchar2(8) | ✓ | 100.0% |  |
| 27 | `StockOptionsMark` | 纳入股票期权标识 | varchar2(8) | ✓ | 100.0% |  |
| 28 | `StockFuturesMark` | 纳入股票期货标识 | varchar2(8) | ✓ | 100.0% |  |
| 29 | `OtherName` | 曾用名 | varchar2(200) | ✓ | 5.66% |  |
| 30 | `ISIN` | ISIN | varchar2(20) | ✓ | 80.22% |  |
| 31 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 32 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 33 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### RelStockInnerCode (关联正股内部编码)

关联正股内部编码（RelStockInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到非港交所上市指数的交易代码、简称等。

### SecuMarket (证券市场)

证券市场（SecuMarket）：包括香港联交所。

### SecuCategory (证券类别)

证券类别（SecuCategory）：包括常见的港股证券类别，如港股、红筹股、H股、港股临时代码、ETF基金、信托基金、牛熊证、衍生权证等。

### ListedSector (上市板块)

上市板块（ListedSector）：包括主板、创业板。

### ListedState (上市状态)

上市状态（ListedState）：包括正常交易、停牌、临时交易主代码停牌。

### Currency (交易货币)

交易货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (6010 ,3030, 1160, 1320, 3000, 1420, 1000, 1100, 5010, 1210)，得到交易货币的具体描述：1000-美元，1100-港元，1160-日本元，1210-澳门元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。

## SQL示例

```sql
-- 查询 港股证券交易代码表 数据
SELECT *
FROM hk_secucodetable
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
