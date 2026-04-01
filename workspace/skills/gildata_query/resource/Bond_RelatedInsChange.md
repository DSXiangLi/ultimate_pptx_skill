# Bond_RelatedInsChange

**中文名**: 债券相关机构变更

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RelatedInsChange` |
| MySQL表名 | `bond_relatedinschange` |
| 中文名 | 债券相关机构变更 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：记录债券相关机构变更的情况
2.数据范围：2016年以后

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等... |
| 3 | `AgentType` | 机构类别 | number(10) | ✗ | 100.0% | 机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM ... |
| 4 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到机构的具体名称、... |
| 5 | `EffectiveDate` | 生效日期 | date | ✓ | 50.04% |  |
| 6 | `CancelDate` | 取消日期 | date | ✓ | 50.04% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 and DM in... |
| 8 | `ChangeReason` | 变更原因 | number(10) | ✓ | 49.89% | 变更原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2416，得到变更... |
| 9 | `Remark` | 备注 | varchar2(1000) | ✓ | 5.83% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### AgentType (机构类别)

机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM IN (144)，得到机构类别的具体描述：144-发行人/发起机构/原始权益人。

### CompanyCode (公司代码)

与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到机构的具体名称、基本信息等。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

### ChangeReason (变更原因)

变更原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2416，得到变更原因的具体描述：1-合并，2-重组，3-改制，4-债务承继，5-债务承继(股权转让）。

## SQL示例

```sql
-- 查询 债券相关机构变更 数据
SELECT *
FROM bond_relatedinschange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
