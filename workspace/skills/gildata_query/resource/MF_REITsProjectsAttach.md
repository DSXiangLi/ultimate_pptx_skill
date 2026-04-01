# MF_REITsProjectsAttach

**中文名**: 基础设施基金(REITs)-项目公司信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsProjectsAttach` |
| MySQL表名 | `mf_reitsprojectsattach` |
| 中文名 | 基础设施基金(REITs)-项目公司信息附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 不定时更新 |
| 字段数量 | 7 |
| 版本 | 1 |

## 表描述

1.内容说明：本表用于记录基础设施公募REITs的招募说明书中，涉及项目公司原始权益人、运营管理机构等相关信息。
2.数据范围：2021年4月起-至今。
3.信息来源：上交所、深交所和证监会官网公布的基金招募说明书、基金合同等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID与基础设施基金(REITs)-项目公司信息（MF_REITsProjects）的ID关联 |
| 3 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB=2400，得到信息类别的具体描... |
| 4 | `InvolvedCode` | 涉及代码 | number(10) | ✗ | 100.0% | 涉及代码（InvolvedCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（Compan... |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID与基础设施基金(REITs)-项目公司信息（MF_REITsProjects）的ID关联

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB=2400，得到信息类别的具体描述：1-原始权益人，2-运营管理机构。

### InvolvedCode (涉及代码)

涉及代码（InvolvedCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（CompanyCode）”关联，得到项目公司的运营管理机构、原始权益人等基本信息。						

## SQL示例

```sql
-- 查询 基础设施基金(REITs)-项目公司信息附表 数据
SELECT *
FROM mf_reitsprojectsattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
