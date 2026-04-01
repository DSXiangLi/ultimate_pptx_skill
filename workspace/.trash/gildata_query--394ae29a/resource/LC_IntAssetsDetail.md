# LC_IntAssetsDetail

**中文名**: 公司研发投入与产出

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IntAssetsDetail` |
| MySQL表名 | `lc_intassetsdetail` |
| 中文名 | 公司研发投入与产出 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表附注 |
| 更新频率 | 不定期更新 |
| 字段数量 | 22 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录上市公司研发投入相关数据，主要包括研发费用投入总额、占比，研发人员构成、占比等信息。
2.数据范围：2014年至今
3.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并（IfMerged）固定常量：1-合并，2-母公司 |
| 8 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)固定常量：2-否，1-是 |
| 9 | `ExpensedRDInput` | 费用化研发投入(元) | number(19,4) | ✓ | 82.31% |  |
| 10 | `CapitalizedRDInput` | 资本化研发投入(元) | number(19,4) | ✓ | 70.13% |  |
| 11 | `TotalRDInput` | 研发投入合计(元) | number(19,4) | ✓ | 99.46% |  |
| 12 | `RDInputRatio` | 研发投入占营业收入比例(%) | number(19,6) | ✓ | 99.2% |  |
| 13 | `CapitalizedRDInputR` | 资本化研发投入占比(%) | number(6,2) | ✓ | 70.31% |  |
| 14 | `RDStaffNum` | 研发人员数量 | number(6,0) | ✓ | 59.88% |  |
| 15 | `RDStaffNumRatio` | 研发人员数量占比(%) | number(6,2) | ✓ | 59.44% |  |
| 16 | `CoreTechnicalStaffNum` | 核心技术人员数量 | number(6,0) | ✓ | 2.9% |  |
| 17 | `CoreTechnicalStaffR` | 核心技术人员数量占比(%) | number(6,2) | ✓ | 2.89% |  |
| 18 | `CoreTechnologyOutput` | 核心技术营业收入(元) | number(19,4) | ✓ | 2.34% |  |
| 19 | `CoreTechnologyOutputR` | 核心技术营业收入占比(%) | number(19,6) | ✓ | 2.31% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (110101,110102,110103,110104,110105,120102,120103,120104,120105)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)。

### IfMerged (是否合并)

是否合并（IfMerged）固定常量：1-合并，2-母公司

### IfAdjusted (是否调整)

是否调整(IfAdjusted)固定常量：2-否，1-是

## SQL示例

```sql
-- 查询 公司研发投入与产出 数据
SELECT *
FROM lc_intassetsdetail
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
