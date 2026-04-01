# DZ_AShareSNIAttach

**中文名**: A股增发附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AShareSNIAttach` |
| MySQL表名 | `dz_asharesniattach` |
| 中文名 | A股增发附表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 7 |
| 版本 | 1 |

## 表描述

1、内容说明：收录A股增发表对发行目的的分类情况；
2、信息来源：发行方案，发行认购，发行情况报告书；
3、数据范围：1991-08-17至今。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“A股增发【DZ_AShareSeasonedNewIssue】”的ID关联 |
| 3 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB=2490，得到信息类别的具体描... |
| 4 | `InfoContentCode` | 信息内容编码 | number(10) | ✗ | 100.0% | 信息内容编码(InfoContentCode)与(CT_SystemConst)表中的DM字段关联，令LB=2491，得... |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“A股增发【DZ_AShareSeasonedNewIssue】”的ID关联

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB=2490，得到信息类别的具体描述：1-增发新股-增发目的。

### InfoContentCode (信息内容编码)

信息内容编码(InfoContentCode)与(CT_SystemConst)表中的DM字段关联，令LB=2491，得到信息内容编码的具体描述：1-补充流动资金，2-项目融资，3-配套融资，4-融资收购其他资产，5-重大资产重组，6-引入战略投资者，7-补充核心资本，8-股权激励，9-筹措库存股，10-借壳上市，11-实控人资产注入，12-壳资源重组，13-重大资产置换，14-吸收合并，999-其他。

## SQL示例

```sql
-- 查询 A股增发附表 数据
SELECT *
FROM dz_asharesniattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
