# Bond_CBVARTypeOne

**中文名**: 中债单券VAR类型一

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBVARTypeOne` |
| MySQL表名 | `bond_cbvartypeone` |
| 中文名 | 中债单券VAR类型一 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债估值中心发布的中债单券VaR和CVaR值，持有期=1天，置信水平=0.95
2.数据范围：2018年8月30日至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `HoldingPeriod` | 持有期 | number(9,6) | ✗ | 100.0% |  |
| 5 | `ConfidenceLevel` | 置信水平 | number(9,6) | ✗ | 100.0% |  |
| 6 | `VAR` | VaR值 | number(19,8) | ✓ | 100.0% |  |
| 7 | `CVAR` | CVaR值 | number(19,8) | ✓ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

## SQL示例

```sql
-- 查询 中债单券VAR类型一 数据
SELECT *
FROM bond_cbvartypeone
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
