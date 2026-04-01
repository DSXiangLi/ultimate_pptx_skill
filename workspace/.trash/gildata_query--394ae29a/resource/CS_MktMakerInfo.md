# CS_MktMakerInfo

**中文名**: 股票做市商信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_MktMakerInfo` |
| MySQL表名 | `cs_mktmakerinfo` |
| 中文名 | 股票做市商信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

内容说明：记录上市公司所对应的做市商名称、编码、加入做市日期和退出做市日期等信息；
数据范围：2022-12-02 至今
信息来源：证券交易所披露做市商加入和退出公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `GilCode` | 聚源代码 | varchar2(12) | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN... |
| 6 | `MarketMaker` | 做市商名称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `MarketMakerCode` | 做市商编码 | number(10) | ✗ | 100.0% |  |
| 8 | `InDate` | 加入日期 | date | ✗ | 100.0% |  |
| 9 | `OutDate` | 退出日期 | date | ✓ | 2.0% |  |
| 10 | `OutReason` | 退出原因 | number(10) | ✓ | 0.0% | 目前暂无披露。  |
| 11 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.0% |  |
| 12 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

### OutReason (退出原因)

目前暂无披露。 

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 股票做市商信息 数据
SELECT *
FROM cs_mktmakerinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
