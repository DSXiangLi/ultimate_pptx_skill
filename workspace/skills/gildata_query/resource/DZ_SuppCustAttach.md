# DZ_SuppCustAttach

**中文名**: 公司供应商与客户附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_SuppCustAttach` |
| MySQL表名 | `dz_suppcustattach` |
| 中文名 | 公司供应商与客户附表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司产品供销 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：收录企业供应商与客户明细表中供应商、客户的具体清单，以及交易金额、占比等信息。
2.数据范围：2015年至今
3.信息来源：招股说明书、定报

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与DZ_SuppCustDetail的ID关联，获取相关信息。 |
| 3 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 4 | `RelatedPartyName` | 供应商/客户名称 | varchar2(600) | ✓ | 100.0% |  |
| 5 | `RelatedPartyCode` | 供应商/客户代码 | number(10) | ✓ | 80.35% | 供应商/客户(RelatedPartyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（C... |
| 6 | `RelatedPartyAttribute` | 供应商/客户属性 | number(10) | ✓ | 99.96% | 供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令L... |
| 7 | `TradingValue` | 交易金额(元) | number(19,4) | ✓ | 24.48% |  |
| 8 | `Ratio` | 占比 | number(9,6) | ✓ | 22.32% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与DZ_SuppCustDetail的ID关联，获取相关信息。

### RelatedPartyCode (供应商/客户代码)

供应商/客户(RelatedPartyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到所属公司的基本信息。

### RelatedPartyAttribute (供应商/客户属性)

供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到供应商/客户属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 公司供应商与客户附表 数据
SELECT *
FROM dz_suppcustattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
