# DZ_ConsultingPlatform

**中文名**: 上市公司咨询互动平台

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_ConsultingPlatform` |
| MySQL表名 | `dz_consultingplatform` |
| 中文名 | 上市公司咨询互动平台 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司公告资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：主要记录上市公司的投资者与上市公司董秘互动问答、传闻求证等内容,包括咨询日期,问题情况,问题回复,回复日期等内容。
2.数据范围：2018年1月起至今。
3.信息来源：上交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `InfoType` | 咨询互动类型 | number(10) | ✗ | 100.0% | 咨询互动类型(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2104，得到咨询互动... |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `Questioner` | 提问人 | varchar2(100) | ✓ | 99.99% |  |
| 6 | `ConsultationDate` | 咨询日期 | date | ✓ | 100.0% |  |
| 7 | `ProblemStatement` | 问题情况 | varchar2(2000) | ✓ | 100.0% |  |
| 8 | `ProblemReply` | 问题回复 | clob | ✓ | 100.0% |  |
| 9 | `ReplyDate` | 回复日期 | date | ✓ | 100.0% |  |
| 10 | `SecuCode` | 股票代码 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `SecuAbbr` | 股票简称 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `TrueAndFalse` | 传闻是否属实 | number(10) | ✓ | 0.06% | 传闻是否属实(TrueAndFalse)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InfoType (咨询互动类型)

咨询互动类型(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2104，得到咨询互动类型的具体描述：1-咨询问答，2-传闻求证。

### TrueAndFalse (传闻是否属实)

传闻是否属实(TrueAndFalse)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到传闻是否属实的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 上市公司咨询互动平台 数据
SELECT *
FROM dz_consultingplatform
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
