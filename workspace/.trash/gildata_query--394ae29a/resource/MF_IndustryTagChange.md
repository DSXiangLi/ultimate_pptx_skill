# MF_IndustryTagChange

**中文名**: 公募基金行业标签变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IndustryTagChange` |
| MySQL表名 | `mf_industrytagchange` |
| 中文名 | 公募基金行业标签变动 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：记录偏股型基金的行业标签及变动。目前包含了中证一级、申万一级、中信一级行业标签，。应用场景为，XX时间范围内，将XX基金的长期/中期/短期投资风格，匹配XX行业。
算法采用持仓和净值拟合互相验证的方式，更及时准确定义基金行业。
2.数据范围：2017年5月-至今。
3.信息来源：根据基金季报披露的持仓数据，以及每日更新的净值、中证指数行情数据，用模型拟合得到。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode)：与“行业类别表（CT_IndustryType）”中的“行业代码（IndustryC... |
| 4 | `FundTagName` | 标签名称 | varchar2(500) | ✗ | 100.0% |  |
| 5 | `StartDate` | 启用日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 停用日期 | date | ✓ | 86.89% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)：1-是 2-否。 |
| 8 | `Relationship` | 关联类型 | number(10) | ✗ | 100.0% | 关联类型（Relationship): 与“行业类别表（CT_IndustryType）”中的“行业分类标准（Stand... |
| 9 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期（IndexCycle): 表示计算时选取的基金收益时间跨度，例如 6表示近6个月，表示短期风格，12表示近一年... |
| 10 | `ReportDate` | 报告期 | date | ✗ | 100.0% | 报告期（ReportDate): 表示定报披露基金持仓数据的日期。 |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundTagCode (标签代码)

标签代码(FundTagCode)：与“行业类别表（CT_IndustryType）”中的“行业代码（IndustryCode）”关联，得到行业代码及其他信息。其中当Relationship=28-中证指数行业分类(2016版)时，由于字段类型原因，FundTagCode展示为0-能源；1-原材料；2-工业；3-可选消费；4-主要消费；5-医药卫生；6-金融地产；7-信息技术；8-电信业务；9-公用事业

### IfEffected (是否有效)

是否有效(IfEffected)：1-是 2-否。

### Relationship (关联类型)

关联类型（Relationship): 与“行业类别表（CT_IndustryType）”中的“行业分类标准（Standard）”关联，得到行业分类标准的具体描述：28-中证指数行业分类(2016版)，37-中信行业2019分类，38-申万行业分类(新)

### IndexCycle (指标周期)

指标周期（IndexCycle): 表示计算时选取的基金收益时间跨度，例如 6表示近6个月，表示短期风格，12表示近一年，表示中期风格.36表示近36个月，代表长期风格。

### ReportDate (报告期)

报告期（ReportDate): 表示定报披露基金持仓数据的日期。

## SQL示例

```sql
-- 查询 公募基金行业标签变动 数据
SELECT *
FROM mf_industrytagchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
