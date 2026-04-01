# MF_FundManagerTrans

**中文名**: 公募基金经理(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundManagerTrans` |
| MySQL表名 | `mf_fundmanagertrans` |
| 中文名 | 公募基金经理(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

1.本表记录历任基金经理、基金经理助理的任职起止日期、任职期间最新的净值增长率等。可以通过所属人员代码关联MF_PersonalInfo，配合使用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `PersonalCode` | 所属人员代码 | number(19) | ✗ | 100.0% |  |
| 6 | `Name` | 姓名 | varchar2(30) | ✓ | 100.0% |  |
| 7 | `PostName` | 职位名称 | number(10) | ✓ | 100.0% | 职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB=1209，得到职位名称的具体描... |
| 8 | `Incumbent` | 在任与否 | number(10) | ✓ | 100.0% |  |
| 9 | `AccessionDate` | 到任日期 | date | ✗ | 100.0% |  |
| 10 | `DimissionDate` | 离职日期 | date | ✓ | 56.76% |  |
| 11 | `SerialNumber` | 序号 | number(10) | ✓ | 40.6% |  |
| 12 | `ManagementTime` | 任职天数 | number(10) | ✓ | 99.21% |  |
| 13 | `Performance` | 任职期间基金净值增长率 | number(18,6) | ✓ | 98.87% |  |
| 14 | `Notes` | 备注说明 | varchar2(250) | ✓ | 99.77% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PostName (职位名称)

职位名称(PostName)与(CT_SystemConst)表中的DM字段关联，令LB=1209，得到职位名称的具体描述：1-基金经理，2-基金经理助理。

## SQL示例

```sql
-- 查询 公募基金经理(转型) 数据
SELECT *
FROM mf_fundmanagertrans
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
