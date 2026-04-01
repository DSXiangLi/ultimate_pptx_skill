# Bond_IssuerCrLineDet

**中文名**: 债券发行人授信明细情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IssuerCrLineDet` |
| MySQL表名 | `bond_issuercrlinedet` |
| 中文名 | 债券发行人授信明细情况 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 滚动更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.反映银行等机构给予债券发行人的授信明细情况。
2.包括授信额度、授信说明、使用情况等。
3.数据范围：2005-05-26 至今
4.信息来源：募集说明书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `CreditEntityName` | 授信机构名称 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `CreditEntityCode` | 授信机构编号 | number(10) | ✓ | 88.63% |  |
| 7 | `AmountOfCreditLine` | 授信额度(亿元) | number(18,10) | ✓ | 99.88% |  |
| 8 | `AmountOfDrawdown` | 已使用额度(亿元) | number(18,10) | ✓ | 97.03% |  |
| 9 | `OutstandingAmount` | 未使用额度(亿元) | number(18,10) | ✓ | 93.85% |  |
| 10 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 债券发行人授信明细情况 数据
SELECT *
FROM bond_issuercrlinedet
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
