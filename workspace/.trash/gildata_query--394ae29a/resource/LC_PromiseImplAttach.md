# LC_PromiseImplAttach

**中文名**: 股东承诺实施表附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PromiseImplAttach` |
| MySQL表名 | `lc_promiseimplattach` |
| 中文名 | 股东承诺实施表附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.内容说明：收录股东承诺实施主表中各个股东的股东性质、股东ID的信息。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 股东承诺实施ID | number(19) | ✗ | 100.0% |  |
| 3 | `SHName` | 股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `SHAttribute` | 股东属性 | number(10) | ✓ | 99.92% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属... |
| 5 | `SHID` | 股东ID | number(10) | ✓ | 45.07% | 股东ID（SHID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHID (股东ID)

股东ID（SHID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。 

## SQL示例

```sql
-- 查询 股东承诺实施表附表 数据
SELECT *
FROM lc_promiseimplattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
