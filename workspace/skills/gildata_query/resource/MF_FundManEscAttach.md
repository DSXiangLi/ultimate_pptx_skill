# MF_FundManEscAttach

**中文名**: 公募基金经理代任情况附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundManEscAttach` |
| MySQL表名 | `mf_fundmanescattach` |
| 中文名 | 公募基金经理代任情况附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.本表以产品为维度记录公募基金管理人休假及代任情况。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。
4.本表RID与公募基金经理(新)MF_FundManagerNew的ID相关联。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“公募基金经理(新)MF_FundManagerNew”中的“ID”关联。 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.47% |  |
| 4 | `VacaSerialNumber` | 历次休假序号 | number(10) | ✗ | 100.0% |  |
| 5 | `VacaStartDate` | 休假开始日 | date | ✓ | 100.0% |  |
| 6 | `VacaEndDate` | 休假结束日 | date | ✓ | 93.32% |  |
| 7 | `VacaReason` | 休假原因 | number(10) | ✓ | 100.0% | 休假原因(VacaReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2460，得到休假原因... |
| 8 | `Notes` | 备注(休假原因) | varchar2(250) | ✓ | 9.29% |  |
| 9 | `EscrowPersonalCode` | 代任经理人员代码 | number(19) | ✗ | 100.0% | 代任经理人员代码(EscrowPersonalCode)：与“基金自然人基本资料表（MF_PersonalInfo）”中... |
| 10 | `IfMutualManager` | 是否为共同管理人 | number(10) | ✓ | 100.0% | 是否为共同管理人(IfMutualManager)与(CT_SystemConst)表中的DM字段关联，令LB=999 ... |
| 11 | `EscrowStartDate` | 代任开始日 | date | ✓ | 100.0% |  |
| 12 | `EscrowEndDate` | 代任结束日 | date | ✓ | 93.52% |  |
| 13 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“公募基金经理(新)MF_FundManagerNew”中的“ID”关联。

### VacaReason (休假原因)

休假原因(VacaReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2460，得到休假原因的具体描述：1-产假，2-病假，3-个人原因，4-外出培训，999-其他。

### EscrowPersonalCode (代任经理人员代码)

代任经理人员代码(EscrowPersonalCode)：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。

### IfMutualManager (是否为共同管理人)

是否为共同管理人(IfMutualManager)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否为共同管理人的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金经理代任情况附表 数据
SELECT *
FROM mf_fundmanescattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
