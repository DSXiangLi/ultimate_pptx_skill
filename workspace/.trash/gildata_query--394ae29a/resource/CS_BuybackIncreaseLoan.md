# CS_BuybackIncreaseLoan

**中文名**: 股票回购增持再贷款

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_BuybackIncreaseLoan` |
| MySQL表名 | `cs_buybackincreaseloan` |
| 中文名 | 股票回购增持再贷款 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定期更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

收录上市公司借贷中股票回购增持再贷款的数据
数据范围:2023至今
信息来源:上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EventDesc` | 事件描述 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% |  |
| 7 | `LoanUseCategory` | 贷款用途类型 | number(10) | ✓ | 100.0% |  |
| 8 | `LoanUse` | 贷款用途 | varchar2(500) | ✓ | 99.64% |  |
| 9 | `Borrower` | 借入方 | varchar2(50) | ✗ | 100.0% |  |
| 10 | `BorrowerCode` | 借入方企业编号 | number(10) | ✓ | 99.76% |  |
| 11 | `Lender` | 借出方 | varchar2(50) | ✗ | 100.0% |  |
| 12 | `LenderCode` | 借出方企业编号 | number(10) | ✓ | 87.22% |  |
| 13 | `Guarantor` | 担保方 | varchar2(50) | ✓ | 0.71% |  |
| 14 | `GuarantorCode` | 担保方企业编号 | number(10) | ✓ | 0.47% |  |
| 15 | `LoanValueCeiling` | 贷款金额上限(万元) | number(19,4) | ✓ | 97.4% |  |
| 16 | `LoanValueFloor` | 贷款金额下限(万元) | number(19,4) | ✓ | 1.3% |  |
| 17 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% |  |
| 18 | `LoanTerm` | 借贷期限(月) | varchar2(20) | ✗ | 100.0% |  |
| 19 | `LendBeginDate` | 借贷起始日 | date | ✓ | 1.89% |  |
| 20 | `LendEndDate` | 借贷截止日 | date | ✓ | 1.18% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 股票回购增持再贷款 数据
SELECT *
FROM cs_buybackincreaseloan
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
