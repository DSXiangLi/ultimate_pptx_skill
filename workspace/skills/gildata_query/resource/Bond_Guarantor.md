# Bond_Guarantor

**中文名**: 债券担保人

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_Guarantor` |
| MySQL表名 | `bond_guarantor` |
| 中文名 | 债券担保人 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 24 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录债券担保机构的名称、性质、担保方式、担保期限、以及担保函内容等。
2.ABS内部增信由基础资产提供，本表提供的担保人均为ABS的原始权益人，仅供参考。
3.数据范围：1992-10-30 至今
4.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 债券内部代码 | number(10) | ✗ | 100.0% | 债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `PublishDate` | 公告日期 | date | ✓ | 99.99% |  |
| 5 | `GuaranteeType` | 最高担保类型 | number(10) | ✓ | 100.0% | 最高担保类型(GuaranteeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1438，得... |
| 6 | `GuarantorCode` | 担保人代码 | number(10) | ✓ | 100.0% | 担保人代码（GuarantorCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 7 | `GuarantorName` | 担保人名称 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `GuarantorNature` | 担保人性质 | number(10) | ✓ | 100.0% | 担保人性质(GuarantorNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414，... |
| 9 | `GuarantorInfo` | 担保人介绍 | clob | ✓ | 47.07% |  |
| 10 | `GuaranteeRange` | 担保范围与对象 | varchar2(500) | ✓ | 25.14% |  |
| 11 | `GuaranteeMethod` | 担保方式 | number(10) | ✓ | 100.0% | 担保方式(GuaranteeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1439 A... |
| 12 | `AssureGuaType` | 保证担保方式 | number(10) | ✓ | 28.65% | 保证担保方式(AssureGuaType)与(CT_SystemConst)表中的DM字段关联，令LB = 1439 A... |
| 13 | `GuaMaturity` | 担保期限(年) | number(18,8) | ✓ | 23.39% |  |
| 14 | `BeginDate` | 担保起始日期 | date | ✓ | 23.77% |  |
| 15 | `EndDate` | 担保结束日期 | date | ✓ | 23.65% |  |
| 16 | `GuaContent` | 担保函内容 | clob | ✓ | 11.24% |  |
| 17 | `GuaMaturityDesc` | 担保期限描述 | varchar2(500) | ✓ | 23.25% |  |
| 18 | `GuaranteeFee` | 担保费用(亿元) | number(19,8) | ✓ | 0.01% |  |
| 19 | `GuaranteeSum` | 担保金额(亿元) | number(19,8) | ✓ | 12.49% |  |
| 20 | `GuaranteeRatio` | 担保比例(%) | number(19,8) | ✓ | 28.28% |  |
| 21 | `TLowMoRatio` | 理论最低抵质押比率 | number(19,8) | ✓ | 0.6% |  |
| 22 | `MoRatioDesc` | 抵质押比率描述 | varchar2(2000) | ✓ | 0.84% |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (债券内部代码)

债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### GuaranteeType (最高担保类型)

最高担保类型(GuaranteeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1438，得到最高担保类型的具体描述：1-担保，2-再担保，3-反担保，4-收购承诺，5-差额补偿，6-其他增信。

### GuarantorCode (担保人代码)

担保人代码（GuarantorCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到担保机构的具体名称、基本信息等。

### GuarantorNature (担保人性质)

担保人性质(GuarantorNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414，得到担保人性质的具体描述：10-中央银行，11-政策性银行，13-商业银行，20-财政部，21-铁道部，22-地方财政，29-其他部委，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，70-国际机构，75-自然人，80-外国主权政府，81-外国地方政府，91-建设基金，99-一般企业，100-地方融资平台。

### GuaranteeMethod (担保方式)

担保方式(GuaranteeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1439 AND DM not in (101,111,113,115,116,1001)，得到担保方式的具体描述：100-保证，200-抵押，201-保证担保和抵押担保，300-质押，301-保证担保和质押担保，302-抵押担保和质押担保，303-保证担保，抵押担保和质押担保，400-留置，500-定金，600-交易型信用增进，700-其他担保，800-债券远期回购信用增进，900-豁免担保，1000-全额收购承诺，1100-流动性支持，1200-维好承诺，1300-保证金账户设置，1400-评级下调增信安排，1500-现金流净额覆盖不足增信安排，1600-保险代偿，2000-差额补偿人，3000-结构化设计，3100-超额覆盖，3200-超额利差，3300-超额利差-累计利息，3400-超额抵押，3500-设立储备账户，3600-信用触发器机制，3700-超额奖励服务费，3800-租赁押金担保。

### AssureGuaType (保证担保方式)

保证担保方式(AssureGuaType)与(CT_SystemConst)表中的DM字段关联，令LB = 1439 AND DM IN (101,111,113,115,116,1001)，得到保证担保方式的具体描述：101-一般保证，111-一般连带责任保证，113-不可撤销连带责任保证，115-无条件不可撤销连带责任保证，116-无限连带责任保证担保，1001-无条件不可撤销全额收购承诺。

## SQL示例

```sql
-- 查询 债券担保人 数据
SELECT *
FROM bond_guarantor
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
