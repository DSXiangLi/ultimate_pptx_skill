# HK_AvaSubPayAble

**中文名**: 港股新股可供认购股数及应缴款项

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_AvaSubPayAble` |
| MySQL表名 | `hk_avasubpayable` |
| 中文名 | 港股新股可供认购股数及应缴款项 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股新股可供认购股数及应缴款项表，记录港股新股申请表格记录的港股可供认购的股数及对应需要缴纳的款项信息。
2.数据范围：2015-01-20年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 6 | `ApplyNumSub` | 申请认购股数 | number(19,0) | ✗ | 100.0% |  |
| 7 | `Payable` | 应缴款项 | number(19,4) | ✓ | 100.0% |  |
| 8 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 9 | `IFAvaAppMax` | 是否可申请最高数目 | number(10) | ✓ | 100.0% | 是否可申请最高数目（IFAvaAppMax）：1-是，2-否。 |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM in (1000,1100,1420)，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### IFAvaAppMax (是否可申请最高数目)

是否可申请最高数目（IFAvaAppMax）：1-是，2-否。

## SQL示例

```sql
-- 查询 港股新股可供认购股数及应缴款项 数据
SELECT *
FROM hk_avasubpayable
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
