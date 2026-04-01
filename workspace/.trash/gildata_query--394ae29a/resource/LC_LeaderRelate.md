# LC_LeaderRelate

**中文名**: 公司领导人亲属信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_LeaderRelate` |
| MySQL表名 | `lc_leaderrelate` |
| 中文名 | 公司领导人亲属信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司人力资源 |
| 更新频率 | 不定期更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：收录了上市公司董事会、监事会、经营层中主要领导人及核心技术人员的亲属，包括配偶、子女、兄弟姐妹等所在的公司信息，包括公司名称、在公司中的角色，如高管、股东等、起始截止时间等。
2.数据范围：20180801-至今。
3.信息来源：申报稿、招股说明书、定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 高管背景表ID | number(19) | ✗ | 100.0% | 高管背景表ID（RID）与公司领导人介绍(LC_LeaderIntroduce)的ID关联，可以到相关公司及领导人数据。 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `RelateName` | 亲属姓名 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `RelateCode` | 亲属编码 | number(10) | ✓ | 73.75% |  |
| 6 | `Relationship` | 亲属关系 | number(10) | ✗ | 100.0% | 亲属关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 1499 AND ... |
| 7 | `RelationshipStatement` | 亲属关系说明 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `RelateCompanyCode` | 亲属所在公司编码 | number(10) | ✓ | 90.66% | 亲属所在公司编码（RelateCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编... |
| 9 | `RelateCompanyName` | 亲属所在公司名称 | varchar2(100) | ✗ | 100.0% |  |
| 10 | `RelateHoldingRatio` | 亲属所在公司持股比例 | number(9,6) | ✓ | 64.76% |  |
| 11 | `CorporateRole` | 亲属与所在公司关系描述 | varchar2(100) | ✓ | 97.87% |  |
| 12 | `BeginDate` | 亲属与所在公司关系的起始日期 | date | ✗ | 100.0% |  |
| 13 | `EndDate` | 亲属与所在公司关系的结束日期 | date | ✓ | 0.27% |  |
| 14 | `IfEffected` | 亲属关系是否有效 | number(10) | ✗ | 100.0% | 亲属关系是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and... |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (高管背景表ID)

高管背景表ID（RID）与公司领导人介绍(LC_LeaderIntroduce)的ID关联，可以到相关公司及领导人数据。

### Relationship (亲属关系)

亲属关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 1499 AND DM IN (2,3,4,5,9)，得到亲属关系的具体描述：2-父母，3-配偶，4-子女，5-兄弟姐妹，9-其他。

### RelateCompanyCode (亲属所在公司编码)

亲属所在公司编码（RelateCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到亲属所在公司的基本资料。

### IfEffected (亲属关系是否有效)

亲属关系是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到亲属关系是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公司领导人亲属信息 数据
SELECT *
FROM lc_leaderrelate
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
