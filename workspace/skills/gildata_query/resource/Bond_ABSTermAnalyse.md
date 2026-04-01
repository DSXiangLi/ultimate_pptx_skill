# Bond_ABSTermAnalyse

**中文名**: 资产支持证券期限分析表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ABSTermAnalyse` |
| MySQL表名 | `bond_abstermanalyse` |
| 中文名 | 资产支持证券期限分析表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 资产支持证券信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：资产证券支持证券的期限敏感性分析情况,包括早偿率、违约率的影响因素等影响ABS的加权平均期限及预计到期日的情况。
2.数据范围：2015年开始至今
3.信息来源：中债登、货币网、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InfluIndexO` | 影响指标一 | number(10) | ✓ | 87.2% | 影响指标一(InfluIndexO)与(Bond_SystemConst)表中的DM字段关联，令LB = 110，得到影... |
| 4 | `IndexValueO` | 指标值一 | number(9,6) | ✓ | 87.2% |  |
| 5 | `InfluIndexT` | 影响指标二 | number(10) | ✓ | 31.18% | 影响指标二(InfluIndexT)与(Bond_SystemConst)表中的DM字段关联，令LB = 111，得到影... |
| 6 | `IndexValueT` | 指标值二 | number(9,6) | ✓ | 31.18% |  |
| 7 | `WeightedAvgLife` | 加权平均期限(年) | number(9,6) | ✓ | 99.9% |  |
| 8 | `PrincipalBeginDate` | 本金起付日 | date | ✓ | 6.14% |  |
| 9 | `PrincipalEndDate` | 本金止付日 | date | ✓ | 11.9% |  |
| 10 | `EarlyReCycle` | 提前回收周期 | number(10) | ✓ | 7.49% | 提前回收周期(EarlyReCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 1241 AN... |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### InfluIndexO (影响指标一)

影响指标一(InfluIndexO)与(Bond_SystemConst)表中的DM字段关联，令LB = 110，得到影响指标一的具体描述：1-提前还款率/提前回收率/早偿率，2-滞后回收率。

### InfluIndexT (影响指标二)

影响指标二(InfluIndexT)与(Bond_SystemConst)表中的DM字段关联，令LB = 111，得到影响指标二的具体描述：1-违约率。

### EarlyReCycle (提前回收周期)

提前回收周期(EarlyReCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 1241 AND DM IN (1,2,3)，得到提前回收周期的具体描述：1-三个月，2-六个月，3-一年。

## SQL示例

```sql
-- 查询 资产支持证券期限分析表 数据
SELECT *
FROM bond_abstermanalyse
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
