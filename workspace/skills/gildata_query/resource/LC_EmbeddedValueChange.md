# LC_EmbeddedValueChange

**中文名**: 保险公司内含价值变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_EmbeddedValueChange` |
| MySQL表名 | `lc_embeddedvaluechange` |
| 中文名 | 保险公司内含价值变动 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 季更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.反映保险公司在年报中披露的内含价值变动数据。
2.仅收录保险公司在报告期末未调整的合并报表。
3.该表中各科目的单位均为人民币元。
4.07年之前，保险公司未分别披露寿险业务和非寿险业务的内含价值变化，因此，07年之前，寿险业务内含价值中，包含了非寿险业务的部分。
5.由于披露精度的问题，数据校验时，可能在百万位上有小额差异。
6.数据范围：2005-12-31至今
7.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 5 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `BeginEVLifeInsurance` | 寿险业务内含价值期初值 | number(19,4) | ✓ | 100.0% |  |
| 8 | `ExpectedReturn` | 内含价值预期回报 | number(19,4) | ✓ | 100.0% |  |
| 9 | `PeriodNewBusinessValue` | 期间新业务价值 | number(19,4) | ✓ | 100.0% |  |
| 10 | `OperExperienceVariances` | 营运经验差异 | number(19,4) | ✓ | 92.06% |  |
| 11 | `DividendVariances` | 红利分配差异 | number(19,4) | ✓ | 50.79% |  |
| 12 | `InvestReturnVariances` | 投资收益差异 | number(19,4) | ✓ | 80.16% |  |
| 13 | `RiskDiscountRateChange` | 风险贴现率变动 | number(19,4) | ✓ | 7.14% |  |
| 14 | `EvaluationBaseChange` | 评估基础的改变 | number(19,4) | ✓ | 4.76% |  |
| 15 | `EvaluationMethodChange` | 评估方法，假设和模型的改变 | number(19,4) | ✓ | 89.68% |  |
| 16 | `AdjustedMarketValueLife` | 市场价值调整(寿险业务) | number(19,4) | ✓ | 77.78% |  |
| 17 | `OtherVariances` | 其他 | number(19,4) | ✓ | 84.92% |  |
| 18 | `EVBeforeChange` | 资本变动前寿险内含价值 | number(19,4) | ✓ | 100.0% | 资本变动前寿险内含价值（EVBeforeChange）=寿险业务内含价值期初值+内含价值预期回报+期间新业务价值+营运经... |
| 19 | `CapitalInjection` | 资本注入 | number(19,4) | ✓ | 21.43% |  |
| 20 | `ShareholderDividend` | 股东股息 | number(19,4) | ✓ | 41.27% |  |
| 21 | `EndEVLifeInsurance` | 寿险业务期末内含价值 | number(19,4) | ✓ | 100.0% | 寿险业务期末内含价值（EndEVLifeInsurance）=资本变动前寿险内含价值+资本注入+股东股息 |
| 22 | `BeginEVGeneralInsurance` | 非寿险业务内含价值期初值 | number(19,4) | ✓ | 38.1% |  |
| 23 | `NAVBeforeChange` | 资本变动前净资产价值变化 | number(19,4) | ✓ | 38.1% |  |
| 24 | `CapitalInvestment` | 资本投资 | number(19,4) | ✓ | 36.51% |  |
| 25 | `AdjustedMarketValueGeneral` | 市场价值调整(非寿险业务) | number(19,4) | ✓ | 40.48% |  |
| 26 | `EndEVGeneralInsurance` | 非寿险业务期末内含价值 | number(19,4) | ✓ | 56.35% | 非寿险业务期末内含价值（EndEVGeneralInsurance）：直接取公司定期报告披露数据；若无披露，则为“非寿险... |
| 27 | `AdjustedMinorityInterests` | 少数股东权益调整 | number(19,4) | ✓ | 19.05% |  |
| 28 | `EndEVGroup` | 集团内含价值期末值 | number(19,4) | ✓ | 100.0% |  |
| 29 | `EndEVPS` | 每股内含价值期末值 | number(19,4) | ✓ | 39.68% |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### EVBeforeChange (资本变动前寿险内含价值)

资本变动前寿险内含价值（EVBeforeChange）=寿险业务内含价值期初值+内含价值预期回报+期间新业务价值+营运经验差异+红利分配差异+投资收益差异+风险贴现率变动+评估基础的改变+评估方法，假设和模型的改变+市场价值调整+其他

### EndEVLifeInsurance (寿险业务期末内含价值)

寿险业务期末内含价值（EndEVLifeInsurance）=资本变动前寿险内含价值+资本注入+股东股息

### EndEVGeneralInsurance (非寿险业务期末内含价值)

非寿险业务期末内含价值（EndEVGeneralInsurance）：直接取公司定期报告披露数据；若无披露，则为“非寿险业务内含价值期初值+资本变动前净资产价值变化+资本投资+市场价值调整变化”。

## SQL示例

```sql
-- 查询 保险公司内含价值变动 数据
SELECT *
FROM lc_embeddedvaluechange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
