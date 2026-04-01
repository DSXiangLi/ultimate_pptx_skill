# HK_FundRelationship

**中文名**: 香港基金代码关联

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundRelationship` |
| MySQL表名 | `hk_fundrelationship` |
| 中文名 | 香港基金代码关联 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1. 本表收录了香港互认基金和香港ETF，同一基金的关联代码等信息。
2. 历史数据：2015年起-至今。
3. 数据来源：基金公司官网等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `CodeDefine` | 代码关联方式 | number(10) | ✗ | 100.0% | 代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 1350 AND ... |
| 4 | `RelatedInnerCode` | 关联代码内部编码 | number(10) | ✗ | 100.0% | 关联代码内部编码（RelatedInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（I... |
| 5 | `StartDate` | 启用日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 终止日期 | date | ✓ | 12.01% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 8 | `Remarks` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### CodeDefine (代码关联方式)

代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 1350 AND DM IN (21,35,37,79,80)，得到代码关联方式的具体描述：21-同一基金分级关联，35-港股双币双股代码关联，37-同一基金货币关系关联，79-同一基金对冲与否关联，80-同一基金分红与否关联。

### RelatedInnerCode (关联代码内部编码)

关联代码内部编码（RelatedInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 香港基金代码关联 数据
SELECT *
FROM hk_fundrelationship
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
