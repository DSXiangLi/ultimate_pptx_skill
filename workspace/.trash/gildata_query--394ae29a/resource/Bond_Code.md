# Bond_Code

**中文名**: 债券代码对照表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_Code` |
| MySQL表名 | `bond_code` |
| 中文名 | 债券代码对照表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 37 |
| 版本 | 1.04 |

## 表描述

1.针对同一债券在不同市场的交易代码不统一的问题，设置了“统一内部编码”，与发行的债券对应，不随交易市场而改变。
2.同一债券在不同交易市场交易，对应不同的“债券内部编码（InnerCode）”。
3.通过对“证券市场（SecuMarket）”的选择，可以得到债券在该市场上的交易代码、交易简称、债券内部编码等。
4.此表不包含取消发行债券。
5.数据范围：1990-12-01 至今
6.信息来源：中债登、货币网、上清所、上交所、深交所、北交所等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 统一内部编码(不同市场交易的同一债券) | number(10) | ✗ | 100.0% | 针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。MainCod... |
| 3 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。同一只债券在不... |
| 4 | `CompanyCode` | 公司代码(发债公司内部编码) | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：ABS的公司代码展示的是原始权益人/发起机构总的代码，其他类型债券的公司代码展示的是... |
| 5 | `SecuCode` | 债券代码 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `SecuAbbr` | 债券简称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `ChiSpelling` | 拼音债券简称 | varchar2(50) | ✓ | 100.0% |  |
| 8 | `ExtendedAbbr` | 扩位简称 | varchar2(100) | ✓ | 2.76% |  |
| 9 | `ExtendedSpelling` | 拼音扩位简称 | varchar2(50) | ✓ | 2.76% |  |
| 10 | `ChiName` | 债券全称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `ChiNameAbbr` | 中文名称缩写 | varchar2(100) | ✓ | 29.22% |  |
| 12 | `EngName` | 英文名称 | varchar2(200) | ✓ | 99.6% |  |
| 13 | `EngNameAbbr` | 英文名称缩写 | varchar2(50) | ✓ | 1.54% |  |
| 14 | `IssueYear` | 债券年度 | number(10) | ✓ | 99.88% |  |
| 15 | `IssuePhase` | 债券期次 | number(10) | ✓ | 99.88% |  |
| 16 | `Currency` | 计量货币 | number(10) | ✓ | 100.0% | 计量货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM i... |
| 17 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM ... |
| 18 | `ListedDate` | 上市日期 | date | ✓ | 97.34% |  |
| 19 | `ListedSector` | 上市板块 | number(10) | ✓ | 100.0% | 上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207，得到上市板... |
| 20 | `ListedState` | 上市状态 | number(10) | ✓ | 100.0% | 上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND D... |
| 21 | `DelistDate` | 摘牌日 | date | ✓ | 83.06% |  |
| 22 | `Issuer` | 发行人 | varchar2(200) | ✓ | 100.0% |  |
| 23 | `IssuerNature` | 发行人性质 | number(10) | ✓ | 100.0% | 发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 and... |
| 24 | `IssuerCode` | 发行人代码 | number(10) | ✓ |  | 发行人代码（IssuerCode）：ABS的发行人代码目前展示的是原始权益人/发起机构的代码，同OriginatorCo... |
| 25 | `GuarantorCode` | 担保人代码 | number(10) | ✓ |  |  |
| 26 | `CreatOrgCode` | 发起机构代码 | number(10) | ✓ |  |  |
| 27 | `OriginatorCode` | 原始权益人代码 | number(10) | ✓ |  |  |
| 28 | `ManagerCode` | 受托机构/计划管理人代码 | number(10) | ✓ |  |  |
| 29 | `CustodyCode` | 托管银行代码 | number(10) | ✓ |  |  |
| 30 | `InterestEndDate` | 到期日 | date | ✓ | 99.87% | 依次取以下字段非空值：实际到期日、债券截止日；对于可转债，依次取以下字段非空值：停止转股日、实际到期日、债券期限截止日。 |
| 31 | `BondNature` | 债券类别 | number(10) | ✓ | 100.0% | 债券类别(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类别... |
| 32 | `BondTypeLevel1` | 债券分类(级别1) | number(10) | ✓ | 100.0% | 债券分类(级别1)(BondTypeLevel1),该字段固定以下常量：1000-国债,1100-央行票据,1200-政... |
| 33 | `BondTypeLevel1Desc` | 债券分类说明(级别1) | varchar2(50) | ✓ | 100.0% |  |
| 34 | `BondTypeLevel2` | 债券分类(级别2) | number(10) | ✓ | 100.0% | 债券分类(级别2)(BondTypeLevel2),该字段固定以下常量：1001-记帐式国债,1002-凭证式国债,10... |
| 35 | `BondTypeLevel2Desc` | 债券分类说明(级别2) | varchar2(50) | ✓ | 100.0% |  |
| 36 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 37 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (统一内部编码(不同市场交易的同一债券))

针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。MainCode与发行的债券对应，不随交易市场而改变。

### InnerCode (债券内部编码)

针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。同一只债券在不同的交易市场将产生多个InnerCode，对于同一只债券，一个市场对应一个InnerCode。

### CompanyCode (公司代码(发债公司内部编码))

公司代码（CompanyCode）：ABS的公司代码展示的是原始权益人/发起机构总的代码，其他类型债券的公司代码展示的是发债人的公司代码

### Currency (计量货币)

计量货币(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1420,3000,9990)，得到计量货币的具体描述：1000-美元，1420-人民币元，3000-欧元，9990-特别提款权。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM in (16,18,71,73,81,83,84,89,90,310)，得到证券市场的具体描述：16-上海票据交易所，18-北京证券交易所，71-柜台交易市场，73-一级市场，81-三板市场，83-上海证券交易所，84-其他市场，89-银行间债券市场，90-深圳证券交易所，310-机构间私募产品报价与服务系统。

### ListedSector (上市板块)

上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207，得到上市板块的具体描述：1-主板，2-中小企业板，3-三板，4-其他，5-大宗交易系统，6-创业板，7-科创板，8-北交所股票，101-纳斯达克全球精选市场（NASDAQ-GS），102-纳斯达克全球市场（NASDAQ-GM），103-纳斯达克资本市场（NASDAQ-CM），201-伦交所主板，202-伦交所主板-高级市场，203-伦交所主板-标准市场，204-伦交所主板-高增长市场，205-伦交所主板-高科技市场，210-伦交所另类投资市场，220-伦交所专家证券市场，230-伦交所专家基金市场，240-伦交所环球板(GES)。

### ListedState (上市状态)

上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,3,5,9)，得到上市状态的具体描述：1-上市，3-暂停，5-终止，9-其他。

### IssuerNature (发行人性质)

发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 and DM not in (21)，得到发行人性质的具体描述：10-中央银行，11-政策性银行，13-商业银行，20-财政部，22-地方财政，29-其他部委，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，70-国际机构，75-自然人，80-外国主权政府，81-外国地方政府，91-建设基金，99-一般企业，100-地方融资平台。

### IssuerCode (发行人代码)

发行人代码（IssuerCode）：ABS的发行人代码目前展示的是原始权益人/发起机构的代码，同OriginatorCode和CreatOrgCode。其中交易所ABS展示的是原始权益人，银行间ABS展示的是发起机构；其他类型债券展示的是发债人的公司代码，同CompanyCode

### InterestEndDate (到期日)

依次取以下字段非空值：实际到期日、债券截止日；对于可转债，依次取以下字段非空值：停止转股日、实际到期日、债券期限截止日。

## SQL示例

```sql
-- 查询 债券代码对照表 数据
SELECT *
FROM bond_code
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
