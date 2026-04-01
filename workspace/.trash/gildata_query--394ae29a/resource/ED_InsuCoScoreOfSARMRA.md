# ED_InsuCoScoreOfSARMRA

**中文名**: 保险公司SARMRA评估得分

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `ED_InsuCoScoreOfSARMRA` |
| MySQL表名 | `ed_insucoscoreofsarmra` |
| 中文名 | 保险公司SARMRA评估得分 |
| 路径 | 聚源新版数据库 > 机构数据库 > 保险公司 |
| 更新频率 | 年更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

内容说明：本表用于记录保险公司偿付能力风险管理能力（SARMRA）的评估得分结果，SARMRA是偿二代第二支柱的重要内容，其将保险公司的风险管理能力与资本要求相挂钩，即保险公司的风险管理能力越强，资本要求越低；风险管理能力越差，资本要求越高。
数据范围：包含再保险公司、财产险公司、人身险公司、保险集团公司
信息来源：中国保险行业协会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | number(10) | ✓ | 93.72% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令where LB = 2195 ... |
| 4 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `BasicEnvironmentRM` | 风险管理基础与环境 | number(18,6) | ✓ | 93.72% |  |
| 7 | `ObjectToolRM` | 风险管理目标与工具 | number(18,6) | ✓ | 93.47% |  |
| 8 | `InsuranceRM` | 保险风险管理 | number(18,6) | ✓ | 93.72% |  |
| 9 | `MarketRM` | 市场风险管理 | number(18,6) | ✓ | 93.47% |  |
| 10 | `CreditRM` | 信用风险管理 | number(18,6) | ✓ | 93.97% |  |
| 11 | `OperationRM` | 操作风险管理 | number(18,6) | ✓ | 93.47% |  |
| 12 | `StrategyRM` | 战略风险管理 | number(18,6) | ✓ | 93.47% |  |
| 13 | `GoodwillRM` | 声誉风险管理 | number(18,6) | ✓ | 93.47% |  |
| 14 | `LiquidityRM` | 流动性风险管理 | number(18,6) | ✓ | 93.47% |  |
| 15 | `TotalScore` | 总分 | number(18,6) | ✓ | 98.74% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令where LB = 2195 and DM in (800000300)，得到信息来源的具体描述：

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到公司的其他基本资料。

## SQL示例

```sql
-- 查询 保险公司SARMRA评估得分 数据
SELECT *
FROM ed_insucoscoreofsarmra
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
