# MF_FundManEscAttachT

**中文名**: 公募基金经理代任情况附表(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundManEscAttachT` |
| MySQL表名 | `mf_fundmanescattacht` |
| 中文名 | 公募基金经理代任情况附表(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.本表用于记录基金经理代任情况。
2.数据范围：1998年-至今。
3.信息来源：基金定报或其他临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.49% |  |
| 4 | `VacaSerialNumber` | 历次休假序号 | number(10) | ✗ | 100.0% |  |
| 5 | `VacaStartDate` | 休假开始日 | date | ✓ | 100.0% |  |
| 6 | `VacaEndDate` | 休假结束日 | date | ✓ | 93.61% |  |
| 7 | `VacaReason` | 休假原因 | number(10) | ✓ | 100.0% |  |
| 8 | `Notes` | 备注(休假原因) | varchar2(250) | ✓ | 9.1% |  |
| 9 | `EscrowPersonalCode` | 代任经理人员代码 | number(19) | ✗ | 100.0% |  |
| 10 | `IfMutualManager` | 是否为共同管理人 | number(10) | ✓ | 100.0% |  |
| 11 | `EscrowStartDate` | 代任开始日 | date | ✓ | 100.0% |  |
| 12 | `EscrowEndDate` | 代任结束日 | date | ✓ | 93.8% |  |
| 13 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金经理代任情况附表(转型) 数据
SELECT *
FROM mf_fundmanescattacht
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
