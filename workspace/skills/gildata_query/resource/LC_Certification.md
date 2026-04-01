# LC_Certification

**中文名**: 企业认定情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Certification` |
| MySQL表名 | `lc_certification` |
| 中文名 | 企业认定情况 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

收录企业各种资质认证情况，包括企业认定单位、企业认定类型、企业认定时间和认定取消时间等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `IfCertified` | 企业认定与否 | number(10) | ✓ | 100.0% | 企业认定与否(IfCertified)，该字段固定以下常量：1-是；0-否 |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.97% |  |
| 6 | `CetificationTime` | 企业认定时间 | date | ✓ | 80.07% |  |
| 7 | `CertCancelTime` | 认定取消时间 | date | ✓ | 0.35% |  |
| 8 | `Organization` | 企业认定单位 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `CetificationType` | 企业认定类型 | number(10) | ✓ | 0.0% |  |
| 10 | `ValidTerm` | 企业认定有效期限 | varchar2(50) | ✓ | 0.0% |  |
| 11 | `CetificationGrade` | 企业认定级别 | number(10) | ✓ | 100.0% | 企业认定级别(CetificationGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 12... |
| 12 | `CetificationObject` | 企业认定对象 | number(10) | ✓ | 100.0% | 企业认定对象(CetificationObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 13 | `CetificationProject` | 企业认定项目 | varchar2(255) | ✓ | 50.37% |  |
| 14 | `CertificationType` | 企业认定类型 | number(10) | ✓ |  |  |
| 15 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% | 序号(SerialNumber)，针对同一公告中，披露了多家公司的证书，按照披露顺序给定序号 |
| 16 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfCertified (企业认定与否)

企业认定与否(IfCertified)，该字段固定以下常量：1-是；0-否

### CetificationGrade (企业认定级别)

企业认定级别(CetificationGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 1224，得到企业认定级别的具体描述：1-省级，2-国家级。

### CetificationObject (企业认定对象)

企业认定对象(CetificationObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1223，得到企业认定对象的具体描述：1-上市公司，2-下属公司，3-公司前身，4-公司产品，5-控股股东。

### SerialNumber (序号)

序号(SerialNumber)，针对同一公告中，披露了多家公司的证书，按照披露顺序给定序号

## SQL示例

```sql
-- 查询 企业认定情况 数据
SELECT *
FROM lc_certification
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
