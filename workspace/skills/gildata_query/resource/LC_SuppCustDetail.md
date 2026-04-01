# LC_SuppCustDetail

**中文名**: 公司供应商与客户

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SuppCustDetail` |
| MySQL表名 | `lc_suppcustdetail` |
| 中文名 | 公司供应商与客户 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司产品供销 |
| 更新频率 | 不定期更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：收录A股上市公司的主要供应商、客户清单，以及交易标的、交易金额等信息。
2.数据范围：2015年至今
3.信息来源：招股说明书、定报

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `RelationType` | 关系类型 | number(10) | ✗ | 100.0% | 关系类型(RelationType)与(CT_SystemConst)表中的DM字段关联，令LB = 1590 AND ... |
| 8 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% | 序号(SerialNumber)：999表示前5大客户、前5大供应商的合计值；990表示前5大客户、前5大供应商关联方合... |
| 9 | `RelatedPartyName` | 供应商/客户名称 | varchar2(600) | ✓ | 100.0% |  |
| 10 | `RelatedPartyCode` | 供应商/客户代码 | number(10) | ✓ | 23.09% | 供应商/客户代码(RelatedPartyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号... |
| 11 | `RelatedPartyAttribute` | 供应商/客户属性 | number(10) | ✓ | 100.0% | 供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令L... |
| 12 | `TargetName` | 交易标的名称 | varchar2(100) | ✓ | 15.36% |  |
| 13 | `TargetCode` | 交易标的代码 | number(10) | ✓ | 7.21% |  |
| 14 | `TradingValue` | 交易金额(元) | number(19,4) | ✓ | 97.07% |  |
| 15 | `Ratio` | 占比(%) | number(9,6) | ✓ | 99.23% |  |
| 16 | `Remark` | 备注 | varchar2(1000) | ✓ | 10.89% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到A股上市公司的交易代码、简称等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (110101,110102,120102,120103,120106,120205,130102,130103,130104,130106,130107,130111)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120106-临时公告:公开转让说明书(更正后)，120205-临时公告:其他，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130111-发行上市书:其他。

### RelationType (关系类型)

关系类型(RelationType)与(CT_SystemConst)表中的DM字段关联，令LB = 1590 AND DM IN (4,6)，得到关系类型的具体描述：4-客户，6-供应商。

### SerialNumber (序号)

序号(SerialNumber)：999表示前5大客户、前5大供应商的合计值；990表示前5大客户、前5大供应商关联方合计值

### RelatedPartyCode (供应商/客户代码)

供应商/客户代码(RelatedPartyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到所属公司的基础信息。

### RelatedPartyAttribute (供应商/客户属性)

供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到供应商/客户属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 公司供应商与客户 数据
SELECT *
FROM lc_suppcustdetail
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
