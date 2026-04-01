# Bond_BADepositT

**中文名**: 大额存单条款

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BADepositT` |
| MySQL表名 | `bond_badepositt` |
| 中文名 | 大额存单条款 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.记录大额存单的行权条款信息，主要包括转让、提前赎回、提前支取、质押条款。
2.数据范围：2015-08-13 至今
3.信息来源：中债登、货币网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到大... |
| 3 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 4 | `TermType` | 条款类型 | number(10) | ✗ | 100.0% | 条款类型(TermType)与(CT_SystemConst)表中的DM字段关联，令LB = 1982，得到条款类型的具... |
| 5 | `TermRemark` | 条款说明 | varchar2(2000) | ✓ | 98.31% |  |
| 6 | `ValidEndDate` | 有效期截止日 | date | ✓ | 0.0% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 8 | `Remark` | 备注 | varchar2(2000) | ✓ | 1.48% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到大额存单的交易代码、简称等信息。

### TermType (条款类型)

条款类型(TermType)与(CT_SystemConst)表中的DM字段关联，令LB = 1982，得到条款类型的具体描述：1-转让，2-提前赎回，3-提前支取，4-质押。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 大额存单条款 数据
SELECT *
FROM bond_badepositt
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
