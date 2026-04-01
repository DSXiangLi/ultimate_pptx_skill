# LC_STIBAICRelAttach

**中文名**: 科创板一致行动人关系附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBAICRelAttach` |
| MySQL表名 | `lc_stibaicrelattach` |
| 中文名 | 科创板一致行动人关系附表 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.内容说明: 收录根据科创板上市公司在招投说明书、定期报告及临时公告中披露的一致行动人的每个人单独的详细信息。
2.数据范围：2019年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `ActInConcertName` | 一致行动人名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `ActInConcertNature` | 一致行动人性质 | number(10) | ✓ | 100.0% | 一致行动人性质(ActInConcertNature)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 5 | `ActInConcertID` | 一致行动人ID | number(10) | ✓ | 61.84% | 一致行动人ID（ActInConcertID）：当一致行动人性质（ActInConcertNature）=2时，与机构基... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ActInConcertNature (一致行动人性质)

一致行动人性质(ActInConcertNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到一致行动人性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### ActInConcertID (一致行动人ID)

一致行动人ID（ActInConcertID）：当一致行动人性质（ActInConcertNature）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；一致行动人性质（ActInConcertNature）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

## SQL示例

```sql
-- 查询 科创板一致行动人关系附表 数据
SELECT *
FROM lc_stibaicrelattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
