# Bond_CBSPPI

**中文名**: 中债SPPI

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBSPPI` |
| MySQL表名 | `bond_cbsppi` |
| 中文名 | 中债SPPI |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录中债金融估值中心发布的SPPI测试结果，包括是否通过，未通过原因，使权不重大的购入价条件（剩余面值、购入价下限），权的价值等
2.数据范围：2018年至今
3.信息来源：中债金融估值中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 计算日 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `IfPassed` | 是否通过 | number(10) | ✗ | 100.0% | 是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM IN... |
| 5 | `Reason` | 未通过的原因 | varchar2(1000) | ✓ | 7.18% |  |
| 6 | `OutstandingPar` | 剩余面值 | number(12,6) | ✓ | 5.33% | 剩余面值(OutstandingPar)：使权不重大的购入价条件，以两个数字的形式展示，第一个数字表示计算日该债券的剩余... |
| 7 | `PriceFloor` | 购入价下限 | number(18,6) | ✓ | 5.33% | 购入价下限(PriceFloor)：使权不重大的购入价条件，以两个数字的形式展示，第二个数字表示可接受的购入价下限，对于... |
| 8 | `OptionValue` | 权的价值 | number(18,8) | ✓ | 5.32% |  |
| 9 | `OtherCondition` | 其他条件 | varchar2(100) | ✓ | 5.79% | 其他条件(OtherCondition)：通过查看系统常量表LB=2215的CVALUE值可得到索引的具体内容。 |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

### IfPassed (是否通过)

是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM IN (1,2)，得到是否通过的具体描述：1-是，2-否。

### OutstandingPar (剩余面值)

剩余面值(OutstandingPar)：使权不重大的购入价条件，以两个数字的形式展示，第一个数字表示计算日该债券的剩余面值

### PriceFloor (购入价下限)

购入价下限(PriceFloor)：使权不重大的购入价条件，以两个数字的形式展示，第二个数字表示可接受的购入价下限，对于溢/折价购入的债券，若购入价大于该可接受的购入价下限，则认为权的价值在购入日不重大。

### OtherCondition (其他条件)

其他条件(OtherCondition)：通过查看系统常量表LB=2215的CVALUE值可得到索引的具体内容。

## SQL示例

```sql
-- 查询 中债SPPI 数据
SELECT *
FROM bond_cbsppi
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
