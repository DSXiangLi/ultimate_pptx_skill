# HK_LongTermInvDet

**中文名**: 港股长期股权投资明细表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_LongTermInvDet` |
| MySQL表名 | `hk_longterminvdet` |
| 中文名 | 港股长期股权投资明细表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股长期股权投资明细表，记录港股上市公司对外持有子公司、联营企业、合营企业资料和持股明细。
2.数据范围：2009年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InnerCode` | 证券内部代码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `InfoSourceCode` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 ... |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 9 | `InvObjectsCla` | 投资对象分类 | number(10) | ✓ | 100.0% | 投资对象分类(InvObjectsCla)与(CT_SystemConst)表中的DM字段关联，令LB = 1596，得... |
| 10 | `HoldingWay` | 持有方式 | number(10) | ✓ | 100.0% | 持有方式(HoldingWay)与(CT_SystemConst)表中的DM字段关联，令LB = 1904，得到持有方式... |
| 11 | `InvCompName` | 投资公司名称 | varchar2(200) | ✗ | 100.0% |  |
| 12 | `EquityRatio` | 持股比例(%) | number(18,2) | ✓ | 97.86% |  |
| 13 | `MainBusiness` | 公司主营业务 | varchar2(500) | ✓ | 97.56% |  |
| 14 | `Remark` | 备注 | varchar2(500) | ✓ | 3.68% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InnerCode (证券内部代码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### InfoSourceCode (信息来源代码)

信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1926 AND DM in (5,12)，得到信息来源代码的具体描述：5-年度报告，12-招股章程。

### InvObjectsCla (投资对象分类)

投资对象分类(InvObjectsCla)与(CT_SystemConst)表中的DM字段关联，令LB = 1596，得到投资对象分类的具体描述：1-对子公司的投资，2-对联营企业的投资，3-对合营企业的投资，4-其他。

### HoldingWay (持有方式)

持有方式(HoldingWay)与(CT_SystemConst)表中的DM字段关联，令LB = 1904，得到持有方式的具体描述：1-直接持有，2-间接持有。

## SQL示例

```sql
-- 查询 港股长期股权投资明细表 数据
SELECT *
FROM hk_longterminvdet
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
