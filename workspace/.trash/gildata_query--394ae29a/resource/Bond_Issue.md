# Bond_Issue

**中文名**: 债券发行与上市

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_Issue` |
| MySQL表名 | `bond_issue` |
| 中文名 | 债券发行与上市 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 40 |
| 版本 | 1 |

## 表描述

1.记录债券（可转换债券、交易所ABS除外）在不同市场上的发行和上市信息。
2.同一债券若在多个市场上市，将对应多条记录。
3.数据范围：1981-01-01 至今
4.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 主内部代码 | number(10) | ✗ | 100.0% | 主内部代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，... |
| 3 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `BondFullName` | 债券全称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `BondNature` | 债券类型 | number(10) | ✓ | 100.0% | 债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型... |
| 6 | `BondForm` | 债券形态 | number(10) | ✓ | 99.99% | 债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具... |
| 7 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and ... |
| 8 | `CrossExchange` | 是否跨市场 | number(10) | ✓ | 100.0% | 是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 9 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✓ | 100.0% |  |
| 10 | `Issuer` | 发行人 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `IssuerNature` | 发行人性质 | number(10) | ✓ | 100.0% | 发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND... |
| 12 | `Guarantor` | 担保人 | varchar2(1000) | ✓ | 4.97% |  |
| 13 | `GuarantMethod` | 担保方式 | number(10) | ✓ | 1.29% | 担保方式(GuarantMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1167，得到担... |
| 14 | `CRAs` | 评级人 | varchar2(1000) | ✓ | 27.97% |  |
| 15 | `CreditRating` | 债券信用级别 | varchar2(50) | ✓ | 27.97% |  |
| 16 | `LeadUnderwriter` | 主承销商 | varchar2(1000) | ✓ | 32.26% |  |
| 17 | `UnderwritingMethod` | 承销方式 | number(10) | ✓ | 30.28% | 承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 101... |
| 18 | `PublicAnnouncementDate` | 发行公告发布日期 | date | ✓ | 100.0% |  |
| 19 | `IssueObject` | 发行对象 | varchar2(200) | ✓ | 45.64% |  |
| 20 | `IssueMethod` | 发行方式 | varchar2(200) | ✓ | 99.86% |  |
| 21 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 99.93% |  |
| 22 | `IssueCommissionRate` | 发行手续费率 | number(10,6) | ✓ | 14.61% |  |
| 23 | `IssueStarDate` | 发行期起始日 | date | ✓ | 86.35% |  |
| 24 | `IssueEndDate` | 发行期截止日 | date | ✓ | 86.35% |  |
| 25 | `PlanIssueSize` | 计划发行总额(包含计划增发)(元) | number(19,2) | ✓ | 99.99% | 同一债券若在多个市场发行，债券发行人在披露发行规模时，一般将柜台发行量单独披露，而将深圳交易所、上海交易所、银行间的发行... |
| 26 | `ActualIssueSize` | 实际发行总额(包含实际增发)(元) | number(19,2) | ✓ | 99.82% | 同一债券若在多个市场发行，债券发行人在披露发行规模时，一般将柜台发行量单独披露，而将深圳交易所、上海交易所、银行间的发行... |
| 27 | `ApplyCodeOnline` | 网上认购代码 | varchar2(10) | ✓ | 0.16% |  |
| 28 | `ApplyUnitOnline` | 网上认购单位(元) | number(16,2) | ✓ | 0.15% |  |
| 29 | `ApplyMaxOnline` | 网上认购数量上限(元) | number(16,2) | ✓ | 0.01% |  |
| 30 | `ApplyMinOnline` | 网上认购数量下限(元) | number(16,2) | ✓ | 0.11% |  |
| 31 | `SubstriptionUnit` | 网下认购单位(元) | number(19,4) | ✓ | 12.99% |  |
| 32 | `ApplyMinOffline` | 网下认购数量下限(元) | number(16,2) | ✓ | 12.15% |  |
| 33 | `ExPuAnnouncementDay` | 上市公告书发布日期 | date | ✓ | 81.44% |  |
| 34 | `ListedDate` | 上市日 | date | ✓ | 98.04% |  |
| 35 | `Exchange` | 上市地点 | number(10) | ✓ | 100.0% | 上市地点(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 201，得到上市地点的具体... |
| 36 | `TradeUnit` | 交易单位(文字) | varchar2(200) | ✓ | 1.49% |  |
| 37 | `ParValuePer` | 每手面值(元) | number(19,4) | ✓ | 0.07% |  |
| 38 | `DelistDate` | 退市日 | date | ✓ | 84.81% |  |
| 39 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 40 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (主内部代码)

主内部代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### BondNature (债券类型)

债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型的具体描述：1-企业债券，2-金融债券，3-金融次级债，4-国债现货，5-央行票据，6-短期融资券，7-MBS(房贷支持)，8-ABS(其他支持)，9-混合资本债券，10-可转换债券，11-国库现金管理，12-资产证券化，13-公司债券，14-中期票据，15-转债分离公司债，16-地方政府债券，17-中小企业集合票据，18-集合债券，19-超短期融资券，20-非公开定向债务融资工具，21-次级定期债务，22-中小企业区域集优票据，23-政府支持债券，24-中小企业私募债券，25-资产支持票据，26-小微企业扶持债券，27-二级资本债券，28-中小企业可交换私募债，29-可交换公司债券，30-同业存单，31-区域集优中期票据，32-项目收益票据，33-项目收益债券，34-证券公司短期公司债券，35-保险公司资本补充债券，36-非公开发行公司债，37-信用风险缓释凭证，38-信用联结票据，39-其他一级资本工具，40-标准化票据，41-自贸区债，42-TLAC非资本债券，99-其他。

### BondForm (债券形态)

债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具体描述：1-实名制记帐式，2-无记名实物券，3-凭证式国债，4-其他形式，5-电子式储蓄国债。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1420,9990)，得到货币单位的具体描述：1000-美元，1420-人民币元，9990-特别提款权。

### CrossExchange (是否跨市场)

是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否跨市场的具体描述：1-是，2-否。

### IssuerNature (发行人性质)

发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM NOT IN (21)，得到发行人性质的具体描述：10-中央银行，11-政策性银行，13-商业银行，20-财政部，22-地方财政，29-其他部委，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，70-国际机构，75-自然人，80-外国主权政府，81-外国地方政府，91-建设基金，99-一般企业，100-地方融资平台。

### GuarantMethod (担保方式)

担保方式(GuarantMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1167，得到担保方式的具体描述：1-不可撤销担保，2-连带责任担保，3-不可撤销连带责任担保，4-其他担保，5-豁免担保，6-无条件不可撤消全额收购承诺，7-差额补偿。

### UnderwritingMethod (承销方式)

承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

### PlanIssueSize (计划发行总额(包含计划增发)(元))

同一债券若在多个市场发行，债券发行人在披露发行规模时，一般将柜台发行量单独披露，而将深圳交易所、上海交易所、银行间的发行量合计披露，鉴于此，我们在深圳交易所、上海交易所、银行间市场对应的发行总额下均收录三个市场的合计数据。若需要统计市场发行总额，为避免重复，请通过“债券规模（Bond_Size）”表获取相关信息。

## SQL示例

```sql
-- 查询 债券发行与上市 数据
SELECT *
FROM bond_issue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
