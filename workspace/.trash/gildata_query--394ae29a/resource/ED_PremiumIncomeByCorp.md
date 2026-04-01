# ED_PremiumIncomeByCorp

**中文名**: 保险公司保费收入情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `ED_PremiumIncomeByCorp` |
| MySQL表名 | `ed_premiumincomebycorp` |
| 中文名 | 保险公司保费收入情况 |
| 路径 | 聚源新版数据库 > 机构数据库 > 保险公司 |
| 更新频率 | 月更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.收录中国保险监督管理委员会公布的，各家财险公司和寿险公司在全国的保险保费总收入情况；与机构基本资料表关联得到相关保险公司的详细信息
2.数据范围：2006年5月-至今
3.数据源：中国保监会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `ReportPeriod` | 数据统计区间 | number(10) | ✗ | 100.0% | 数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AN... |
| 5 | `SerialNum` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `CompanyName` | 企业名称 | varchar2(200) | ✓ | 100.0% |  |
| 7 | `CompanyCode` | 企业编号 | number(10) | ✓ | 95.21% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 8 | `InsuranceCorpType` | 保险公司类别 | number(10) | ✗ | 100.0% | 保险公司类别（InsuranceCorpType）：与“系统常量表（CT_SystemConst）”的“代码（DM）”关... |
| 9 | `CapitalStructure` | 企业资本结构 | varchar2(100) | ✓ | 98.4% |  |
| 10 | `CapitalStructureCode` | 企业资本结构代码 | number(10) | ✓ | 98.4% | 企业资本结构代码(CapitalStructureCode)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 11 | `PremiumIncome` | 保费收入(万元) | number(19,4) | ✓ | 99.95% |  |
| 12 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ReportPeriod (数据统计区间)

数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (3)，得到数据统计区间的具体描述：3-期末累计。

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### InsuranceCorpType (保险公司类别)

保险公司类别（InsuranceCorpType）：与“系统常量表（CT_SystemConst）”的“代码（DM）”关联，“LB=1412”，得到保险公司的具体类别。110-财产保险公司，130-人寿保险公司

### CapitalStructureCode (企业资本结构代码)

企业资本结构代码(CapitalStructureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1133 AND DM IN (100,300)，得到企业资本结构代码的具体描述：100-内资企业，300-外商投资企业。

## SQL示例

```sql
-- 查询 保险公司保费收入情况 数据
SELECT *
FROM ed_premiumincomebycorp
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
