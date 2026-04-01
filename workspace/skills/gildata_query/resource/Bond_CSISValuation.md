# Bond_CSISValuation

**中文名**: 中证债券特殊估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CSISValuation` |
| MySQL表名 | `bond_csisvaluation` |
| 中文名 | 中证债券特殊估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中证代理数据库 > 中证估值 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录中证违约债券的特殊品种估值
2.数据范围：2018-12-14至今
3.信息来源：中证指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 【注1】内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValueFullPrice` | 估值全价 | number(18,10) | ✓ | 100.0% |  |
| 5 | `ValueFullPriceSource` | 推荐估值全价依据 | number(10) | ✓ | 37.37% |  |
| 6 | `PessiFullPrice` | 下界估值全价 | number(18,10) | ✓ | 37.37% |  |
| 7 | `PessiFullPriceSource` | 下界估值全价依据 | number(10) | ✓ | 37.37% |  |
| 8 | `OptiFullPrice` | 上界估值全价 | number(18,10) | ✓ | 37.37% |  |
| 9 | `OptiFullPriceSource` | 上界估值全价依据 | number(10) | ✓ | 37.37% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

【注1】内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；或与“优先股概况（PS_Archives）”中的“优先股代码（InnerCode）”关联，得到优先股的基本信息。

## SQL示例

```sql
-- 查询 中证债券特殊估值 数据
SELECT *
FROM bond_csisvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
