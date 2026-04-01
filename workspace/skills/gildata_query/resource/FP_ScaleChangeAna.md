# FP_ScaleChangeAna

**中文名**: 金融产品规模份额变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_ScaleChangeAna` |
| MySQL表名 | `fp_scalechangeana` |
| 中文名 | 金融产品规模份额变动 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品衍生 > 规模分析 |
| 更新频率 | 季更新 |
| 字段数量 | 24 |
| 版本 | 1 |

## 表描述

1.内容说明：记录金融产品规模变动相关统计。
2.数据范围：至今。
3.信息来源：根据金融产品规模，分类计算。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `TypeCode` | 分类口径代码 | number(10) | ✓ | 100.0% | 分类口径代码(TypeCode)：1-按公私募分类；2-按投资性质分类. |
| 6 | `TypeName` | 分类口径描述 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `ProTypeCode` | 产品类别代码 | varchar2(12) | ✗ | 100.0% | 产品类别代码(ProTypeCode)：（1）TypeCode为1时，FCC0000001T2-公募，FCC000000... |
| 8 | `ProTypeName` | 产品类别描述 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)：3-三个月，6-六个月，12-一年，36-三年 |
| 10 | `NVIIChange` | 规模变动 | number(18,4) | ✓ | 77.73% |  |
| 11 | `NVIIROC` | 规模变动率 | number(18,4) | ✓ | 77.69% |  |
| 12 | `CombNVIIChange` | 规模变动(合并) | number(18,4) | ✓ | 73.73% |  |
| 13 | `CombNVIIROC` | 规模变动率(合并) | number(18,4) | ✓ | 73.73% |  |
| 14 | `SharesChange` | 份额变动 | number(18,4) | ✓ | 79.58% |  |
| 15 | `SharesROC` | 份额变动率 | number(18,4) | ✓ | 79.52% |  |
| 16 | `CombSharesChange` | 份额变动(合并) | number(18,4) | ✓ | 74.66% |  |
| 17 | `CombSharesROC` | 份额变动率(合并) | number(18,4) | ✓ | 74.66% |  |
| 18 | `NVIIROCTypeAvg` | 规模变动率同类均值 | number(18,4) | ✓ | 77.69% |  |
| 19 | `NVIIROCTypeRank` | 规模变动率同类排名 | varchar2(100) | ✓ | 77.69% |  |
| 20 | `CombNVIIROCTypeAvg` | 规模变动率同类均值(合并) | number(18,4) | ✓ | 73.73% |  |
| 21 | `CombNVIIROCTypeRank` | 规模变动率同类排名(合并) | varchar2(100) | ✓ | 73.73% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### TypeCode (分类口径代码)

分类口径代码(TypeCode)：1-按公私募分类；2-按投资性质分类.

### ProTypeCode (产品类别代码)

产品类别代码(ProTypeCode)：（1）TypeCode为1时，FCC0000001T2-公募，FCC0000001T3-私募；（2）TypeCode为2时，FCC0000001T8-固定收益类，FCC0000001T9-权益类，FCC0000001TA-商品及金融衍生品类，FCC0000001TB-混合类。

### IndexCycle (指标周期)

指标周期(IndexCycle)：3-三个月，6-六个月，12-一年，36-三年

## SQL示例

```sql
-- 查询 金融产品规模份额变动 数据
SELECT *
FROM fp_scalechangeana
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
