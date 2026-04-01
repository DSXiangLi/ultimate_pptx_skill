# LC_NewsAbstract

**中文名**: 公司动态摘要

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_NewsAbstract` |
| MySQL表名 | `lc_newsabstract` |
| 中文名 | 公司动态摘要 |
| 路径 | 聚源新版数据库 > 产品代理 > 新闻代理数据库 > A股资讯 |
| 更新频率 | 滚动更新 |
| 字段数量 | 12 |
| 版本 | 1.01 |

## 表描述

1.该表主要覆盖各主流媒体发布的上市公司相关新闻资讯。
2.数据范围：2001-至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 相关公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `Media` | 媒体出处 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `MediaCode` | 媒体出处代码 | number(10) | ✓ | 100.0% | 媒体出处代码(MediaCode)与(NI_NewsConst)表中的DM字段关联，令LB = 4，得到媒体出处代码的具... |
| 6 | `Writer` | 撰写机构 | varchar2(100) | ✓ | 2.81% |  |
| 7 | `Category` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1049，得到信息类别的具... |
| 8 | `InfoTitle` | 标题 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `Abstract` | 信息内容摘要 | clob | ✓ | 0.12% |  |
| 10 | `RecordDate` | 记录录入时间 | date | ✓ | 76.13% |  |
| 11 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MediaCode (媒体出处代码)

媒体出处代码(MediaCode)与(NI_NewsConst)表中的DM字段关联，令LB = 4，得到媒体出处代码的具体描述。

### Category (信息类别)

信息类别(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1049，得到信息类别的具体描述：901-公司公告，902-公司研究，903-公司动态，908-回购动态。

## SQL示例

```sql
-- 查询 公司动态摘要 数据
SELECT *
FROM lc_newsabstract
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
