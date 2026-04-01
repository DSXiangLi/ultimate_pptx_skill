# LC_SMVotingAttach

**中文名**: 股东大会表决附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SMVotingAttach` |
| MySQL表名 | `lc_smvotingattach` |
| 中文名 | 股东大会表决附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上市公司在股东大会议案表决时的回避议案情况，包括回避的股东、回避原因。
2.数据范围：2020年8月-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID关联LC_SMVoting的ID关联，获取股东大会议案的大标题、小标题、议案类别、议案投票类型、回避表决股数等相关... |
| 3 | `AvoidSHName` | 回避股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `AvoidSHKind` | 回避股东性质 | number(10) | ✓ | 100.0% | 回避股东性质(AvoidSHKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到回... |
| 5 | `AvoidSHCode` | 回避股东ID | number(10) | ✓ | 52.67% | 当回避股东性质(AvoidSHKind)=2时，与机构基本资料（LC_InstiArchive）中的企业编号（Compa... |
| 6 | `AvoidReason` | 回避原因 | number(10) | ✗ | 100.0% | 回避原因(AvoidReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2220，得到回避原... |
| 7 | `AvoidReasonDesc` | 回避原因描述 | varchar2(200) | ✓ | 99.51% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID关联LC_SMVoting的ID关联，获取股东大会议案的大标题、小标题、议案类别、议案投票类型、回避表决股数等相关信息

### AvoidSHKind (回避股东性质)

回避股东性质(AvoidSHKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到回避股东性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### AvoidSHCode (回避股东ID)

当回避股东性质(AvoidSHKind)=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；回避股东性质(AvoidSHKind)=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联

### AvoidReason (回避原因)

回避原因(AvoidReason)与(CT_SystemConst)表中的DM字段关联，令LB = 2220，得到回避原因的具体描述：1-关联交易方，2-公司管理层，99-其他。

## SQL示例

```sql
-- 查询 股东大会表决附表 数据
SELECT *
FROM lc_smvotingattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
