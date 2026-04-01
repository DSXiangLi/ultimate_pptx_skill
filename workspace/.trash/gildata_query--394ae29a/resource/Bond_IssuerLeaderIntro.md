# Bond_IssuerLeaderIntro

**中文名**: 债券发行人领导人介绍

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IssuerLeaderIntro` |
| MySQL表名 | `bond_issuerleaderintro` |
| 中文名 | 债券发行人领导人介绍 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.02 |

## 表描述

本表收录了债券发行人在任和历任的领导人的简历介绍，包括姓名、性别、出生年月、学历背景、上任离任日期等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码(CompanyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyC... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.94% |  |
| 5 | `LeaderName` | 领导人姓名 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `PersonalCode` | 人员编码 | number(10) | ✓ | 0.0% |  |
| 7 | `Gender` | 性别 | number(10) | ✓ | 91.48% | 性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-... |
| 8 | `BirthYM` | 出生年月 | date | ✓ | 88.42% |  |
| 9 | `BirthYMInfo` | 出生年月(文本) | varchar2(20) | ✓ | 87.23% |  |
| 10 | `EducationLevel` | 学历 | number(10) | ✓ | 83.02% | 学历(EducationLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到学历... |
| 11 | `Background` | 背景介绍 | clob | ✓ | 90.92% |  |
| 12 | `Incumbent` | 在任与否 | number(10) | ✓ | 100.0% | 在任与否(Incumbent)：该字段固定以下常量：1-有；0-无。 |
| 13 | `InDate` | 上任日期 | date | ✓ | 98.01% |  |
| 14 | `OffDate` | 离任日期 | date | ✓ | 61.18% |  |
| 15 | `ConcurrentPost` | 兼职状况 | varchar2(255) | ✓ | 36.39% |  |
| 16 | `Statement` | 变更说明 | varchar2(1000) | ✓ | 98.55% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `Nationality` | 国籍 | number(10) | ✓ | 69.23% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码(CompanyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到相关企业的具体名称、基本信息等。

### Gender (性别)

性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-男，2-女。

### EducationLevel (学历)

学历(EducationLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到学历的具体描述：1-博士后，2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他，9-初中及以下。

### Incumbent (在任与否)

在任与否(Incumbent)：该字段固定以下常量：1-有；0-无。

## SQL示例

```sql
-- 查询 债券发行人领导人介绍 数据
SELECT *
FROM bond_issuerleaderintro
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
