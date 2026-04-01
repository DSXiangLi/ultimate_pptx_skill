# MF_PersonalInfoChange

**中文名**: 公募基金经理基本资料变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PersonalInfoChange` |
| MySQL表名 | `mf_personalinfochange` |
| 中文名 | 公募基金经理基本资料变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

1.本表记录公募基金历任基金经理、基金经理助理的任职情况包括到任日期和在任与否，以及人员基本资料包括学历、证券从业经验、背景介绍等信息。可以通过所属人员代码关联MF_FundManagerNew，配合使用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书、其他公开信息源。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `PersonalCode` | 所属人员编码 | number(19) | ✗ | 100.0% | 所属人员编码（PersonalCode）：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `PostName` | 职位名称 | number(10) | ✓ | 100.0% | 职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具... |
| 7 | `Name` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 8 | `Gender` | 性别 | number(10) | ✓ | 100.0% | 性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-... |
| 9 | `BirthYMInfo` | 出生年月(文本) | varchar2(20) | ✓ | 8.93% |  |
| 10 | `AccessionDate` | 到任日期 | date | ✗ | 100.0% | 到任日期（AccessionDate）：未成立基金，指首次公告的信息发布日期；后续产品成立后，会更新为产品成立日。 |
| 11 | `DimissionDate` | 离职日期 | date | ✓ | 55.97% |  |
| 12 | `EducationLevel` | 学历 | number(10) | ✓ | 100.0% | 学历(EducationLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到学历... |
| 13 | `ExperienceYear` | 证券从业经历(年) | number(4,1) | ✓ | 98.97% |  |
| 14 | `PracticeDate` | 证券从业日期 | date | ✓ | 98.97% |  |
| 15 | `Background` | 背景介绍 | clob | ✓ | 4.59% |  |
| 16 | `Incumbent` | 在任与否 | number(10) | ✓ | 100.0% | 在任与否（Incumbent），该字段固定以下常量： 1-在任；2-离任 |
| 17 | `Remark` | 备注说明 | varchar2(255) | ✓ | 99.76% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |
| 21 | `BirthDate` | 出生日期 | date | ✓ | 5.09% |  |
| 22 | `Age` | 年龄(岁) | number(10) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### PersonalCode (所属人员编码)

所属人员编码（PersonalCode）：与“基金自然人基本资料表（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。

### PostName (职位名称)

职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具体描述：1-基金经理，2-基金经理助理。

### Gender (性别)

性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-男，2-女。

### AccessionDate (到任日期)

到任日期（AccessionDate）：未成立基金，指首次公告的信息发布日期；后续产品成立后，会更新为产品成立日。

### EducationLevel (学历)

学历(EducationLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1154，得到学历的具体描述：1-博士后，2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他，9-初中及以下。

### Incumbent (在任与否)

在任与否（Incumbent），该字段固定以下常量： 1-在任；2-离任

## SQL示例

```sql
-- 查询 公募基金经理基本资料变动 数据
SELECT *
FROM mf_personalinfochange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
