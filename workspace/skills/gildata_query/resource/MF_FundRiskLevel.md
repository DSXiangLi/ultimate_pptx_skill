# MF_FundRiskLevel

**中文名**: 公募基金风险等级表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundRiskLevel` |
| MySQL表名 | `mf_fundrisklevel` |
| 中文名 | 公募基金风险等级表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录基金公司披露的全市场基金的风险等级的数据。应监管需要，本数据可服务于各类公募基金销售场景。
2.数据范围：1999年1月起-至今
3.信息来源：基金公司官网、基金公告、聚源规则定义（详见Q&A）

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表(SecuMain)”以及"港股证券主表(HK_SecuMain)中的“证券... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 99.4% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `RiskLevel` | 风险等级 | number(10) | ✓ | 100.0% | 风险等级(RiskLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1847，得到风险等级的... |
| 6 | `BeginDate` | 起始日期 | date | ✓ | 100.0% |  |
| 7 | `EndDate` | 截止日期 | date | ✓ | 27.91% |  |
| 8 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表(SecuMain)”以及"港股证券主表(HK_SecuMain)中的“证券内部编码（InnerCode）"关联，得到基金的交易代码、简称等

### RiskLevel (风险等级)

风险等级(RiskLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1847，得到风险等级的具体描述：1-低，2-中低，3-中，4-中高，5-高，99-未披露。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN(1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金风险等级表 数据
SELECT *
FROM mf_fundrisklevel
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
