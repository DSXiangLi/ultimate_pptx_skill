# LC_STIBCDRSHStru

**中文名**: 科创板CDR公司份额结构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCDRSHStru` |
| MySQL表名 | `lc_stibcdrshstru` |
| 中文名 | 科创板CDR公司份额结构 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1 |

## 表描述

1.内容说明：以份为单位收录CDR上市公司股本结构历史变动情况说明
2.数据范围：2020年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，限... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `TotalShares` | 总股本(份) | number(16,0) | ✓ | 100.0% |  |
| 7 | `RestrictedShares` | A.有限售条件的流通股份(份)(计算) | number(16,0) | ✓ | 100.0% |  |
| 8 | `NonResiSharesJY` | B.无限售条件流通股份(份)(计算) | number(16,0) | ✓ | 100.0% |  |
| 9 | `RestrictShareP` | C.有限售条件的流通股份(份)(披露) | number(16,0) | ✓ | 100.0% |  |
| 10 | `NonRestrictedShares` | D.无限售条件流通股份(份)(披露) | number(16,0) | ✓ | 100.0% |  |
| 11 | `FloatListed` | a.已上市流通股份(包含高管股)(份) | number(16,0) | ✓ | 100.0% |  |
| 12 | `StategicInvestorShares` | b.战略投资者配售持股(份) | number(16,0) | ✓ | 28.57% |  |
| 13 | `CommonLPShares` | c.一般法人配售持股(份) | number(16,0) | ✓ | 0.0% |  |
| 14 | `RestrictedFloatShares` | d.有限售流通股份(份) | number(16,0) | ✓ | 100.0% |  |
| 15 | `StateHolding` | 1.国家持股(份) | number(16,0) | ✓ | 0.0% |  |
| 16 | `SLegalPersonHolding` | 2.国有法人持股(份) | number(16,0) | ✓ | 28.57% |  |
| 17 | `OtherDCapitalHolding` | 3.其他内资持股(份) | number(16,0) | ✓ | 100.0% |  |
| 18 | `DLegalPersonHolding` | 3.1)境内法人持股(份) | number(16,0) | ✓ | 12.24% |  |
| 19 | `DNaturalPersonHolding` | 3.2)境内自然人持股(份) | number(16,0) | ✓ | 89.8% |  |
| 20 | `ManagementShares` | ##高管股(份) | number(16,0) | ✓ | 0.0% |  |
| 21 | `ForeignHolding` | 4.外资持股(份) | number(16,0) | ✓ | 100.0% |  |
| 22 | `FLegalPersonHolding` | 4.1)境外法人持股(份) | number(16,0) | ✓ | 100.0% |  |
| 23 | `FNaturalPersonHolding` | 4.2)境外自然人持股(份) | number(16,0) | ✓ | 0.0% |  |
| 24 | `OtherRestrictedShares` | 5.其他有限售持股(份) | number(16,0) | ✓ | 0.0% |  |
| 25 | `ChangeReason` | 股本变动原因说明 | varchar2(2000) | ✓ | 77.55% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，限制证券类别（SecuCategory）为41-中国存托凭证，得到上市公司的交易代码、简称等

## SQL示例

```sql
-- 查询 科创板CDR公司份额结构 数据
SELECT *
FROM lc_stibcdrshstru
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
