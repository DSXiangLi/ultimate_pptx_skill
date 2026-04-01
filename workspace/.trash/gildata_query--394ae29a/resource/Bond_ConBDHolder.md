# Bond_ConBDHolder

**中文名**: 可转债持有人持券情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDHolder` |
| MySQL表名 | `bond_conbdholder` |
| 中文名 | 可转债持有人持券情况 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 21 |
| 版本 | 1.03 |

## 表描述

1.交易所市场可转换债券持有人的持券变动情况。
2.可通过可转债持有人的代码，得到持有人的其他信息。
3.数据范围：1999-06-30 至今
4.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.99% |  |
| 5 | `OutstandingAmount` | 可转债剩余金额(元) | number(19,4) | ✓ | 95.92% |  |
| 6 | `HolderNumber` | 持有人户数(户) | number(10) | ✓ | 45.86% |  |
| 7 | `HolderSN` | 持有人序号 | number(10) | ✓ | 100.0% |  |
| 8 | `HolderName` | 持有人名称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `HoldAmount` | 持有金额(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `HoldVolume` | 持有数量(张) | number(18,2) | ✓ | 100.0% |  |
| 11 | `HoldRatio` | 持有比例(%) | number(9,6) | ✓ | 99.55% |  |
| 12 | `HolderRelationship` | 持有人之间关联关系 | varchar2(100) | ✓ | 0.02% |  |
| 13 | `HolderAttribute` | 持有人所属性质 | number(10) | ✓ | 99.92% | 持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 178... |
| 14 | `HolderNatureType` | 持有人性质编码 | number(10) | ✓ | 100.0% | 持有人性质编码(HolderNatureType)与(CT_SystemConst)表中的DM字段关联，令LB = 10... |
| 15 | `HolderNature` | 持有人性质 | varchar2(300) | ✓ | 100.0% |  |
| 16 | `RelatedCompanyCode` | 所属公司代码 | number(10) | ✓ | 42.47% | 所属公司代码（RelatedCompanyCode）：当债券持有人是上市公司或基金时，该字段下有数据，通过与“证券主表（... |
| 17 | `AgentCode` | 持有人代码 | number(10) | ✓ | 72.51% | 持有人代码(AgentCode)：当持有人所属性质（HolderAttribute）=2时，与EP_CompanyMai... |
| 18 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 19 | `Remark` | 备注 | varchar2(500) | ✓ | 0.03% |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### HolderAttribute (持有人所属性质)

持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持有人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### HolderNatureType (持有人性质编码)

持有人性质编码(HolderNatureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1026 AND DM NOT IN (13,16,40,50,60,61,67)，得到持有人性质编码的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，14-职工工会，15-财务公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，64-保险投资组合，66-保险资管产品，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### RelatedCompanyCode (所属公司代码)

所属公司代码（RelatedCompanyCode）：当债券持有人是上市公司或基金时，该字段下有数据，通过与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，可以得到持债人的相关信息。

### AgentCode (持有人代码)

持有人代码(AgentCode)：当持有人所属性质（HolderAttribute）=2时，与EP_CompanyMain表CompanyCode关联； 当持有人所属性质（HolderAttribute）=3时，与SecuMainAll表InnerCode关联。

## SQL示例

```sql
-- 查询 可转债持有人持券情况 数据
SELECT *
FROM bond_conbdholder
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
