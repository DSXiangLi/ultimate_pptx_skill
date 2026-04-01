# MF_Share

**中文名**: 公募基金份额

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_Share` |
| MySQL表名 | `mf_share` |
| 中文名 | 公募基金份额 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

本表记录公募基金的份额信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `Shares` | 基金份额(份) | number(18,4) | ✓ | 100.0% |  |
| 8 | `ExchangeShares` | 场内份额(份) | number(18,4) | ✓ | 72.77% |  |
| 9 | `ExRestrictedShares` | 场内限售份额(份) | number(18,4) | ✓ | 100.0% |  |
| 10 | `IfCombine` | 是否合并披露 | number(10) | ✓ | 100.0% | 是否合并披露(IfCombine)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM I... |
| 11 | `ChangeReason` | 份额变动原因 | number(10) | ✓ | 100.0% | 份额变动原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB=2585，得到份额... |
| 12 | `IfNew` | 是否最新 | number(10) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfCombine (是否合并披露)

是否合并披露(IfCombine)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1, 2)，得到是否合并披露的具体描述：1-是，2-否。

### ChangeReason (份额变动原因)

份额变动原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB=2585，得到份额变动原因的具体描述：1-日常申购赎回，2-基金成立，3-到期清算，4-基金上市，5-扩募，6-分级基金拆分折算，7-普通基金拆分折算，8-封转开拆分折算，9-ETF拆分折算，10-份额合并，11-其他，101-限售解禁，102-限售延期，103-追加限售。

## SQL示例

```sql
-- 查询 公募基金份额 数据
SELECT *
FROM mf_share
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
