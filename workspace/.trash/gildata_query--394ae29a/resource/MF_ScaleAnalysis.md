# MF_ScaleAnalysis

**中文名**: 公募基金规模份额相关统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ScaleAnalysis` |
| MySQL表名 | `mf_scaleanalysis` |
| 中文名 | 公募基金规模份额相关统计 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析 |
| 更新频率 | 每季度/新基金股本披露日更新 |
| 字段数量 | 25 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录公募基金规模与份额的相关统计指标。
其中，计算规则如下：
（1）披露值（披露规模、披露份额）：表示基金定报披露的数据。
（2）合并值（规模合并值、份额合并值）：将全部分开披露的子基金进行加总，主子基金都显示加总值。如果FundRemark=1,则取自身与其分开披露的子基金数值的加总；如果FundRemark=2、4，则取其主基金的合并值（需计算全部子基金的加总值）；如果FundRemark=3，则取实际值。
（3）实际规模：优先取披露规模，如果新基金还未披露时，则新基金规模=份额*{>=披露日的单位净值}。
（4）是否合并披露（规模、份额）：表示基金（InnerCode)对应的披露规模、实际规模、份额是否与它的子基金（RelatedInnerCode）合并披露，如果合并披露，则会对InnerCode赋值1，其对应的RelatedInnerCode的是否合并披露字段也会赋值1。
（5）同类均值、排名：如果是合并值，会剔除InnerCode为子基金的数据，即只取FundRemark in(1,3)的数据。
2.数据范围：1998年4月-至今。
3.信息来源：根据基金公司、证监会、中证信息披露的数据通过逻辑算法生成。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% | 截止日期(EndDate）：为公告披露最新份额的截止日期，如定期报告、合同生效公告等。 |
| 4 | `TypeCode` | 基金分类口径代码 | number(10) | ✓ | 100.0% |  |
| 5 | `TypeName` | 基金分类口径描述 | varchar2(100) | ✗ | 100.0% | 基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类“ |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✓ | 99.81% | 基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTy... |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 99.81% |  |
| 8 | `RelatedInnerCode` | 关联代码内部编码 | number(10) | ✓ | 36.26% | 关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 9 | `IfScaleComb` | 规模是否合并披露 | number(10) | ✓ | 100.0% | 规模是否合并披露(IfScaleComb): 1-是；0-否 |
| 10 | `NVI` | 披露规模(元) | number(18,4) | ✓ | 91.96% |  |
| 11 | `CombNVI` | 披露规模合并值(元) | number(18,4) | ✓ | 93.87% |  |
| 12 | `NVII` | 实际规模(元) | number(18,4) | ✓ | 99.97% |  |
| 13 | `CombNVII` | 实际规模合并值(元) | number(18,4) | ✓ | 99.9% |  |
| 14 | `IfShareComb` | 份额是否合并披露 | number(10) | ✓ | 100.0% | 份额是否合并披露（IfShareComb）：1-是；0-否 |
| 15 | `TotalShares` | 份额(份) | number(18,4) | ✓ | 100.0% |  |
| 16 | `CombTotalShares` | 份额合并值(份) | number(18,4) | ✓ | 99.9% |  |
| 17 | `TotalAsset` | 资产总值(合并) | number(18,4) | ✓ | 58.07% |  |
| 18 | `NVIITypeAvg` | 规模同类均值 | number(18,4) | ✓ | 99.78% |  |
| 19 | `NVIIRank` | 规模同类排名 | varchar2(100) | ✓ | 99.78% |  |
| 20 | `CombNVIITypeAvg` | 合并规模同类均值 | number(18,4) | ✓ | 64.77% |  |
| 21 | `CombNVIIRank` | 合并规模同类排名 | varchar2(100) | ✓ | 64.77% |  |
| 22 | `FundRemark` | 基金备注 | number(10) | ✓ | 100.0% | 基金备注(FundRemark): 1-基金是主基金、不是子基金；2-表示基金是主基金、也是子基金；3-基金没有主或子基... |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### EndDate (截止日期)

截止日期(EndDate）：为公告披露最新份额的截止日期，如定期报告、合同生效公告等。

### TypeName (基金分类口径描述)

基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类“

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述，1101-股票型，1103-混合型，1105-债券型，1110-QDII，1106-短期理财债券型，1109-货币型。

### RelatedInnerCode (关联代码内部编码)

关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得基金的交易代码、简称等。

### IfScaleComb (规模是否合并披露)

规模是否合并披露(IfScaleComb): 1-是；0-否

### IfShareComb (份额是否合并披露)

份额是否合并披露（IfShareComb）：1-是；0-否

### FundRemark (基金备注)

基金备注(FundRemark): 1-基金是主基金、不是子基金；2-表示基金是主基金、也是子基金；3-基金没有主或子基金 ；4-基金不是主基金、是子基金。
取值逻辑：MF_CodeRelationshipNew，满足截止日期在有效时间区间内，CodeDefine in(21,22,37,76)，用于判断基金是否存在主/子基金。

## SQL示例

```sql
-- 查询 公募基金规模份额相关统计 数据
SELECT *
FROM mf_scaleanalysis
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
