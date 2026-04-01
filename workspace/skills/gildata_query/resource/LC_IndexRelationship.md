# LC_IndexRelationship

**中文名**: 指数代码关联

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndexRelationship` |
| MySQL表名 | `lc_indexrelationship` |
| 中文名 | 指数代码关联 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.收录了同一指数在不同的证券发布市场上的代码之间的关联信息。
2.数据源：深圳证券交易所、上海证券交易所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指... |
| 3 | `SecuCode` | 证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 4 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场/主表（SecuMarket）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“L... |
| 5 | `CodeDefine` | 关联方式 | number(10) | ✗ | 100.0% | 关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 2014，得到关联方式... |
| 6 | `Market` | 关联对应证券市场 | number(10) | ✗ | 100.0% | 关联对应证券市场/主表（Market）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“L... |
| 7 | `RelatedInnerCode` | 关联对应内部编码 | number(10) | ✗ | 100.0% | 关联对应内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 8 | `RelatedSecuCode` | 关联对应证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 9 | `CancelDate` | 取消日期 | date | ✓ | 0.04% |  |
| 10 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |
| 13 | `CompanyCode` | 公司代码(无效字段) | number(10) | ✗ | 100.0% |  |
| 14 | `RelatedCompanyCode` | 关联对应公司代码 | number(10) | ✗ | 100.0% |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### SecuMarket (证券市场)

证券市场/主表（SecuMarket）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=201”，得到该字段的具体描述。
当代码关联方式=30（同一指数不同代码关联），这里的描述即为指数所属的市场。83-上海证券交易所，90-深圳证券交易所,84-其他市场，72-香港联交所
当代码关联方式=56（同一指数不同内码关联），这里的描述代指指数所在的主表。83，90，84等均表证券主表（SecuMain），72-表港股证券主表（HK_SecuMain），此处优先用证券主表。

### CodeDefine (关联方式)

关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 2014，得到关联方式的具体描述：1-币种不同，2-分红规则不同，3-分红规则和币种都不同，4-税后分红，5-主指数，6-待偿期限不同，7-分红规则和待偿期限都不同，8-税后分红和待偿期限不同，9-对冲指数，30-转发指数，31-加权方式不同。

### Market (关联对应证券市场)

关联对应证券市场/主表（Market）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=201”，得到该字段的具体描述。
当代码关联方式=30（同一指数不同代码关联），这里的描述即为指数所属的市场。83-上海证券交易所，90-深圳证券交易所,84-其他市场，72-香港联交所
当代码关联方式=56（同一指数不同内码关联），这里的描述代指指数所在的主表。83，90，84等均表证券主表（SecuMain），72-表港股证券主表（HK_SecuMain），此处优先用证券主表。

### RelatedInnerCode (关联对应内部编码)

关联对应内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

## SQL示例

```sql
-- 查询 指数代码关联 数据
SELECT *
FROM lc_indexrelationship
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
