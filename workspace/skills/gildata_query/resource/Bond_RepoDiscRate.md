# Bond_RepoDiscRate

**中文名**: 债券回购折扣率表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RepoDiscRate` |
| MySQL表名 | `bond_repodiscrate` |
| 中文名 | 债券回购折扣率表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券回购信息 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1.01 |

## 表描述

1.收录各类回购质押券、所属篮子、折扣率等数据
2.数据范围：2018-5-23 至今
3.信息来源：上交所，深交所，上海清算所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码(InnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债券... |
| 3 | `RepurchaseNature` | 回购类型 | number(10) | ✗ | 100.0% | 回购类型(RepurchaseNature)：该字段固定以下常量：1-上交所三方回购，2-深交所三方回购，3-上交所报价... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `BasketCode` | 所属篮子编码 | number(10) | ✓ | 58.33% | 所属篮子编码(BasketCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2133，得到所属... |
| 6 | `BasketAbbr` | 所属篮子简称 | varchar2(50) | ✓ | 58.33% |  |
| 7 | `DiscountRate` | 折扣率(%) | number(19,8) | ✓ | 100.0% | 折扣率(DiscountRate)：三方回购的折扣率，报价回购的折算率（质押券为债券），报价回购的折算值（质押券为债券E... |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码(InnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债券，债券ETF或货币ETF的交易代码、简称等。

### RepurchaseNature (回购类型)

回购类型(RepurchaseNature)：该字段固定以下常量：1-上交所三方回购，2-深交所三方回购，3-上交所报价回购，4-银行间通用质押式回购

### BasketCode (所属篮子编码)

所属篮子编码(BasketCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2133，得到所属篮子编码的具体描述：1-B001，2-B002，3-B003，4-B004，5-B005，6-B006，7-B007，8-B008，201-篮子1，202-篮子2，203-篮子3，204-篮子4，205-篮子5，206-篮子6，207-篮子7，208-篮子8。

### DiscountRate (折扣率(%))

折扣率(DiscountRate)：三方回购的折扣率，报价回购的折算率（质押券为债券），报价回购的折算值（质押券为债券ETF或货币ETF）

## SQL示例

```sql
-- 查询 债券回购折扣率表 数据
SELECT *
FROM bond_repodiscrate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
