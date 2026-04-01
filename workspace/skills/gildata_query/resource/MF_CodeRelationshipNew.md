# MF_CodeRelationshipNew

**中文名**: 公募基金代码关联(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CodeRelationshipNew` |
| MySQL表名 | `mf_coderelationshipnew` |
| 中文名 | 公募基金代码关联(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.本表收录了聚源整理的分级基金的关联代码、复制型基金的关联代码、封转开基金代码对应关系、基金与其收益线对应关系等信息，其中分级关系涉及的代码关联方式 in (21,22,37,76)。
2.历史数据：2001年9月起-至今。
3.信息来源：基金公司官网披露的产品说明书、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `CodeDefine` | 代码关联方式 | number(10) | ✗ | 100.0% | 代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM... |
| 4 | `SndCodeDefine` | 二级关联方式 | number(10) | ✓ | 77.64% | 二级关联方式(SndCodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND... |
| 5 | `RelatedInnerCode` | 关联代码内部编码 | number(10) | ✓ | 100.0% | 关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 6 | `StartDate` | 启用日期 | date | ✓ | 100.0% |  |
| 7 | `EndDate` | 终止日期 | date | ✓ | 15.18% |  |
| 8 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 9 | `Remarks` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |
| 12 | `TrdCodeDefine` | 三级关联方式 | number(10) | ✓ | 0.0% |  |
| 13 | `RelatedCode` | 对应代码 | varchar2(10) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等，一般为常规AC份额类基金的主代码和分级基金的母代码，详见Q&A

### CodeDefine (代码关联方式)

代码关联方式(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM IN(21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,37 ,76)，得到代码关联方式的具体描述：21-同一基金分级关联，22-母子基金分级关联，23-复制型基金关联，24-联接基金关联，25-封转开基金对应，26-同一基金保本期关联，27-基金与收益线对应，28-开转封基金对应，29-开放式基金转型对应，37-同一基金货币关系关联，76-互认基金关联。

### SndCodeDefine (二级关联方式)

二级关联方式(SndCodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB=1350 AND DM IN (2101 ,2102 ,2106)，得到二级关联方式的具体描述：2101-同一基金杠杆分级关联，2102-同一基金母子子代码关联，2106-同一基金按费用不同关联。

### RelatedInnerCode (关联代码内部编码)

关联代码内部编码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得基金的交易代码、简称等。当RelatedInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等，一般为常规AC份额类基金的下属代码和分级基金的子代码，详见Q&A

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金代码关联(新) 数据
SELECT *
FROM mf_coderelationshipnew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
