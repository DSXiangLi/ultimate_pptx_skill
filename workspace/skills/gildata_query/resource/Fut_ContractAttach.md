# Fut_ContractAttach

**中文名**: 期货品种附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_ContractAttach` |
| MySQL表名 | `fut_contractattach` |
| 中文名 | 期货品种附表 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表收录国内期货的品种简介信息，包括品种简介，市场概述和影响因素三个方面的内容。
2.数据范围：1995年至今
3.信息来源：国内期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `VarietyInnerCode` | 品种内部编码 | number(10) | ✗ | 100.0% | 品种内部编码(VarietyInnerCode)：与期货品种表（Fut_FuturesContract）的品种内部编码（... |
| 4 | `VarietyArchives` | 品种概况 | clob | ✓ | 62.07% |  |
| 5 | `MarketOverview` | 市场概述 | clob | ✓ | 49.43% |  |
| 6 | `PriceFactors` | 影响价格因素 | clob | ✓ | 56.32% |  |
| 7 | `InvolvedPlate` | 涉及概念板块 | number(10) | ✓ | 81.03% | 涉及概念板块(InvolvedPlate)与(CT_SystemConst)表中的DM字段关联，令LB = 2317，得... |
| 8 | `Remark` | 备注 | clob | ✓ | 0.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### VarietyInnerCode (品种内部编码)

品种内部编码(VarietyInnerCode)：与期货品种表（Fut_FuturesContract）的品种内部编码（ContractInnerCode） 字段关联，得到该品种的相关信息

### InvolvedPlate (涉及概念板块)

涉及概念板块(InvolvedPlate)与(CT_SystemConst)表中的DM字段关联，令LB = 2317，得到涉及概念板块的具体描述：1-贵金属，2-有色金属，3-煤焦钢矿，4-非金属建材，5-能源，6-化工，7-油脂油料，8-软商品，9-谷物，10-农副产品，11-基本金属，12-农产品，13-能源化工，14-国债期货，15-航运指数，16-股指期货。

## SQL示例

```sql
-- 查询 期货品种附表 数据
SELECT *
FROM fut_contractattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
