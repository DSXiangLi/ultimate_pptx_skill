# LC_SecuHolder

**中文名**: 证券持有人

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SecuHolder` |
| MySQL表名 | `lc_secuholder` |
| 中文名 | 证券持有人 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 不定时更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.收录持有数量达到或超过可流通数量5%的权证持有人信息(当前已不再更新)、基金的关联方持有人信息等。
2.数据范围：2004-12-31至今
3.信息来源：上交所、深交所、定报等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券代码 | number(10) | ✗ | 100.0% | 证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 89.65% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 6 | `InfoType` | 信息类别 | number(10) | ✓ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1380，得到信息类别的具... |
| 7 | `SecuVolume` | 证券规模(份) | number(18,2) | ✓ | 0.0% |  |
| 8 | `HolderNum` | 持有人户数(户) | number(10) | ✓ | 0.0% |  |
| 9 | `HolderNo` | 持有人序号 | number(10) | ✓ | 100.0% |  |
| 10 | `HolderName` | 持有人名称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `HolderNature` | 持有人性质 | number(10) | ✓ |  |  |
| 12 | `HolderCode` | 持有人编号 | number(10) | ✓ | 80.79% | 持有人编号(HolderCode)和机构基本资料表(LC_InstiArchive)中的CompanyCode关联 |
| 13 | `BelongedCompanyCode` | 所属公司 | number(10) | ✓ | 28.93% | 所属公司(BelongedCompanyCode)和证券主表(SecuMain)中的CompanyCode关联 |
| 14 | `HoldVolume` | 持有数量(份) | number(18,2) | ✓ | 87.54% |  |
| 15 | `HoldRatio` | 持有比例 | number(9,6) | ✓ | 82.75% |  |
| 16 | `Notes` | 备注 | varchar2(1000) | ✓ | 0.0% |  |
| 17 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券代码)

证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1380，得到信息类别的具体描述：2001-权证持有5%以上，2002-权证创设人持有量，3001-基金关联方持有份额。

### HolderCode (持有人编号)

持有人编号(HolderCode)和机构基本资料表(LC_InstiArchive)中的CompanyCode关联

### BelongedCompanyCode (所属公司)

所属公司(BelongedCompanyCode)和证券主表(SecuMain)中的CompanyCode关联

## SQL示例

```sql
-- 查询 证券持有人 数据
SELECT *
FROM lc_secuholder
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
