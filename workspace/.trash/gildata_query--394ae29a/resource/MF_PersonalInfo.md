# MF_PersonalInfo

**中文名**: 公募基金经理基本资料

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PersonalInfo` |
| MySQL表名 | `mf_personalinfo` |
| 中文名 | 公募基金经理基本资料 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.02 |

## 表描述

1.本表基金经理的基本资料包括学历、证券从业经验、背景介绍等信息，其中背景介绍为聚源依据历史公开信息自行拼接而成，一般涵盖基金经理的性别、国籍、学历、历史任职公司、历史管理基金等，相对招募说明书、基金经理变更等公告披露内容更全面。如需公告披露原文，可通过MF_PersonalInfoChange中的背景介绍获取！
涉及计算字段规则如下：
（1）ExperienceTime-证券从业经历(年)：在任的，ExperienceTime=当前日期-证券从业日期；已不在任的，ExperienceTime=最晚离任日期-证券从业日期；
（2）ExperienceTimeII-任职经历 ：在任的，ExperienceTimeII=当前日期-任职起始日期；已不在任的，ExperienceTimeII=最晚离任日期-最早任职日期；没有在任基金的，ExperienceTimeII=null。
本表可以通过所属人员代码关联MF_FundManagerNew，配合使用。基金经理不同尺寸照片可通过关联MF_FundManPhoAttach的RID字段获取。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书、其他公开信息源。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PersonalCode` | 所属人员编码 | number(19) | ✗ | 100.0% |  |
| 3 | `ChineseName` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 4 | `Gender` | 性别 | number(10) | ✓ | 100.0% | 性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-... |
| 5 | `Nationality` | 国籍 | number(10) | ✓ | 99.39% | 国籍(Nationality)与(CT_SystemConst)表中的DM字段关联，令LB = 1023 AND DM ... |
| 6 | `BirthYMInfo` | 出生年月(文本) | varchar2(20) | ✓ | 12.12% |  |
| 7 | `Education` | 最高学历 | number(10) | ✓ | 99.82% | 最高学历(Education)与(CT_SystemConst)表中的DM字段关联，令LB = 1154 AND DM<... |
| 8 | `PracticeDate` | 证券从业日期 | date | ✓ | 97.17% |  |
| 9 | `ExperienceTime` | 证券从业经历(年) | number(4,1) | ✓ | 97.17% |  |
| 10 | `ExperienceTimeII` | 任职经历 | number(4,1) | ✓ | 97.67% |  |
| 11 | `Background` | 背景介绍 | clob | ✓ | 1.88% | 背景介绍(Background)：本字段为聚源依据历史公开信息自行拼接而成，一般涵盖基金经理的性别、国籍、学历、历史任职... |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |
| 15 | `PersonalData` | 个人资料 | blob | ✓ | 2.01% | 不同尺寸的基金经理照片可以通过本表ID，关联附表(MF_FundManPhoAttach)的RID字段获取 |
| 16 | `FileType` | 文件格式 | number(10) | ✓ | 90.36% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 17 | `IDCardNum` | 身份证 | varchar2(50) | ✓ | 0.0% |  |
| 18 | `PassportNum` | 护照 | varchar2(100) | ✓ | 0.0% |  |
| 19 | `OtherName` | 曾用名 | varchar2(30) | ✓ | 0.01% |  |
| 20 | `EnglishName` | 英文名 | varchar2(30) | ✓ | 0.61% |  |
| 21 | `BirthDate` | 出生日期 | date | ✓ | 5.56% |  |
| 22 | `ProQualifi` | 专业资格 | varchar2(100) | ✓ | 0.0% |  |

## 字段说明

### Gender (性别)

性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB = 1234，得到性别的具体描述：1-男，2-女。

### Nationality (国籍)

国籍(Nationality)与(CT_SystemConst)表中的DM字段关联，令LB = 1023 AND DM IN (110,116,122,132,142,143,303,304,305,501,502,601,609)，得到国籍的具体描述：110-中国香港，116-日本，122-马来西亚，132-新加坡，142-中国，143-中国台湾，303-英国，304-德国，305-法国，501-加拿大，502-美国，601-澳大利亚，609-新西兰。

### Education (最高学历)

最高学历(Education)与(CT_SystemConst)表中的DM字段关联，令LB = 1154 AND DM<>1，得到最高学历的具体描述：2-博士，3-硕士，4-本科，5-大专，6-高中，7-中专，8-其他，9-初中及以下。

### Background (背景介绍)

背景介绍(Background)：本字段为聚源依据历史公开信息自行拼接而成，一般涵盖基金经理的性别、国籍、学历、历史任职公司、历史管理基金等，相对招募说明书、基金经理变更等公告披露内容更全面。如需公告披露原文，可通过MF_PersonalInfoChange中的背景介绍获取！

### PersonalData (个人资料)

不同尺寸的基金经理照片可以通过本表ID，关联附表(MF_FundManPhoAttach)的RID字段获取

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 公募基金经理基本资料 数据
SELECT *
FROM mf_personalinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
