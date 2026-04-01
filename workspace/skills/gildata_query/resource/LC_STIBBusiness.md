# LC_STIBBusiness

**中文名**: 科创板公司经营范围

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBBusiness` |
| MySQL表名 | `lc_stibbusiness` |
| 中文名 | 科创板公司经营范围 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1.01 |

## 表描述

1.内容说明：科创板公司的经营范围（包括主营和兼营）、主要产品业务情况。
2.数据范围：2019年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `MainBusiness` | 业务简介 | varchar2(2000) | ✓ | 100.0% |  |
| 5 | `BusinessMajor` | 经营范围-主营 | clob | ✓ | 14.78% |  |
| 6 | `BusinessMinor` | 经营范围-兼营 | clob | ✓ | 26.02% |  |
| 7 | `MainName` | 主要产品业务 | clob | ✓ | 8.89% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 科创板公司经营范围 数据
SELECT *
FROM lc_stibbusiness
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
