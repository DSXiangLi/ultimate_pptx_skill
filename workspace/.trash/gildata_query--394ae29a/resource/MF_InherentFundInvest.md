# MF_InherentFundInvest

**中文名**: 公募基金管理人固有资金投资

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InherentFundInvest` |
| MySQL表名 | `mf_inherentfundinvest` |
| 中文名 | 公募基金管理人固有资金投资 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 不定时更新 |
| 字段数量 | 19 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金管理公司持有的旗下基金的份额变动信息，变动方式包括：认购、申购、赎回、红利再投资、其他等。
2.历史数据：1999年1月起-至今。
3.数据来源：基金公司披露的临时报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ContractEffectiveDate` | 合同生效公告日 | date | ✓ | 7.59% |  |
| 7 | `ApplyingStartDate` | 变动起始日 | date | ✗ | 100.0% |  |
| 8 | `ApplyingEndDate` | 变动截止日 | date | ✓ | 99.96% |  |
| 9 | `ChangeType` | 变动方式 | number(10) | ✓ | 100.0% | 变动方式(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1540，得到变动方式... |
| 10 | `InvestAdvisorCode` | 基金管理人编号 | number(10) | ✗ | 100.0% | 基金管理人编号（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutlin... |
| 11 | `InvestAdvisorName` | 基金管理人名称 | varchar2(200) | ✓ | 100.0% |  |
| 12 | `CurrentShares` | 本次数量 | number(18,2) | ✓ | 99.34% |  |
| 13 | `AssetCustodianSum` | 涉及金额 | number(19,4) | ✓ | 2.41% |  |
| 14 | `ApplyingExpense` | 涉及费用 | number(19,4) | ✓ | 3.77% |  |
| 15 | `AccuShares` | 累计持有数量 | number(18,2) | ✓ | 99.27% |  |
| 16 | `Remark` | 备注 | varchar2(1000) | ✓ | 95.22% |  |
| 17 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ChangeType (变动方式)

变动方式(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1540，得到变动方式的具体描述：1-认购，2-申购，3-赎回，4-红利再投资，5-收益结转，9-其他。

### InvestAdvisorCode (基金管理人编号)

基金管理人编号（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutline）”中的“基金管理人名称编号（InvestAdvisorCode）”关联，得到基金管理人的基本情况。

## SQL示例

```sql
-- 查询 公募基金管理人固有资金投资 数据
SELECT *
FROM mf_inherentfundinvest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
