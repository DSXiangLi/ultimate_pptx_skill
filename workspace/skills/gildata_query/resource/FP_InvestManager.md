# FP_InvestManager

**中文名**: 金融产品投资经理

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_InvestManager` |
| MySQL表名 | `fp_investmanager` |
| 中文名 | 金融产品投资经理 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品主体信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表收录金融产品（券商资管、保险资管、养老金产品）投资经理的姓名，性别，职位，背景介绍等信息
2.信息来源：证券、资产管理公司、保险公司官网。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `PersonalCode` | 人员代码 | number(10) | ✗ | 100.0% | 人员代码（PersonalCode）：与“ 金融产品投资经理基本资料(FP_PersonalInfo)”中的“所属人员代... |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.99% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `PostName` | 职位名称 | varchar2(12) | ✓ | 100.0% | 职位名称(PostName)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关... |
| 8 | `ManagerName` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 9 | `AccessionDate` | 任期开始日期 | date | ✗ | 100.0% |  |
| 10 | `DimissionDate` | 任期结束日期 | date | ✓ | 90.36% |  |
| 11 | `Incumbent` | 在任与否 | varchar2(12) | ✓ | 99.98% | 在任与否(Incumbent)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 12 | `Remark` | 备注说明 | varchar2(500) | ✓ | 98.85% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### PersonalCode (人员代码)

人员代码（PersonalCode）：与“ 金融产品投资经理基本资料(FP_PersonalInfo)”中的“所属人员代码（PersonalCode ）”关联，得到金融产品投资经理的基本信息。

### PostName (职位名称)

职位名称(PostName)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到职位名称的具体描述：FCC000000YI1-投资经理，FCC000000YI2-投资经理助理。

### Incumbent (在任与否)

在任与否(Incumbent)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到在任与否的具体描述：FCC000000005-是，FCC000000006-否。

## SQL示例

```sql
-- 查询 金融产品投资经理 数据
SELECT *
FROM fp_investmanager
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
