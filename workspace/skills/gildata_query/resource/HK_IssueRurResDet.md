# HK_IssueRurResDet

**中文名**: 港股发行申购结果详细记录

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IssueRurResDet` |
| MySQL表名 | `hk_issuerurresdet` |
| 中文名 | 港股发行申购结果详细记录 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.内容说明：记录新上市个股每个新股申购人申购到的新股数据，方便新股申购人能够及时获取到获配发信息。
2.数据范围：2019-10-09至今；
3.信息来源：港交所披露数值

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `ApplyType` | 申请类型 | number(10) | ✗ | 100.0% | 申请类型(ApplyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2283，得到申请类型的... |
| 6 | `IdentiNumber` | 证件号码 | varchar2(100) | ✗ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 8 | `AllottedShares` | 获配发股数 | number(10) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### ApplyType (申请类型)

申请类型(ApplyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2283，得到申请类型的具体描述：10-白表，20-黄表，30-黄表-电子认购指示，40-蓝表，50-绿表，60-粉表，70-其他。

## SQL示例

```sql
-- 查询 港股发行申购结果详细记录 数据
SELECT *
FROM hk_issuerurresdet
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
