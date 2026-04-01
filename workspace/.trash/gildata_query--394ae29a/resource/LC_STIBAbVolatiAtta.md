# LC_STIBAbVolatiAtta

**中文名**: 科创板严重异常波动信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBAbVolatiAtta` |
| MySQL表名 | `lc_stibabvolatiatta` |
| 中文名 | 科创板严重异常波动信息附表 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：收录交易所公布的科创板严重异常波动信息以及成交明细等；本表是附表展示成交明细信息，主表为科创板交易所日公开信息(LC_STIBOpTradInfo)
2.数据范围：证券上市之日-至今
3.信息来源：上海证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 与科创板交易所日公开信息（LC_STIBOpTradInfo）表的ID关联，得到对应异动类型的详细信息。 |
| 3 | `ReportArea` | 统计方式 | number(10) | ✗ | 100.0% | 统计方式(ReportArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式... |
| 4 | `InvestorType` | 投资者类型 | number(10) | ✗ | 100.0% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND D... |
| 5 | `InvestorTypeDes` | 投资者类型描述 | varchar2(20) | ✓ | 100.0% |  |
| 6 | `AccuBuySum` | 累计买入金额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `AccuSaleSum` | 累计卖出金额(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `BuyingRatio` | 买入占比(%) | number(7,4) | ✓ | 100.0% |  |
| 9 | `SellingRatio` | 卖出占比(%) | number(7,4) | ✓ | 100.0% |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

与科创板交易所日公开信息（LC_STIBOpTradInfo）表的ID关联，得到对应异动类型的详细信息。

### ReportArea (统计方式)

统计方式(ReportArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式的具体描述：10-买卖金额，11-买入金额，13-卖出金额。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=2127 AND DM IN (1,4,100,101)，得到投资者类型的具体描述：1-自然人，4-机构，100-中小投资者，101-其他自然人。

## SQL示例

```sql
-- 查询 科创板严重异常波动信息附表 数据
SELECT *
FROM lc_stibabvolatiatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
