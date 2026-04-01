# Fut_DeliveryDec

**中文名**: 期货交割意向申报

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_DeliveryDec` |
| MySQL表名 | `fut_deliverydec` |
| 中文名 | 期货交割意向申报 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录期货合约的交割意向申报数据。
2.数据范围：2013年至今
3.信息来源：中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与期货合约（Fut_ContractMain）表中的合约内部编码（C... |
| 4 | `MemberCompanyCode` | 会员企业编号 | number(10) | ✗ | 100.0% | 会员内部编码(MemberInnerCode)与(LC_InstiArchive)表中的CompanyCode字段关联，... |
| 5 | `SettlementMemberCode` | 结算会员号 | varchar2(20) | ✓ | 100.0% |  |
| 6 | `SettlementMemberName` | 结算会员名称 | varchar2(200) | ✓ | 100.0% |  |
| 7 | `DecSellDeliveryVolume` | 申报卖方交割量 | number(19,4) | ✓ | 100.0% |  |
| 8 | `DecBuyDeliveryVolume` | 申报买方交割量 | number(19,4) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与期货合约（Fut_ContractMain）表中的合约内部编码（ContractInnerCode）字段进行关联，得到该期货合约的基础信息。

### MemberCompanyCode (会员企业编号)

会员内部编码(MemberInnerCode)与(LC_InstiArchive)表中的CompanyCode字段关联，令IfExisted = 1，得到会员内部编码的具体描述。

## SQL示例

```sql
-- 查询 期货交割意向申报 数据
SELECT *
FROM fut_deliverydec
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
