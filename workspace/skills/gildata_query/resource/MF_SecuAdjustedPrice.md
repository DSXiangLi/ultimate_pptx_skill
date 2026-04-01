# MF_SecuAdjustedPrice

**中文名**: 公募基金持仓证券调价表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_SecuAdjustedPrice` |
| MySQL表名 | `mf_secuadjustedprice` |
| 中文名 | 公募基金持仓证券调价表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录基金公司披露的对于旗下基金持有证券的调整估值价格信息。
2.数据范围：2004年3月起-至今。
3.信息来源：聚源按照源原始披露整理。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InvestAdvisorCode` | 基金管理人 | number(10) | ✗ | 100.0% | 基金管理人（InvestAdvisorCode）与“基金管理人概况表（MF_InvestAdvisorOutline）”... |
| 4 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 5 | `InnerCode` | 证券内码 | number(10) | ✗ | 100.0% | 证券内码(InnerCode)与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金... |
| 6 | `SecuName` | 证券名称 | varchar2(200) | ✗ | 100.0% |  |
| 7 | `AdjustedMethod` | 调整估值方法类别 | number(10) | ✓ | 100.0% | 调整估值方法类别(AdjustedMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 233... |
| 8 | `AdjustedPrice` | 调整后价格 | number(18,6) | ✓ | 12.56% |  |
| 9 | `CurrencyCode` | 币种 | number(10) | ✓ | 12.56% | 币种(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM... |
| 10 | `Content` | 公告内容 | varchar2(2000) | ✓ | 100.0% |  |
| 11 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.01% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InvestAdvisorCode (基金管理人)

基金管理人（InvestAdvisorCode）与“基金管理人概况表（MF_InvestAdvisorOutline）”中的“基金管理人名称编号（InvestAdvisorCode）”关联，得到基金管理人的具体名称。

### InnerCode (证券内码)

证券内码(InnerCode)与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### AdjustedMethod (调整估值方法类别)

调整估值方法类别(AdjustedMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2338，得到调整估值方法类别的具体描述：1-公允价值法，2-指数收益率法，3-可比公司法，4-估值模型法，5-净资产法，6-其他。

### CurrencyCode (币种)

币种(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM = 1420，得到币种的具体描述：1420-人民币元。

## SQL示例

```sql
-- 查询 公募基金持仓证券调价表 数据
SELECT *
FROM mf_secuadjustedprice
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
