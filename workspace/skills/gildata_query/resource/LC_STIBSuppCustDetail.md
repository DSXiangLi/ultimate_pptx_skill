# LC_STIBSuppCustDetail

**中文名**: 科创板公司供应商与客户

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSuppCustDetail` |
| MySQL表名 | `lc_stibsuppcustdetail` |
| 中文名 | 科创板公司供应商与客户 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 产品供销 |
| 更新频率 | 不定期更新 |
| 字段数量 | 19 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录科创板公司主要供应商、客户清单，以及交易标的、交易金额等信息。
2.数据范围：2016年至今
3.信息来源：招股说明书、定报

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码(CompanyCode)：与“证券主表(SecuMain)”中的“公司代码(CompanyCode)”关联，令... |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `RelationType` | 关系类型 | number(10) | ✗ | 100.0% | 关系类型(RelationType)与(CT_SystemConst)表中的DM字段关联，令LB = 1590，得到关系... |
| 8 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% | 序号(SerialNumber)：999表示前5大客户、前5大供应商的合计值 |
| 9 | `RelatedPartyName` | 供应商/客户名称 | varchar2(600) | ✓ | 100.0% |  |
| 10 | `RelatedPartyCode` | 供应商/客户代码 | number(10) | ✓ | 30.34% | 关联企业代码(RelatedPartyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(C... |
| 11 | `RelatedPartyAttribute` | 供应商/客户属性 | number(10) | ✓ | 100.0% | 供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令L... |
| 12 | `TargetName` | 交易标的名称 | varchar2(100) | ✓ | 32.29% |  |
| 13 | `TargetCode` | 交易标的代码 | number(10) | ✓ | 14.25% |  |
| 14 | `TradingValue` | 交易金额(元) | number(19,4) | ✓ | 99.75% |  |
| 15 | `Ratio` | 占比(%) | number(9,6) | ✓ | 99.87% |  |
| 16 | `Remark` | 备注 | varchar2(1000) | ✓ | 19.48% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码(CompanyCode)：与“证券主表(SecuMain)”中的“公司代码(CompanyCode)”关联，令上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (110101, 110102, 120102, 120103, 130102, 130106)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，130102-发行上市书:招股说明书(申报稿)，130106-发行上市书:招股说明书。

### RelationType (关系类型)

关系类型(RelationType)与(CT_SystemConst)表中的DM字段关联，令LB = 1590，得到关系类型的具体描述：1-非关联方，2-关联方，3-往来单位，4-客户，5-子公司，6-供应商。

### SerialNumber (序号)

序号(SerialNumber)：999表示前5大客户、前5大供应商的合计值

### RelatedPartyCode (供应商/客户代码)

关联企业代码(RelatedPartyCode)：与“机构基本资料(LC_InstiArchive)”中的“企业编号(CompanyCode)”关联，得到所属公司的基础信息。

### RelatedPartyAttribute (供应商/客户属性)

供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到供应商/客户属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 科创板公司供应商与客户 数据
SELECT *
FROM lc_stibsuppcustdetail
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
