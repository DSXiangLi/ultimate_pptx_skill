# Bond_FCLWeightAvgRate

**中文名**: 外币加权平均价

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_FCLWeightAvgRate` |
| MySQL表名 | `bond_fclweightavgrate` |
| 中文名 | 外币加权平均价 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：收录对外新公布的上海外汇交易中心外币拆借加权平均价
2.数据范围：2020年12月25日至今
3.信息来源：外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingTime` | 交易时间 | varchar2(8) | ✗ | 100.0% |  |
| 4 | `BENCHMARKRATE_TYPE` | 基准利率类型 | number(10) | ✗ | 100.0% | 基准利率类型(BENCHMARKRATE_TYPE)与(CT_SystemConst)表中的DM字段关联，令LB=239... |
| 5 | `BENCHMARKRATE_DESC` | 基准利率描述 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `OfferedMoney` | 拆借币种类型 | number(10) | ✗ | 100.0% | 拆借币种类型(OfferedMoney)与(CT_SystemConst)表中的DM字段关联，令LB=1548 and ... |
| 7 | `OfferedMoneyDesc` | 拆借币种描述 | varchar2(8) | ✓ | 100.0% |  |
| 8 | `MaturityType` | 期限类型 | number(10) | ✗ | 100.0% | 期限类型(MaturityType)与(CT_SystemConst)表中的DM字段关联，令LB =1555 and D... |
| 9 | `MaturityDesc` | 期限描述 | varchar2(8) | ✓ | 100.0% | 期限描述(MaturityDesc)：展示外汇交易中心披露的原始期限。2025-08-30外汇交易中心版本切换后，期限描... |
| 10 | `WeightedAverageRate` | 加权平均利率 | number(18,10) | ✓ | 77.33% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BENCHMARKRATE_TYPE (基准利率类型)

基准利率类型(BENCHMARKRATE_TYPE)与(CT_SystemConst)表中的DM字段关联，令LB=2391 and DM in (1,2)，得到基准利率类型的具体描述：1-境内银银间美元拆借加权成交利率，2-银行间美元拆借加权成交利率。

### OfferedMoney (拆借币种类型)

拆借币种类型(OfferedMoney)与(CT_SystemConst)表中的DM字段关联，令LB=1548 and DM = 1000，得到拆借币种类型的具体描述：1000-美元。

### MaturityType (期限类型)

期限类型(MaturityType)与(CT_SystemConst)表中的DM字段关联，令LB =1555 and DM in(1,5,7,9,12,20)，得到期限类型的具体描述：1-ON，5-2W，7-1M，9-3M，12-6M，20-1W。

### MaturityDesc (期限描述)

期限描述(MaturityDesc)：展示外汇交易中心披露的原始期限。2025-08-30外汇交易中心版本切换后，期限描述规则发生变化，如1M，变化为M1，即字母在前面，数字在后面，如ON，变化为1。

## SQL示例

```sql
-- 查询 外币加权平均价 数据
SELECT *
FROM bond_fclweightavgrate
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
