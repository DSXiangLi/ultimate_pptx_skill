# LC_EmbeddedValue

**中文名**: 保险公司内含价值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_EmbeddedValue` |
| MySQL表名 | `lc_embeddedvalue` |
| 中文名 | 保险公司内含价值 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 季更新 |
| 字段数量 | 44 |
| 版本 | 1.02 |

## 表描述

1.反映保险公司披露的内含价值表数据
2.收录保险公司在报告期末未调整和调整的合并报表
3.由于披露精度的问题，数据校验时，可能在百万位上有小额差异
4.该表中各科目的单位均为人民币元
5.数据范围：2005-12-31至今
6.信息来源：定期报告、招股意向书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% |  |
| 5 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 6 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `IfMerged` | 是否合并 | number(10) | ✓ | 100.0% | 是否合并（IfMerged），该字段固定以下常量：1-合并报表 |
| 9 | `IfAdjusted` | 是否调整 | number(10) | ✓ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 10 | `ANAVGroup` | 集团经调整净资产价值 | number(19,4) | ✓ | 63.8% |  |
| 11 | `ANAVLifeInsurance` | 寿险业务调整净资产 | number(19,4) | ✓ | 65.44% |  |
| 12 | `ANAVGroupInLife` | 集团应占寿险业务调整净资产 | number(19,4) | ✓ | 65.44% | 集团应占寿险业务调整净资产（ANAVGroupInLife）=寿险业务经调整的净资产价值*集团持有寿险业务股份比率 |
| 13 | `ANAVGroupInGeneral` | 集团应占非寿险业务调整净资产 | number(19,4) | ✓ | 60.94% | 集团应占非寿险业务调整净资产（ANAVGroupInGeneral）=集团经调整净资产价值-寿险业务经调整的净资产价值*... |
| 14 | `PrimeVIFB` | 1999年6月前承保未扣除偿付能力额度成本有效业务价值 | number(19,4) | ✓ | 19.22% |  |
| 15 | `LatterVIFB` | 1999年6月后承保未扣除偿付能力额度成本有效业务价值 | number(19,4) | ✓ | 19.22% |  |
| 16 | `VIFB` | 有效业务价值 | number(19,4) | ✓ | 68.3% | 有效业务价值（VIFB）：直接取公司定期报告披露数据；若无披露，则为“1999年6月前承保的未扣除偿付能力额度成本的有效... |
| 17 | `SolvencyMarginVIFB` | 持有偿付能力额度成本(有效业务价值) | number(19,4) | ✓ | 68.3% | 持有偿付能力额度成本（有效业务价值）（SolvencyMarginVIFB）：直接取公司定期报告披露数据；若无披露，则为... |
| 18 | `VIFBExcludeCost` | 扣除成本的有效业务价值 | number(19,4) | ✓ | 68.3% | 扣除成本的有效业务价值（VIFBExcludeCost）：直接取公司定期报告披露数据；若无披露，则为“有效业务价值+持有... |
| 19 | `RatioGroupInLife` | 集团持有寿险业务股份比例(%) | number(9,6) | ✓ | 14.72% |  |
| 20 | `VIFBGroupInLife` | 集团应占有效业务价值 | number(19,4) | ✓ | 68.3% | 集团应占寿险业务价值（VIFBGroupInLife）：直接取公司定期报告披露数据；若无披露，则为“扣除成本的有效业务价... |
| 21 | `EVGroup` | 集团内含价值 | number(19,4) | ✓ | 71.37% |  |
| 22 | `EVLifeInsurance` | 寿险业务内含价值 | number(19,4) | ✓ | 67.08% |  |
| 23 | `EVGroupInLife` | 集团应占寿险业务内含价值 | number(19,4) | ✓ | 67.08% | 集团应占寿险业务内含价值（EVGroupInLife）=寿险业务内含价值*集团持有寿险业务股份比率 |
| 24 | `EVGroupInGeneral` | 集团应占非寿险业务内含价值 | number(19,4) | ✓ | 67.08% | 集团应占非寿险业务内含价值（EVGroupInGeneral）=集团内含价值-寿险业务内含价值*集团持有寿险业务股份比率 |
| 25 | `NBusinessValue` | 新业务价值 | number(19,4) | ✓ | 75.87% | 新业务价值(NBusinessValue)：①当为年度报告时，优先展示扣除成本后一年新业务价值；如为空，则展示扣除成本前... |
| 26 | `FNBV` | 一年新业务价值 | number(19,4) | ✓ | 56.24% |  |
| 27 | `SolvencyMarginFNBV` | 持有偿付能力额度成本(新业务价值) | number(19,4) | ✓ | 54.81% |  |
| 28 | `FNBVExcludeCost` | 扣除成本的一年新业务价值 | number(19,4) | ✓ | 56.24% |  |
| 29 | `FNBVGroupInLife` | 集团应占一年新业务价值 | number(19,4) | ✓ | 56.24% | 集团应占一年新业务价值（FNBVGroupInLife）：直接取公司定期报告披露数据；若无披露，则为“扣除成本的一年新业... |
| 30 | `RiskDiscountRateEV` | 内含价值风险贴现率(%) | number(9,6) | ✓ | 75.66% |  |
| 31 | `RiskDiscountRateFNBV` | 新业务价值风险贴现率(%) | number(9,6) | ✓ | 62.37% |  |
| 32 | `RemarkOfRDR` | 风险贴现率说明 | varchar2(500) | ✓ | 75.26% |  |
| 33 | `ReturnOnInvestment` | 初始投资收益率(%) | number(9,6) | ✓ | 85.69% |  |
| 34 | `OriginYearROI` | 起始年度(初始投资收益率) | date | ✓ | 46.83% |  |
| 35 | `ChangingPattern` | 变化模式 | varchar2(50) | ✓ | 63.39% |  |
| 36 | `SteadyReturnOnInvestment` | 稳定期投资收益率(%) | number(9,6) | ✓ | 71.37% |  |
| 37 | `OriginYearSROI` | 起始年度(稳定期投资收益率) | date | ✓ | 39.88% |  |
| 38 | `RemarkOfROI` | 投资收益率说明 | varchar2(500) | ✓ | 85.69% |  |
| 39 | `IncomeTaxRate` | 所得税率(%) | number(9,6) | ✓ | 80.16% |  |
| 40 | `ExemptIncomeTaxRate` | 投资收益豁免所得税比率 | number(9,6) | ✓ | 42.54% |  |
| 41 | `RemarkOfITR` | 所得税率说明 | varchar2(500) | ✓ | 80.16% |  |
| 42 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 43 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 44 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfMerged (是否合并)

是否合并（IfMerged），该字段固定以下常量：1-合并报表

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,7)，得到是否调整的具体描述：1-是，2-否，7-二季末调整。

### ANAVGroupInLife (集团应占寿险业务调整净资产)

集团应占寿险业务调整净资产（ANAVGroupInLife）=寿险业务经调整的净资产价值*集团持有寿险业务股份比率

### ANAVGroupInGeneral (集团应占非寿险业务调整净资产)

集团应占非寿险业务调整净资产（ANAVGroupInGeneral）=集团经调整净资产价值-寿险业务经调整的净资产价值*集团持有寿险业务股份比率

### VIFB (有效业务价值)

有效业务价值（VIFB）：直接取公司定期报告披露数据；若无披露，则为“1999年6月前承保的未扣除偿付能力额度成本的有效业务价值+1999年6月后承保的未扣除偿付能力额度成本的有效业务价值”。

### SolvencyMarginVIFB (持有偿付能力额度成本(有效业务价值))

持有偿付能力额度成本（有效业务价值）（SolvencyMarginVIFB）：直接取公司定期报告披露数据；若无披露，则为“扣除成本的有效业务价值-有效业务价值”。

### VIFBExcludeCost (扣除成本的有效业务价值)

扣除成本的有效业务价值（VIFBExcludeCost）：直接取公司定期报告披露数据；若无披露，则为“有效业务价值+持有的偿付能力额度成本”。

### VIFBGroupInLife (集团应占有效业务价值)

集团应占寿险业务价值（VIFBGroupInLife）：直接取公司定期报告披露数据；若无披露，则为“扣除成本的有效业务价值*集团持有寿险业务股份比率”。

## SQL示例

```sql
-- 查询 保险公司内含价值 数据
SELECT *
FROM lc_embeddedvalue
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
