# CT_Personal

**中文名**: 人员表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CT_Personal` |
| MySQL表名 | `ct_personal` |
| 中文名 | 人员表 |
| 路径 | 聚源新版数据库 > 常量库 |
| 更新频率 | T+1工作日 |
| 字段数量 | 21 |
| 版本 | 1.01 |

## 表描述

1、表说明：本表收录与证券市场相关人员的基本信息，目前维护上海证券交易所、深圳证券交易所、北京证券交易所公布的发行审核委员会委员及并购重组审核委员会委员。
2、数据范围：2003年至今
3、信息来源：中国证监会，上海证券交易所，深圳证券交易所，北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `PersonalType` | 类别所属类别 | number(10) | ✓ | 100.0% | 类别所属类别(PersonalType)与(CT_SystemConst)表中的DM字段关联，令LB = 1366，得到... |
| 5 | `PersonalNum` | 人员编号 | number(10) | ✗ | 100.0% |  |
| 6 | `PersonalName` | 姓名 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `WorkPlace` | 单位名称 | varchar2(200) | ✓ | 46.84% |  |
| 8 | `CompanyCode` | 在任单位公司编号 | number(10) | ✓ | 17.88% | 在任单位公司编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Comp... |
| 9 | `Gender` | 性别 | varchar2(2) | ✓ | 30.68% | 性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB=1234，得到性别的具体描述：1-男，... |
| 10 | `BirthY` | 出生年份 | varchar2(6) | ✓ | 25.43% |  |
| 11 | `Education` | 最高学历 | varchar2(50) | ✓ | 8.7% |  |
| 12 | `ProfessionalTitle` | 职称名称 | varchar2(200) | ✓ | 6.07% |  |
| 13 | `Tel` | 电话 | varchar2(100) | ✓ | 0.0% |  |
| 14 | `Fax` | 传真 | varchar2(100) | ✓ | 0.0% |  |
| 15 | `Email` | 邮箱 | varchar2(200) | ✓ | 0.0% |  |
| 16 | `Background` | 简历 | clob | ✓ | 75.72% |  |
| 17 | `MajorName` | 专业 | varchar2(100) | ✓ | 6.23% |  |
| 18 | `PositionName` | 职位名称 | varchar2(200) | ✓ | 37.82% |  |
| 19 | `Remark` | 备注 | varchar2(1000) | ✓ | 27.81% |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PersonalType (类别所属类别)

类别所属类别(PersonalType)与(CT_SystemConst)表中的DM字段关联，令LB = 1366，得到类别所属类别的具体描述：10-基金管理，20-机构研究，30-证监会从属机构委员，40-上交所科创板从属机构委员，50-深交所创业板从属机构委员，60-三板从属机构委员，70-北交所从属机构委员，80-上交所从属机构委员，90-深交所从属机构委员。

### CompanyCode (在任单位公司编号)

在任单位公司编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到人员所在机构的基本信息

### Gender (性别)

性别(Gender)与(CT_SystemConst)表中的DM字段关联，令LB=1234，得到性别的具体描述：1-男，2-女。

## SQL示例

```sql
-- 查询 人员表 数据
SELECT *
FROM ct_personal
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
