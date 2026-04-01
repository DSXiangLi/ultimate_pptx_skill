# MF_BondCreditGrading

**中文名**: 公募基金债券投资信用评级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BondCreditGrading` |
| MySQL表名 | `mf_bondcreditgrading` |
| 中文名 | 公募基金债券投资信用评级 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 半年更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金年报、半年报公布债券投资信用评级信息，包括债券投资信用等级等数据。
2.历史数据：2013年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `NV` | 基金资产净值(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 9 | `TCRType` | 评级类别 | number(10) | ✓ | 100.0% | 评级类别(TCRType)与(CT_SystemConst)表中的DM字段关联，令LB = 1779 AND DM IN... |
| 10 | `BondCreditRating` | 债券信用等级 | varchar2(50) | ✓ | 100.0% |  |
| 11 | `MarketValue` | 市值(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### TCRType (评级类别)

评级类别(TCRType)与(CT_SystemConst)表中的DM字段关联，令LB = 1779 AND DM IN(1,2,47,48,49,50)，得到评级类别的具体描述：1-债券长期信用评级，2-债券短期信用评级，47-资产支持证券短期信用评级，48-同业存单短期信用评级，49-资产支持证券长期信用评级，50-同业存单长期信用评级。

## SQL示例

```sql
-- 查询 公募基金债券投资信用评级 数据
SELECT *
FROM mf_bondcreditgrading
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
