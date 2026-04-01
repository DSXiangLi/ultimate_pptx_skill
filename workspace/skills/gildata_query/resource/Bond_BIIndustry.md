# Bond_BIIndustry

**中文名**: 债券主体行业划分

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BIIndustry` |
| MySQL表名 | `bond_biindustry` |
| 中文名 | 债券主体行业划分 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.本表记录债券主体，包括发行人、原始权益人等行业划分情况。
2.数据范围：2005-10-11 至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 97.49% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 57.67% |  |
| 4 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 5 | `Standard` | 行业划分标准 | number(10) | ✗ | 100.0% | 行业划分标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM... |
| 6 | `Industry` | 所属行业 | number(19) | ✓ | 100.0% | 所属行业（Industry）：当Standard＝22时，与(CT_IndustryType)表中的IndustryNu... |
| 7 | `IfExecuted` | 是否执行 | number(10) | ✓ | 100.0% | 是否执行(IfExecuted)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 8 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 9 | `CancelDate` | 取消日期 | date | ✓ | 2.98% |  |
| 10 | `FirstIndustryCode` | 一级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 11 | `FirstIndustryName` | 一级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `SecondIndustryCode` | 二级行业代码 | varchar2(20) | ✓ | 93.44% |  |
| 13 | `SecondIndustryName` | 二级行业名称 | varchar2(100) | ✓ | 93.44% |  |
| 14 | `ThirdIndustryCode` | 三级行业代码 | varchar2(20) | ✓ | 80.56% |  |
| 15 | `ThirdIndustryName` | 三级行业名称 | varchar2(100) | ✓ | 80.56% |  |
| 16 | `FourthIndustryCode` | 四级行业代码 | varchar2(20) | ✓ | 47.34% |  |
| 17 | `FourthIndustryName` | 四级行业名称 | varchar2(100) | ✓ | 47.34% |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### Standard (行业划分标准)

行业划分标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (22,24,29,32,38,39,44)，得到行业划分标准的具体描述：22-证监会行业分类2012版，24-申万行业分类2014版，29-新聚源行业分类(2017)，32-国民经济行业分类(2017)，38-申万行业分类(新)，39-新聚源行业分类(2021)，44-中国上市公司协会上市公司行业统计分类指引。

### Industry (所属行业)

所属行业（Industry）：当Standard＝22时，与(CT_IndustryType)表中的IndustryNum字段关联，令Standard=22，得到IndustryCode 的具体描述；当Standard＝24时，与系统常量表中的DM字段关联，令LB=1804；当Standard＝29时，与(CT_IndustryType)表中的IndustryNum字段关联，令Standard=29，得到IndustryCode 的具体描述；当Standard＝38时，与(CT_IndustryType)表中的IndustryNum字段关联，令Standard=38，得到IndustryCode 的具体描述；当Standard＝(32,39,44)时，与(CT_IndustryType)表中的IndustryNum字段关联，限定对应Standard，得到IndustryCode 的具体描述。

### IfExecuted (是否执行)

是否执行(IfExecuted)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否执行的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 债券主体行业划分 数据
SELECT *
FROM bond_biindustry
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
