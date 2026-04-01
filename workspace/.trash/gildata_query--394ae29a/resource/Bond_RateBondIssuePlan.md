# Bond_RateBondIssuePlan

**中文名**: 利率债发行计划

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RateBondIssuePlan` |
| MySQL表名 | `bond_ratebondissueplan` |
| 中文名 | 利率债发行计划 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

内容说明：记录财政部披露利率债供给安排。
数据范围：1994年-至今
信息来源：财政部、中债登、货币网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `BondNature` | 债券性质 | number(10) | ✓ | 100.0% | 债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 2628 AND IV... |
| 3 | `BondType` | 债券类型 | number(10) | ✗ | 100.0% | 债券类型(BondType)与(CT_SystemConst)表中的DM字段关联，令LB = 2628 AND (IVA... |
| 4 | `IssueDate` | 发行日期 | date | ✗ | 100.0% |  |
| 5 | `Maturity` | 发行期限(年) | number(10,4) | ✗ | 100.0% |  |
| 6 | `IssueType` | 发行类型 | number(10) | ✓ | 100.0% | 发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB=1316 AND DM in... |
| 7 | `IntPaymentMethod` | 付息方式 | number(10) | ✓ | 90.66% | 付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，... |
| 8 | `CompoundMethod` | 计息方式 | number(10) | ✓ | 91.58% | 计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 9 | `IssueSize` | 发行总额(百万元) | number(19,4) | ✓ | 99.84% |  |
| 10 | `CompanyCode` | 发行人 | number(10) | ✗ | 100.0% |  |
| 11 | `InnerCode` | 关联债券内部编码 | number(10) | ✓ | 91.44% | 关联债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode... |
| 12 | `CrossExchange` | 是否跨市场 | number(10) | ✓ | 91.47% | 是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BondNature (债券性质)

债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 2628 AND IVALUE = 1，得到债券性质的具体描述：100-国债，200-地方政府债，300-政策性金融债，400-同业存单。

### BondType (债券类型)

债券类型(BondType)与(CT_SystemConst)表中的DM字段关联，令LB = 2628 AND (IVALUE = 2 OR DM = 400)，得到债券类型的具体描述：400-同业存单，10001-记账式附息国债，10002-记账式贴现国债，10003-凭证式国债，10004-电子式国债，10005-特别国债，20001-地方政府一般债，20002-地方政府专项债，30001-国家开发银行债，30002-进出口银行债，30003-农业发展银行债。

### IssueType (发行类型)

发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB=1316 AND DM in (10,30)，得到发行类型的具体描述：10-首发，30-增发。

### IntPaymentMethod (付息方式)

付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，得到付息方式的具体描述：1-每年付息，2-半年付息，3-到期一次还本付息，4-按季付息，5-按月付息。

### CompoundMethod (计息方式)

计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AND DM in (1,3,4,5,6)，得到计息方式的具体描述：1-单利(固定利率)，3-浮动利率，4-累进利率，5-贴现，6-无序利率。

### InnerCode (关联债券内部编码)

关联债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。注意：对于块市场券，仅提供银行间市场的InnerCode，需要用银行间市场的InnerCode进行查询。

### CrossExchange (是否跨市场)

是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否跨市场的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 利率债发行计划 数据
SELECT *
FROM bond_ratebondissueplan
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
