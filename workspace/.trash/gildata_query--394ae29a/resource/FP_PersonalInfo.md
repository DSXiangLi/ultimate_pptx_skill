# FP_PersonalInfo

**中文名**: 金融产品投资经理基本资料

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_PersonalInfo` |
| MySQL表名 | `fp_personalinfo` |
| 中文名 | 金融产品投资经理基本资料 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品主体信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

内容说明：本表收录金融产品（券商资管、保险资管、养老金产品）投资经理的姓名，性别，所在机构，国籍，背景介绍等基本资料信息
信息来源：证券、资产管理公司、保险公司官网。
数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PersonalCode` | 所属人员代码 | number(10) | ✗ | 100.0% |  |
| 3 | `ManagerName` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 4 | `EnglishName` | 英文名 | varchar2(30) | ✓ | 0.04% |  |
| 5 | `Gender` | 性别 | varchar2(12) | ✓ | 87.52% | 性别(Gender)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到... |
| 6 | `BirthYM` | 出生年月 | varchar2(20) | ✓ | 3.03% |  |
| 7 | `Nationality` | 国籍 | varchar2(12) | ✓ | 58.18% |  |
| 8 | `Education` | 最高学历 | varchar2(12) | ✓ | 86.36% | 最高学历(Education)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 9 | `CompanyName` | 所在机构 | varchar2(12) | ✓ | 100.0% | 所在机构(CompanyName)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 10 | `PracticeDate` | 证券从业日期 | date | ✓ | 35.48% |  |
| 11 | `Background` | 背景介绍 | clob | ✓ | 87.84% |  |
| 12 | `PersonalData` | 个人资料 | blob | ✓ | 5.4% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Gender (性别)

性别(Gender)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到性别的具体描述：FCC000000YHS-男，FCC000000YHT-女。

### Education (最高学历)

最高学历(Education)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到最高学历的具体描述：FCC000000YHU-博士后，FCC000000YHV-博士，FCC000000YHW-硕士，FCC000000YHX-本科，FCC000000YHY-大专，FCC000000YHZ-高中，FCC000000YI0-中专。

### CompanyName (所在机构)

所在机构(CompanyName)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

## SQL示例

```sql
-- 查询 金融产品投资经理基本资料 数据
SELECT *
FROM fp_personalinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
