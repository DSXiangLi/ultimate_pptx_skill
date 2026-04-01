# Bond_CallPutInfoN

**中文名**: 含权债回售赎回情况新表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CallPutInfoN` |
| MySQL表名 | `bond_callputinfon` |
| 中文名 | 含权债回售赎回情况新表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 60 |
| 版本 | 1.05 |

## 表描述

1.收录非可转换债券含权债的含权行权情况，主要包含：发行人赎回权、利息递延权、上调票面利率选择权、持有人回售权、提前兑付权、定向转让权、延期选择权、暂停索偿权。
2.包括行权期间、行权价格、行权操作日、最低操作金额、行权金额等信息。
3.本表信息通过InnerCode维度展示，能够体现含权行权信息的跨市场差异情况。
4.数据范围：1994-03-10至今
5.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到债... |
| 3 | `InfoPublDate` | 公告日期 | date | ✓ | 100.0% |  |
| 4 | `OpType` | 行权类型 | number(10) | ✓ | 100.0% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM NOT... |
| 5 | `OpTypeSecond` | 行权类型二级 | number(10) | ✓ | 100.0% | 行权类型二级(OpTypeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2063 an... |
| 6 | `OptionMark` | 权利标识 | number(10) | ✓ | 30.47% | 权利标识(OptionMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2286，得到权利标识... |
| 7 | `OpBenchmark` | 权利挂钩基准 | number(10) | ✓ | 2.38% | 权利挂钩基准(OpBenchmark)与(CT_SystemConst)表中的DM字段关联，令LB = 2404，得到权... |
| 8 | `OpRemark` | 权利描述 | clob | ✓ | 80.18% |  |
| 9 | `ExpectedExerciseDate` | 权利可能行使日 | date | ✓ | 67.76% |  |
| 10 | `OpProgress` | 行权进程 | number(10) | ✓ | 100.0% | 行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程... |
| 11 | `IfOption` | 是否行权 | number(10) | ✓ | 21.02% | 是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN... |
| 12 | `OptionReason` | 行权原因说明 | varchar2(2000) | ✓ | 21.07% |  |
| 13 | `CommOpApplStDate` | 行权申请起始日 | date | ✓ | 9.32% |  |
| 14 | `CommOpApplEdDate` | 行权申请截止日 | date | ✓ | 9.31% |  |
| 15 | `CallRegDate` | 赎回登记日 | date | ✓ | 0.25% |  |
| 16 | `CommOptionDate` | 行权操作日 | date | ✓ | 17.52% |  |
| 17 | `CommOpPrice` | 行权价格(含税,元/张) | number(19,4) | ✓ | 23.06% |  |
| 18 | `CommOpPriceTaxed` | 行权价格(扣税,元/张) | number(19,4) | ✓ | 0.04% |  |
| 19 | `IfIncludeInterest` | 是否包含利息 | number(10) | ✓ | 23.06% | 是否包含利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 99... |
| 20 | `Interest` | 利息(元) | number(19,4) | ✓ | 0.45% |  |
| 21 | `FRNRefExtraMarginMax` | 计息额外利差最大值(%) | number(9,6) | ✓ | 6.56% |  |
| 22 | `FRNRefExtraMarginMin` | 计息额外利差最小值(%) | number(9,6) | ✓ | 6.56% |  |
| 23 | `LeastOpVol` | 最低操作金额(元) | number(19,4) | ✓ | 6.61% |  |
| 24 | `CallCode` | 回售/赎回代码 | varchar2(10) | ✓ | 1.56% |  |
| 25 | `CallName` | 回售/赎回简称 | varchar2(50) | ✓ | 1.5% |  |
| 26 | `CommOpApplStTime` | 行权申请受理开始时间 | varchar2(10) | ✓ | 0.51% |  |
| 27 | `CommOpApplEdTime` | 行权申请受理截止时间 | varchar2(10) | ✓ | 0.52% |  |
| 28 | `CallOrPutResultPublDate` | 回售/赎回结果公告日 | date | ✓ | 2.38% |  |
| 29 | `CallOrPutVol` | 被赎回/回售/收购金额(元) | number(19,4) | ✓ | 0.66% |  |
| 30 | `CallOrPutVol_Total` | 全市场被赎回/回售/收购金额总额(元) | number(19,4) | ✓ | 10.83% |  |
| 31 | `AllocatingCallMonDay` | 行权后款项到账日 | date | ✓ | 8.78% |  |
| 32 | `ResaleStTime` | 转售起始日 | date | ✓ | 1.74% |  |
| 33 | `ResaleEdTime` | 转售截止日 | date | ✓ | 1.72% |  |
| 34 | `ResaleRegDate` | 转售面额登记日 | date | ✓ | 0.15% |  |
| 35 | `EstimateResaleVol` | 预计转售金额(元) | number(19,4) | ✓ | 1.73% |  |
| 36 | `ActResaleVol` | 实际转售金额(元) | number(19,4) | ✓ | 1.99% |  |
| 37 | `ResaleCompanyCode` | 转售专业机构代码 | number(10) | ✓ | 0.15% |  |
| 38 | `OutstandingBDVol_Total` | 全市场剩余债券金额总额(元) | number(19,4) | ✓ | 10.45% |  |
| 39 | `RateAdded` | 债券剩余部分增加的票面利率(%) | number(9,4) | ✓ | 10.8% |  |
| 40 | `RevokeStartDate` | 撤销起始日 | date | ✓ | 3.28% |  |
| 41 | `RevokeEndDate` | 撤销截止日 | date | ✓ | 3.28% |  |
| 42 | `ReceiverCode` | 转让对象企业编号 | number(10) | ✓ | 0.03% | 转让对象企业编号（ReceiverCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Com... |
| 43 | `ReceiverName` | 转让对象名称 | varchar2(100) | ✓ | 0.03% |  |
| 44 | `OfferPlanSize` | 计划收购规模(元) | number(19,8) | ✓ | 0.09% |  |
| 45 | `LockupDate` | 标的债券锁定申报截止日期 | date | ✓ | 0.09% |  |
| 46 | `LockupTime` | 标的债券锁定申报截止时间 | varchar2(10) | ✓ | 0.09% |  |
| 47 | `TargetLockUpDate` | 标的债券锁定日 | date | ✓ | 0.09% |  |
| 48 | `PurchaseMethod` | 收购方式 | number(10) | ✓ | 0.09% | 收购方式(PurchaseMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2381，得到... |
| 49 | `OfferPriceType` | 收购价格方式 | number(10) | ✓ | 0.09% | 收购价格方式(OfferPriceType)与(CT_SystemConst)表中的DM字段关联，令LB = 2382，... |
| 50 | `ObjectionStart` | 要约收购异议提起期间起始 | date | ✓ | 0.09% |  |
| 51 | `ObjectionEnd` | 要约收购异议提起期间截止 | date | ✓ | 0.09% |  |
| 52 | `OfferDeclareVol` | 标的债券申报额(元) | number(19,8) | ✓ | 0.08% |  |
| 53 | `OfferStatus` | 要约收购公告状态 | number(10) | ✓ | 0.09% | 要约收购公告状态(OfferStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2383，得... |
| 54 | `DIType` | 递延利息计息类型 | number(10) | ✓ | 3.16% | 递延利息计息类型(DIType)与(CT_SystemConst)表中的DM字段关联，令LB = 2403，得到递延利息... |
| 55 | `DIBasePoint` | 递延利息计息固定基点(BP) | number(19,8) | ✓ | 0.01% |  |
| 56 | `DIRealRate` | 递延利息最终计息利率(%) | number(19,8) | ✓ | 0.01% |  |
| 57 | `DIForeRate` | 递延利息预计计息利率(%) | number(19,8) | ✓ | 0.01% |  |
| 58 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 59 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 60 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM NOT IN (108,207,209,301)，得到行权类型的具体描述：101-发行人赎回权，103-发行人利息递延权，105-发行人调整票面利率选择权，106-发行人续期选择权，107-发行人减记条款，109-回拨选择权，110-可转债转股价格修正，201-持有人回售权，202-持有人提前兑付权，203-持有人定向转让权，205-持有人延期选择权，401-暂停索偿权，501-债务减计（核销）和转股条款，601-投资者保护条款，701-债务回购，999-其他。

### OpTypeSecond (行权类型二级)

行权类型二级(OpTypeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2063 and DM not in (10801)，得到行权类型二级的具体描述：10101-发行人赎回权，10102-可转债到期赎回，10103-原始权益人基础资产回购权，10301-发行人利息递延权，10501-发行人调整票面利率选择权，10601-发行人续期选择权，10602-永续条款，10701-发行人减记条款，10901-网上网下回拨选择权，10902-品种间回拨选择权，11001-可转债转股价格修正，20101-持有人回售权，20102-有条件回售，20103-无条件回售，20104-时点回售，20105-附加回售，20201-持有人提前兑付权，20301-持有人定向转让权，20501-持有人延期选择权，20701-持有人可调换选择权，20901-持有人可转换选择权，30101-合并，40101-暂停索偿权，50101-债务减计（核销）和转股条款，60101-交叉违约，60102-控制权变更，60103-事先约束，70101-债务回购，70102-要约收购，99901-其他。

### OptionMark (权利标识)

权利标识(OptionMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2286，得到权利标识的具体描述：1001-向上调整，1002-向下调整，1003-不确定调整方向，2001-可撤销，2002-不可撤销。

### OpBenchmark (权利挂钩基准)

权利挂钩基准(OpBenchmark)与(CT_SystemConst)表中的DM字段关联，令LB = 2404，得到权利挂钩基准的具体描述：101-可持续发展绩效目标，102-大宗商品价格，103-碳收益，104-股权投资收益率，201-税务政策变更，202-会计准则变更，203-银行业监管规则变化，204-税务政策变更或会计准则变更，205-法律变更，301-持有人回售。

### OpProgress (行权进程)

行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程的具体描述：1-发行时权利约定，2-行权提示与结果。

### IfOption (是否行权)

是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行权的具体描述：1-是，2-否。

### IfIncludeInterest (是否包含利息)

是否包含利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含利息的具体描述：1-是，2-否。

### ReceiverCode (转让对象企业编号)

转让对象企业编号（ReceiverCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到转让对象的具体名称、基本信息等。

### PurchaseMethod (收购方式)

收购方式(PurchaseMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2381，得到收购方式的具体描述：1-现金收购。

## SQL示例

```sql
-- 查询 含权债回售赎回情况新表 数据
SELECT *
FROM bond_callputinfon
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
