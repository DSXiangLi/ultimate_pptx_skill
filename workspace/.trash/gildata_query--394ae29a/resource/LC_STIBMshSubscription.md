# LC_STIBMshSubscription

**中文名**: 科创板配股大股东认配状况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBMshSubscription` |
| MySQL表名 | `lc_stibmshsubscription` |
| 中文名 | 科创板配股大股东认配状况 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1、内容说明：收录科创板配股实施过程中大股东的认配状况，如全额实物认配、部分现金认配等内容。
2、数据范围：2019年至今
3、信息来源：配股结果公告、配股上市公告书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 0.0% | RID（RID）：与科创板配股(LC_STIBSharePlacement)的ID字段关联。 |
| 3 | `SHSN` | 股东序号 | number(10) | ✓ | 0.0% |  |
| 4 | `SHName` | 股东名称 | varchar2(120) | ✓ | 0.0% |  |
| 5 | `SHAttribute` | 股东所属性质 | number(10) | ✓ | 0.0% | 股东所属性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股... |
| 6 | `SHID` | 股东ID | number(10) | ✓ | 0.0% | 股东ID（GDID）：当股东所属性质（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中... |
| 7 | `SubscriptionWay` | 认配方式 | number(10) | ✓ |  | 认配方式(SubscriptionWay)与(CT_SystemConst)表中的DM字段关联，令LB = 1114，得... |
| 8 | `OughtShares` | 应配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 9 | `ActualShares` | 实配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID（RID）：与科创板配股(LC_STIBSharePlacement)的ID字段关联。

### SHAttribute (股东所属性质)

股东所属性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHID (股东ID)

股东ID（GDID）：当股东所属性质（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东所属性质（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

### SubscriptionWay (认配方式)

认配方式(SubscriptionWay)与(CT_SystemConst)表中的DM字段关联，令LB = 1114，得到认配方式的具体描述：1-全额放弃，2-全额认配—现金，3-全额认配—实物，4-全额认配—现金、实物，5-部分认配—现金，6-部分认配—实物，7-部分认配—现金、实物，8-部分定向转让，9-全额定向转让，10-接受定向转让，11-部分转配，12-全额转配。

## SQL示例

```sql
-- 查询 科创板配股大股东认配状况 数据
SELECT *
FROM lc_stibmshsubscription
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
