# HK_HighSHConcList

**中文名**: 港股股权高度集中名单

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_HighSHConcList` |
| MySQL表名 | `hk_highshconclist` |
| 中文名 | 港股股权高度集中名单 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

内容说明：本表记录香港证监会公布的股权集中于少数股东的上市公司名单。
数据范围：历史至今
信息来源：香港证监会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `SHName` | 股东名称 | varchar2(150) | ✗ | 100.0% |  |
| 6 | `SHID` | 股东编码 | number(10) | ✓ | 21.19% |  |
| 7 | `SHAttribute` | 股东属性 | number(10) | ✓ | 100.0% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到股东属性的... |
| 8 | `HoldSum` | 所持股份数量 | number(19,4) | ✓ | 100.0% |  |
| 9 | `RatioInTotalShares` | 占已发行股份总额比例 | number(19,4) | ✓ | 100.0% |  |
| 10 | `Remark` | 备注 | varchar2(1000) | ✓ | 50.74% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

## SQL示例

```sql
-- 查询 港股股权高度集中名单 数据
SELECT *
FROM hk_highshconclist
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
