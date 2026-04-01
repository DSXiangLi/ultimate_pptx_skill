# Bond_IncOrDecHold

**中文名**: 债券增减持情况表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IncOrDecHold` |
| MySQL表名 | `bond_incordechold` |
| 中文名 | 债券增减持情况表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录控股股东及实控人增减持可转换债券的减持数量、减持比例等。
2.数据范围：2003-12-17 至今
3.信息来源：上交所公告, 深交所公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 	 公司代码(CompanyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(Compan... |
| 3 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部代码(InnerCode)：与“债券代码对照表(Bond_Code)”中的“债券内部编码(InnerCode)”... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `TypeSelect` | 类别选择 | number(10) | ✓ | 100.0% | 类别选择(TypeSelect)与(CT_SystemConst)表中的DM字段关联，令LB = 1201 and DM... |
| 7 | `ChangeStartDate` | 变动起始日期 | date | ✗ | 100.0% |  |
| 8 | `ChangeEndDate` | 变动完成日期 | date | ✗ | 100.0% |  |
| 9 | `HolderName` | 持有人名称 | varchar2(100) | ✗ | 100.0% |  |
| 10 | `HolderCode` | 持有人编码 | number(10) | ✓ | 48.43% | 持有人编码(HolderCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyC... |
| 11 | `HolderAttribute` | 持有人所属性质 | number(10) | ✓ | 100.0% | 持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 178... |
| 12 | `HoldVolumeBefore` | 变动前持有数量(张) | number(14,2) | ✓ | 98.62% |  |
| 13 | `HVBToIssueSize` | 变动前持有量占发行总量比例(%) | number(19,8) | ✓ | 98.55% |  |
| 14 | `ChangeVolume` | 变动数量(张) | number(14,2) | ✓ | 100.0% |  |
| 15 | `CVToIssueSize` | 变动量占发行总量比例 | number(19,8) | ✓ | 99.87% |  |
| 16 | `HoldVolumeAfter` | 变动后持有数量(张) | number(14,2) | ✓ | 98.81% |  |
| 17 | `HVAToIssueSize` | 变动后持有量占发行总量比例(%) | number(19,8) | ✓ | 98.71% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

	
公司代码(CompanyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到机构的具体名称、基本信息等。

### InnerCode (债券内部编码)

债券内部代码(InnerCode)：与“债券代码对照表(Bond_Code)”中的“债券内部编码(InnerCode)”关联，得到债券的交易代码、债券简称等。

### TypeSelect (类别选择)

类别选择(TypeSelect)与(CT_SystemConst)表中的DM字段关联，令LB = 1201 and DM =21，得到类别选择的具体描述：21-债券增减持。

### HolderCode (持有人编码)

持有人编码(HolderCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到相关企业的具体名称、基本信息等。

### HolderAttribute (持有人所属性质)

持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持有人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 债券增减持情况表 数据
SELECT *
FROM bond_incordechold
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
