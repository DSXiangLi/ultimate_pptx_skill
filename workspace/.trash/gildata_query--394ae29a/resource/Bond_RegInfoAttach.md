# Bond_RegInfoAttach

**中文名**: 债券注册信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RegInfoAttach` |
| MySQL表名 | `bond_reginfoattach` |
| 中文名 | 债券注册信息附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定期更新 |
| 字段数量 | 7 |
| 版本 | 1 |

## 表描述

1.本表为债券注册信息(Bond_RegInfo)的附表，通过RID进行关联使用，包含发行人代码、涉及债券、承销商/计划管理人代码。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)：1-发行人，2-涉及债券，3-承销商/管理人 |
| 4 | `InvolvedCode` | 涉及代码 | number(10) | ✗ | 100.0% | 涉及代码(InvolvedCode)：根据信息类别(InfoType) 不同进行关联，当信息类别(InfoType) =... |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoType (信息类别)

信息类别(InfoType)：1-发行人，2-涉及债券，3-承销商/管理人

### InvolvedCode (涉及代码)

涉及代码(InvolvedCode)：根据信息类别(InfoType) 不同进行关联，当信息类别(InfoType) =1,3时，与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到担保机构的具体名称、基本信息等；当信息类别(InfoType) =2时，与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 债券注册信息附表 数据
SELECT *
FROM bond_reginfoattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
