# LC_SpecialTradeAtta

**中文名**: 证券特别处理附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SpecialTradeAtta` |
| MySQL表名 | `lc_specialtradeatta` |
| 中文名 | 证券特别处理附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 6 |
| 版本 | 1 |

## 表描述

1.内容说明：本表为“证券特别处理”LC_SpecialTrade”的衍生表，具体收录证券被特别处理(或撤销)的原因。
2.数据范围：1998年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“证券特别处理 LC_SpecialTrade”的【ID】字段关联，取到对应的证券被特别处理(或撤销)的其他数... |
| 3 | `SpecialCause` | 特别处理原因 | number(10) | ✗ | 100.0% | 特别处理原因(SpecialCause)与(CT_SystemConst)表中的DM字段关联，令LB = 2324，得到... |
| 4 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 5 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 6 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“证券特别处理 LC_SpecialTrade”的【ID】字段关联，取到对应的证券被特别处理(或撤销)的其他数据，如涉及的日期、特别处理后的证券简称等。

### SpecialCause (特别处理原因)

特别处理原因(SpecialCause)与(CT_SystemConst)表中的DM字段关联，令LB = 2324，得到特别处理原因的具体描述：

## SQL示例

```sql
-- 查询 证券特别处理附表 数据
SELECT *
FROM lc_specialtradeatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
