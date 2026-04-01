# LC_ShareTrustee

**中文名**: 股东股权托管

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ShareTrustee` |
| MySQL表名 | `lc_sharetrustee` |
| 中文名 | 股东股权托管 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 停止更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.收录公司股东股权委托第三方经营方面的明细资料。包括股权授权方、股权授权方所持股数、接受股权授权方、托管涉及股数以及股权授权期限起始日和截止日等内容。
2.数据范围：1999-12-24 至2014-11-04
3.信息来源：董事会公告、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.67% |  |
| 5 | `Authorizer` | 股权授权方 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `AuthorizerHoldSum` | 股权授权方所持股数(股) | number(16,0) | ✓ | 0.0% |  |
| 7 | `AuthorizedReceiver` | 接受股权授权方 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `InvolvedTrustSum` | 托管涉及股数(股) | number(16,0) | ✓ | 100.0% |  |
| 9 | `PCTOfAuthorizer` | 占股权授权方持股数比例 | number(9,6) | ✓ | 100.0% |  |
| 10 | `PCTOfFullShares` | 占总股本比例 | number(9,6) | ✓ | 100.0% |  |
| 11 | `StartDate` | 股权授权期限起始日 | date | ✓ | 41.72% |  |
| 12 | `EndDate` | 股权授权期限截止日 | date | ✓ | 29.8% |  |
| 13 | `TrustStatement` | 事项描述与进展说明 | clob | ✓ | 46.69% |  |
| 14 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 股东股权托管 数据
SELECT *
FROM lc_sharetrustee
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
