# MF_BankAccountInfo

**中文名**: 公募基金公司银行账号信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BankAccountInfo` |
| MySQL表名 | `mf_bankaccountinfo` |
| 中文名 | 公募基金公司银行账号信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.本表记录基金管理公司银行帐户信息，包括开户银行名称、银行账号登详细信息。
2.历史数据：2006年8月起-至今。
3.信息来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InvestAdvisorCode` | 基金管理公司编号 | number(10) | ✗ | 100.0% | 基金管理公司编号（InvestAdvisorCode）：与“基金管理人概况（MF_InvestAdvisorOutlin... |
| 3 | `InvestAdvisorName` | 基金管理公司名称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 公告日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 公告来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `OpenBankCode` | 开户银行编号 | number(10) | ✓ | 100.0% | 开户银行编号（OpenBankCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 7 | `OpenBankName` | 开户银行名称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `AccountName` | 账户名称 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `AccountNumber` | 银行账号 | varchar2(50) | ✓ | 100.0% |  |
| 10 | `BankIdentifier` | 开户行号 | varchar2(50) | ✓ | 0.4% |  |
| 11 | `BankExchangeStore` | 交换行号 | varchar2(50) | ✓ | 6.99% |  |
| 12 | `InterbankNumber` | 联行行号 | varchar2(50) | ✓ | 11.96% |  |
| 13 | `PaymentSystemNumber` | 人行支付系统行号 | varchar2(50) | ✓ | 12.1% |  |
| 14 | `LargeOnlinePayNumber` | 大额实时支付号 | varchar2(50) | ✓ | 51.08% |  |
| 15 | `IfEffected` | 是否有效 | number(3) | ✓ | 100.0% | 是否有效（IfEffected），该字段固定以下常量：0-否；1-是 |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InvestAdvisorCode (基金管理公司编号)

基金管理公司编号（InvestAdvisorCode）：与“基金管理人概况（MF_InvestAdvisorOutline）”中的“基金管理人编号（InvestAdvisorCode）”关联，得到基金管理人的基本情况。

### OpenBankCode (开户银行编号)

开户银行编号（OpenBankCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到开户银行的基本资料。

### IfEffected (是否有效)

是否有效（IfEffected），该字段固定以下常量：0-否；1-是

## SQL示例

```sql
-- 查询 公募基金公司银行账号信息 数据
SELECT *
FROM mf_bankaccountinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
