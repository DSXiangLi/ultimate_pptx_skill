# MF_FundManagerNew

**中文名**: 公募基金经理(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundManagerNew` |
| MySQL表名 | `mf_fundmanagernew` |
| 中文名 | 公募基金经理(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.本表记录历任基金经理、基金经理助理的任职起止日期、任职期间最新的净值增长率等。可以通过所属人员代码关联MF_PersonalInfo，配合使用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `PersonalCode` | 所属人员代码 | number(19) | ✗ | 100.0% | 所属人员代码（PersonalCode）：与“公募基金经理基本资料（MF_PersonalInfo）”中的“所属人员编码... |
| 6 | `Name` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 7 | `PostName` | 职位名称 | number(10) | ✓ | 100.0% | 职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具... |
| 8 | `Incumbent` | 在任与否 | number(3) | ✓ | 100.0% | 在任与否（Incumbent），该字段固定以下常量： 1-在任；0-离任 |
| 9 | `AccessionDate` | 到任日期 | date | ✗ | 100.0% | 到任日期（AccessionDate）：未成立基金，指首次公告的信息发布日期；后续产品成立后，会更新为产品成立日。 |
| 10 | `DimissionDate` | 离职日期 | date | ✓ | 55.97% |  |
| 11 | `SerialNumber` | 序号 | number(10) | ✓ | 41.34% |  |
| 12 | `ManagementTime` | 任职天数 | number(10) | ✓ | 99.19% |  |
| 13 | `Performance` | 任职期间基金净值增长率 | number(18,6) | ✓ | 98.84% | 任职期间基金净值增长率（Performance）： 计算公式=任职区间尾日基金复权净值/任职区间首日基金复权净值-1。针... |
| 14 | `Notes` | 备注说明 | varchar2(250) | ✓ | 99.76% |  |
| 15 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### PersonalCode (所属人员代码)

所属人员代码（PersonalCode）：与“公募基金经理基本资料（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。

### PostName (职位名称)

职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB = 1209，得到职位名称的具体描述：1-基金经理，2-基金经理助理。

### Incumbent (在任与否)

在任与否（Incumbent），该字段固定以下常量： 1-在任；0-离任

### AccessionDate (到任日期)

到任日期（AccessionDate）：未成立基金，指首次公告的信息发布日期；后续产品成立后，会更新为产品成立日。

### Performance (任职期间基金净值增长率)

任职期间基金净值增长率（Performance）：
计算公式=任职区间尾日基金复权净值/任职区间首日基金复权净值-1。针对已经离任的基金经理，任职区间尾日的复权净值指的是离任日期前(不包含）最大日期复权净值，任职区间首日指的是任职起始日前(不包含任职日)最大日期复权净值

## SQL示例

```sql
-- 查询 公募基金经理(新) 数据
SELECT *
FROM mf_fundmanagernew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
