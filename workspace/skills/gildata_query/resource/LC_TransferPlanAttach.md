# LC_TransferPlanAttach

**中文名**: 股东增减持计划表附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_TransferPlanAttach` |
| MySQL表名 | `lc_transferplanattach` |
| 中文名 | 股东增减持计划表附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录股东增减持计划主表中各个股东的股东性质、股东ID的信息。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 股东增减持计划表ID | number(19) | ✗ | 100.0% |  |
| 3 | `SHName` | 股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `SHAttribute` | 股东属性 | number(10) | ✓ | 100.0% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属... |
| 5 | `SHID` | 股东ID | number(10) | ✓ | 34.6% | 当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（Company... |
| 6 | `SHStatus` | 股东身份 | number(10) | ✓ | 52.55% | 股东身份(SHStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2322，得到股东身份的具... |
| 7 | `SHStatusDesc` | 股东身份描述 | varchar2(50) | ✓ | 47.95% |  |
| 8 | `SharesHoldingNow` | 当前持股数量(股/份) | number(19,4) | ✓ | 49.12% |  |
| 9 | `HoldingRatioNow` | 当前持股比例 | number(19,8) | ✓ | 48.48% |  |
| 10 | `SharesHoldingSource` | 当前持股来源 | varchar2(1000) | ✓ | 17.42% |  |
| 11 | `ChangeReason` | 增减持原因 | number(10) | ✓ | 45.66% | 增减持原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2323，得到增... |
| 12 | `ChangeReasonDesc` | 增减持原因描述 | varchar2(1000) | ✓ | 45.33% |  |
| 13 | `SumMark` | 合并披露标识 | number(10) | ✓ | 0.11% | 合并披露标识(SumMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1433 and DM ... |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHID (股东ID)

当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。      

### SHStatus (股东身份)

股东身份(SHStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2322，得到股东身份的具体描述：1-公司管理层，2-控股股东及其一致行动人，3-实际控制人及其一致行动人，4-控股股东、实际控制人及其一致行动人，5-5%以上非控股股东，6-5%以下股东，7-控股股东及其一致行动人、公司管理层，8-实际控制人及其一致行动人、公司管理层，9-控股股东、实际控制人及其一致行动人、公司管理层，10-5%以上非控股股东、公司管理层，11-5%以下股东、公司管理层，12-其他，13-控股股东，14-实际控制人，15-控股股东、实际控制人，16-控股股东的一致行动人，17-实际控制人的一致行动人，18-公司管理层的一致行动人，19-公司管理层及一致行动人。

### ChangeReason (增减持原因)

增减持原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2323，得到增减持原因的具体描述：1-维护股价，对公司未来价值的认可，2-公司经营发展需要，3-个人资金需求，4-违约处置，5-投资安排，6-归还借款，7-其他。

### SumMark (合并披露标识)

合并披露标识(SumMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1433 and DM in (9900)，得到合并披露标识的具体描述：9900-合计。

## SQL示例

```sql
-- 查询 股东增减持计划表附表 数据
SELECT *
FROM lc_transferplanattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
