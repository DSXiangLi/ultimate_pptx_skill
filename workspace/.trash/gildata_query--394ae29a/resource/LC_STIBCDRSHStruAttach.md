# LC_STIBCDRSHStruAttach

**中文名**: 科创板CDR公司份额结构附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCDRSHStruAttach` |
| MySQL表名 | `lc_stibcdrshstruattach` |
| 中文名 | 科创板CDR公司份额结构附表 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.内容说明：收入CDR上市公司股本结构历史变动原因明细及股本变动说明
2.数据范围：2020年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID(RID)：与“科创板CDR公司份额结构（LC_LC_STIBCDRSHStru）”的“ID”关联使用。 |
| 3 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)：股本变动原因-1 |
| 4 | `ChangeTypeDetail` | 股本变动原因明细 | number(10) | ✗ | 100.0% | 股本变动原因明细(ChangeTypeDetail)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 5 | `ChangeReason` | 股本变动说明 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID(RID)：与“科创板CDR公司份额结构（LC_LC_STIBCDRSHStru）”的“ID”关联使用。

### InfoType (信息类别)

信息类别(InfoType)：股本变动原因-1

### ChangeTypeDetail (股本变动原因明细)

股本变动原因明细(ChangeTypeDetail)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM IN (8,35,49,51,52,53,54,55,56,57,58,59,60,79,84,82,80,89,90,105)，得到股本变动原因明细的具体描述：8-送转股，35-股份回购，49-股权转让，51-其他，52-CDR发行，53-CDR上市，54-CDR增发，55-CDR增发上市，56-CDR配股除权，57-CDR配股上市，58-CDR超额配售上市，59-优先股转普通股，60-战略配售可出借股份变动，79-配股限售流通，80-股权激励限售流通，82-发行前股份限售流通，84-股权激励方案实施，89-延长限售锁定期，90-延长限售锁定期流通，105-高管股份变动。

## SQL示例

```sql
-- 查询 科创板CDR公司份额结构附表 数据
SELECT *
FROM lc_stibcdrshstruattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
