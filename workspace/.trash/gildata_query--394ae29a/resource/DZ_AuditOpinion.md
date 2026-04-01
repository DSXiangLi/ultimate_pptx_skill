# DZ_AuditOpinion

**中文名**: 公司历年审计意见

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AuditOpinion` |
| MySQL表名 | `dz_auditopinion` |
| 中文名 | 公司历年审计意见 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 14 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录中介机构对公司季度、半年度、年度经营情况的评价，区分审计单位、审计意见类型，本表涵盖了公司招股以来的历次纪录。
2.数据范围：1990-12-31至今
3.信息来源：定期报告、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.98% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `AuditReportsType` | 审计报告类型 | number(10) | ✓ | 100.0% | 审计报告类型(AuditReportsType)与(CT_SystemConst)表中的DM字段关联，令LB = 224... |
| 7 | `AccountingFirms` | 会计师事务所 | varchar2(100) | ✓ | 45.66% |  |
| 8 | `InstiBelongedCode` | 所属机构 | number(10) | ✓ | 45.3% | 所属机构（InstiBelongedCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Co... |
| 9 | `CPA` | 注册会计师 | varchar2(100) | ✓ | 44.27% |  |
| 10 | `OpinionType` | 审计意见类型 | number(10) | ✓ | 100.0% | 审计意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1051 AND... |
| 11 | `OpinionFullText` | 审计意见全文 | clob | ✓ | 53.72% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AuditReportsType (审计报告类型)

审计报告类型(AuditReportsType)与(CT_SystemConst)表中的DM字段关联，令LB = 2244 AND DM IN (1,2)，得到审计报告类型的具体描述：1-财务报表审计报告，2-内部控制审计报告。

### InstiBelongedCode (所属机构)

所属机构（InstiBelongedCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到所属机构的基本信息、联系方式等。

### OpinionType (审计意见类型)

审计意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1051 AND DM IN(1,2,3,4,5,6,7,10,11)，得到审计意见类型的具体描述：1-无保留，2-无保留带解释性说明，3-保留意见，4-拒绝/无法表示意见，5-否定意见，6-未经审计，7-保留带解释性说明，10-经审计（不确定具体意见类型），11-无保留带持续经营重大不确定性。

## SQL示例

```sql
-- 查询 公司历年审计意见 数据
SELECT *
FROM dz_auditopinion
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
