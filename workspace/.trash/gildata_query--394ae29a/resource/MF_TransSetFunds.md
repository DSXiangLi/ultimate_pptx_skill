# MF_TransSetFunds

**中文名**: 证券市场交易结算金

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_TransSetFunds` |
| MySQL表名 | `mf_transsetfunds` |
| 中文名 | 证券市场交易结算金 |
| 路径 | 聚源新版数据库 > 市场统计数据库 > 证券市场统计 |
| 更新频率 | 停止更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.证券市场交易结算资金余额及变动情况，包括结算金期末余额、期末日平均数、银证转账增加额、银证转账减少额、银证转账净变动额等指标。
2.数据范围：2012.6-2017.6
3.信息来源：中国证券投资者保护基金有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `DataType` | 资金类型 | number(10) | ✗ | 100.0% | 资金类型(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1861，得到资金类型的具... |
| 4 | `StatPeriod` | 数据统计期间 | number(10) | ✗ | 100.0% | 数据统计期间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND ... |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `StartDate` | 起始日期 | date | ✗ | 100.0% |  |
| 7 | `EndDate` | 终止日期 | date | ✗ | 100.0% |  |
| 8 | `TSFClosingBalance` | 结算金期末余额(亿元) | number(18,4) | ✗ | 100.0% |  |
| 9 | `TSFAverageAmount` | 结算金期末日平均数(亿元) | number(18,4) | ✗ | 100.0% |  |
| 10 | `TSFInBSTransferInc` | 结算金银证转账增加额(亿元) | number(18,4) | ✗ | 100.0% |  |
| 11 | `TSFInBSTransferDec` | 结算金银证转账减少额(亿元) | number(18,4) | ✗ | 100.0% |  |
| 12 | `TSFInBSTransferNet` | 结算金银证转账净变动额(亿元) | number(18,4) | ✗ | 100.0% |  |
| 13 | `Remark` | 备注说明 | varchar2(200) | ✓ | 36.8% |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### DataType (资金类型)

资金类型(DataType)与(CT_SystemConst)表中的DM字段关联，令LB = 1861，得到资金类型的具体描述：1-证券交易结算资金，2-股票期权保证金，3-融资融券担保资金。

### StatPeriod (数据统计期间)

数据统计期间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (1,5,6,9)，得到数据统计期间的具体描述：1-月份，5-日，6-周，9-年度。

## SQL示例

```sql
-- 查询 证券市场交易结算金 数据
SELECT *
FROM mf_transsetfunds
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
