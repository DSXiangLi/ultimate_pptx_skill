# MF_SHInfluence

**中文名**: 公募基金单一持有人份额信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_SHInfluence` |
| MySQL表名 | `mf_shinfluence` |
| 中文名 | 公募基金单一持有人份额信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 季更新 |
| 字段数量 | 20 |
| 版本 | 1.01 |

## 表描述

1.本表记录定报披露的单一持有人持有份额超过20%信息,包含报告期、持有人性质、持有份额、持有比例,以及在报告期中间断出现超过20%持有限额的时间段等信息。
2.历史数据：2006年12月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码(InnerCode):与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | number(10) | ✗ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `InfluStDate` | 影响起始日期 | date | ✓ | 99.86% |  |
| 8 | `InfluEnDate` | 影响截止日期 | date | ✗ | 100.0% |  |
| 9 | `InfluPeriod` | 影响区间 | varchar2(100) | ✓ | 0.14% |  |
| 10 | `SerialNumber` | 持有人编码 | varchar2(10) | ✗ | 100.0% |  |
| 11 | `HolderNature` | 持有人性质 | number(10) | ✓ | 100.0% | 持有人性质(HolderNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持... |
| 12 | `InvestorID` | 投资者ID | number(10) | ✓ | 3.23% | 投资者ID(InvestorID):当HolderNature=2时,与“机构基本资料(LC_InstiArchive)... |
| 13 | `StartShares` | 期初份额(份) | number(19,4) | ✓ | 89.06% |  |
| 14 | `ApplyingShares` | 申购份额(份) | number(19,4) | ✓ | 61.93% |  |
| 15 | `RedeemShares` | 赎回份额(份) | number(19,4) | ✓ | 63.13% |  |
| 16 | `HoldingVolume` | 持有份额(份) | number(19,4) | ✓ | 89.88% |  |
| 17 | `HoldRatio` | 持有比例 | number(19,6) | ✓ | 90.97% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码(InnerCode):与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到基金的交易代码、交易简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (5,6,17,61,23,63)，得到信息来源的具体描述：5-年度报告，6-中期报告，17-第一季度报告，23-第三季度报告，61-第二季度报告，63-第四季度报告。

### HolderNature (持有人性质)

持有人性质(HolderNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持有人性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### InvestorID (投资者ID)

投资者ID(InvestorID):当HolderNature=2时,与“机构基本资料(LC_InstiArchive)表“的"企业编号(CompanyCode)"字段关联,可查询投资机构的中文名称、英文名称、组织机构代码等基本信息；当HolderNature=3时,与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到投资基金的交易代码、交易简称等。

## SQL示例

```sql
-- 查询 公募基金单一持有人份额信息 数据
SELECT *
FROM mf_shinfluence
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
