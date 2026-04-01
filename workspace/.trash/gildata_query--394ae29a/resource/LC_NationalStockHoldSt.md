# LC_NationalStockHoldSt

**中文名**: A股国家队持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_NationalStockHoldSt` |
| MySQL表名 | `lc_nationalstockholdst` |
| 中文名 | A股国家队持股统计 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.02 |

## 表描述

1.内容说明：本表记录股市国家队成员持有A股的相关信息，包含：持有A股总数，占总股本比例，持有A股数量增减，持有A股数量增减幅度等。
2.数据范围：2003-01-01至今
3.信息来源：聚源

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |   公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `SHID` | 股东ID | number(10) | ✓ | 100.0% | 股东ID（SHID）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联 |
| 6 | `SHName` | 股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 7 | `HoldAShareSum` | 持有A股总数(股) | number(16,0) | ✓ | 100.0% |  |
| 8 | `RestrainedAShare` | 其中:有限售A股数(股) | number(16,0) | ✓ | 19.4% |  |
| 9 | `UnstintedAShare` | 其中:无限售A股数(股) | number(16,0) | ✓ | 35.63% |  |
| 10 | `PCTOfTotalShares` | 占总股本比例(%) | number(10,6) | ✓ | 87.97% |  |
| 11 | `PCTOfFloatShares` | 占流通A股比例(%) | number(10,6) | ✓ | 87.09% |  |
| 12 | `HoldASumChange` | 持有A股数量增减(股) | number(16,0) | ✓ | 80.59% |  |
| 13 | `HoldASumChangeRate` | 持有A股数量增减幅度(%) | number(16,6) | ✓ | 80.59% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

 
公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### SHID (股东ID)

股东ID（SHID）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联

## SQL示例

```sql
-- 查询 A股国家队持股统计 数据
SELECT *
FROM lc_nationalstockholdst
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
