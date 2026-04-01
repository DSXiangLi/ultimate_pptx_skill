# LC_SHSCEliStocks

**中文名**: 沪港通合资格股份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSCEliStocks` |
| MySQL表名 | `lc_shscelistocks` |
| 中文名 | 沪港通合资格股份 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.收录沪港通业务中，各类交易（可买入及卖出、只可卖出、可进行保证金交易、可进行担保卖空）的合资格股票的最新清单以及变动情况。
2.历史数据：2014年11月起-至今
3.数据来源：聚源按照上交所、港交所披露整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 	 交易类型(TradingType):与(CT_SystemConst)表中的DM字段关联,令LB = 1844 an... |
| 3 | `TargetCategory` | 标的类别 | number(10) | ✗ | 100.0% | 标的类别(TargetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1851，得到... |
| 4 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：当TradingType=1时，与“证券主表（SecuMain）”中的“内部编码（I... |
| 5 | `SecuCode` | 证券代码 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `SecuAbbr` | 证券简称 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `InDate` | 开始日期 | date | ✗ | 100.0% |  |
| 8 | `OutDate` | 截止日期 | date | ✓ | 36.57% |  |
| 9 | `Flag` | 是否交易标的 | number(10) | ✓ | 100.0% | 是否交易标的（Flag），该字段固定以下常量：1-是；2-否 |
| 10 | `CCASSCode` | CCASS股份编码 | varchar2(50) | ✓ | 87.78% |  |
| 11 | `ParValue` | 面值(人民币) | varchar2(50) | ✓ | 87.78% |  |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

	
交易类型(TradingType):与(CT_SystemConst)表中的DM字段关联,令LB = 1844 and DM in (1,2)得到交易类型的具体描述.1-沪股通，2-港股通（沪）

### TargetCategory (标的类别)

标的类别(TargetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1851，得到标的类别的具体描述：1-可买入及卖出，2-只可卖出，3-可进行保证金交易，4-可进行担保卖空，5-触发持股比例限制暂停买入。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：当TradingType=1时，与“证券主表（SecuMain）”中的“内部编码（InnerCode）”关联，得到股票的交易代码、简称等；当TradingType=2时，与“港股证券主表（HK_SecuMain）”中的“内部编码（InnerCode）”关联，得到股票的交易代码、简称等；

### Flag (是否交易标的)

是否交易标的（Flag），该字段固定以下常量：1-是；2-否

## SQL示例

```sql
-- 查询 沪港通合资格股份 数据
SELECT *
FROM lc_shscelistocks
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
