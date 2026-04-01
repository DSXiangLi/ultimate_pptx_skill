# Index_ReleaseChanInfo

**中文名**: 主要发布渠道指数信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_ReleaseChanInfo` |
| MySQL表名 | `index_releasechaninfo` |
| 中文名 | 主要发布渠道指数信息 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1.01 |

## 表描述

1.收录市场上主要指数发布渠道发布的指数的信息，包括证券代码、证券简称、发布状态等。
2.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所、中央国债登记结算有限责任公司、申银万国研究所等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PubChannelCode` | 发布渠道代码 | number(10) | ✗ | 100.0% | 发布渠道代码（PubChannelCode）：与机构基本资料（LC_InstiArchive）中的企业编号（Compan... |
| 3 | `PubChannelName` | 发布渠道名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `IndexCode` | 指数内部代码 | number(10) | ✗ | 100.0% | 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 5 | `SecuCode` | 证券代码 | varchar2(50) | ✗ | 100.0% | 发布渠道名称为“恒生指数有限公司”的恒生指数，证券代码优先选用彭博代码，如无彭博代码则为路孚特代码。 |
| 6 | `SecuAbbr` | 证券简称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `PubState` | 发布状态 | number(10) | ✗ | 100.0% | 发布状态（PubState）：1-正常发布，0-停止发布，5-其他. |
| 8 | `IfOfficialCode` | 是否官方代码 | number(10) | ✓ | 100.0% | 是否官方代码（IfOfficialCode）：1-是官方代码，2-不是官方代码 |
| 9 | `BeginDate` | 发布起始日期 | date | ✓ | 53.05% |  |
| 10 | `EndDate` | 发布截止日期 | date | ✓ | 6.16% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PubChannelCode (发布渠道代码)

发布渠道代码（PubChannelCode）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联。

### IndexCode (指数内部代码)

指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### SecuCode (证券代码)

发布渠道名称为“恒生指数有限公司”的恒生指数，证券代码优先选用彭博代码，如无彭博代码则为路孚特代码。

### PubState (发布状态)

发布状态（PubState）：1-正常发布，0-停止发布，5-其他.

### IfOfficialCode (是否官方代码)

是否官方代码（IfOfficialCode）：1-是官方代码，2-不是官方代码

## SQL示例

```sql
-- 查询 主要发布渠道指数信息 数据
SELECT *
FROM index_releasechaninfo
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
