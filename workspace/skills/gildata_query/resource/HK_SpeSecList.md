# HK_SpeSecList

**中文名**: 港股特别证券名单表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SpeSecList` |
| MySQL表名 | `hk_speseclist` |
| 中文名 | 港股特别证券名单表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.记录港股市价调节机制（VCM）,收市竞价（CAS）等名单。包含字段有：名单类型、信息发布时间、入选时间、剔除时间等。
2.数据范围：2016-09至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `ListType` | 名单类型 | number(10) | ✗ | 100.0% | 名单类型(ListType)与(CT_SystemConst)表中的DM字段关联，令LB = 1943，得到名单类型的具... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 6 | `OutDate` | 剔除日期 | date | ✓ | 92.97% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 8 | `VCMThreshold` | 市调触发门槛(%) | number(18,2) | ✓ | 0.28% |  |
| 9 | `Mark` | 备注 | varchar2(200) | ✓ | 0.06% |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### ListType (名单类型)

名单类型(ListType)与(CT_SystemConst)表中的DM字段关联，令LB = 1943，得到名单类型的具体描述：1-收市竞价，2-市调机制，3-须缴纳印花税，4-纳入中央结算系统，5-纳入股票期权，6-纳入股票期货。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 港股特别证券名单表 数据
SELECT *
FROM hk_speseclist
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
