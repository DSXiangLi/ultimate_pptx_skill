# Bond_UnderWriter

**中文名**: 债券发行承销

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_UnderWriter` |
| MySQL表名 | `bond_underwriter` |
| 中文名 | 债券发行承销 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.收录各类债券的承销商、分销商的名称及机构编号等。
2.涵盖券种：可转换债券、企业债、金融债、资产支持证券等。
3.数据范围：1992-08-12 至今
4.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 债券内部代码 | number(10) | ✗ | 100.0% | 债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `IssueAndListType` | 发行与上市类别 | number(10) | ✗ | 100.0% | 发行与上市类别(IssueAndListType)与(CT_SystemConst)表中的DM字段关联，令LB = 10... |
| 4 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✓ | 100.0% |  |
| 5 | `AgentType` | 机构类别 | number(10) | ✓ | 100.0% | 机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM ... |
| 6 | `SN` | 序号 | number(10) | ✓ | 100.0% |  |
| 7 | `AgentCode` | 机构编号 | number(10) | ✓ | 100.0% | 机构编号（AgentCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCod... |
| 8 | `FullName` | 机构全称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |
| 11 | `UnderwritingVol` | 承销数量(张) | number(16,0) | ✓ | 0.0% |  |
| 12 | `UnderwritingSum` | 承销/包销金额(元) | number(19,4) | ✓ | 0.0% |  |
| 13 | `UnderwritingRatio` | 承销比例(%) | number(9,6) | ✓ | 0.0% |  |

## 字段说明

### MainCode (债券内部代码)

债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### IssueAndListType (发行与上市类别)

发行与上市类别(IssueAndListType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (4,8,10,12,16)，得到发行与上市类别的具体描述：4-可转换债券，8-企业债券，10-金融债券，12-资产支持证券，16-可交换公司债券。

### AgentType (机构类别)

机构类别(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM IN (1,2,3,5)，得到机构类别的具体描述：1-主承销商，2-副主承销商，3-分销商，5-联席主承销商。

### AgentCode (机构编号)

机构编号（AgentCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到承销或分销机构的具体名称、基本信息等。

## SQL示例

```sql
-- 查询 债券发行承销 数据
SELECT *
FROM bond_underwriter
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
