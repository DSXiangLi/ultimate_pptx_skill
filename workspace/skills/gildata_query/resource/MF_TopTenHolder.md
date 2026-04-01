# MF_TopTenHolder

**中文名**: 公募基金前10名持有人持股信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_TopTenHolder` |
| MySQL表名 | `mf_toptenholder` |
| 中文名 | 公募基金前10名持有人持股信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金前10名持有人持有基金份额情况，包括持有人名称、持有的份额、持有的比例、持有的性质等。
2.历史数据：1998年4月起-至今。
3.数据来源：基金公司披露的临时报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `HolderName` | 持有人名称 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `HolderCode` | 机构代码 | varchar2(20) | ✓ | 33.6% | 机构代码(HolderCode)：与机构基本资料表（LC_InstiArchive）中的公司代码（CompanyCode... |
| 10 | `HoldingVolume` | 持有份额(份) | number(18,4) | ✓ | 100.0% |  |
| 11 | `HoldingRatio` | 持有比例 | number(18,6) | ✓ | 100.0% |  |
| 12 | `HolderNature` | 持有人性质 | number(10) | ✓ |  |  |
| 13 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 14 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### HolderCode (机构代码)

机构代码(HolderCode)：与机构基本资料表（LC_InstiArchive）中的公司代码（CompanyCode）字段关联。

## SQL示例

```sql
-- 查询 公募基金前10名持有人持股信息 数据
SELECT *
FROM mf_toptenholder
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
