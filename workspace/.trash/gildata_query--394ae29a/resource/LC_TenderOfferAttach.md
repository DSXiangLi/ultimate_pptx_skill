# LC_TenderOfferAttach

**中文名**: 重大事项要约收购附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_TenderOfferAttach` |
| MySQL表名 | `lc_tenderofferattach` |
| 中文名 | 重大事项要约收购附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定期更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

本表存放要同一事件有多个要约收购人的具体清单，与主表“重大事项要约收购(LC_TenderOffer)”一起使用，包括要约收购人的名字、编码、与上市公司关系

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID（RID）：与主表“重大事项要约收购(LC_TenderOffer)”的“ID”字段关联，取到要约收购其他数据。 |
| 3 | `ObjectName` | 交易对象名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `ObjectNature` | 交易对象性质 | number(10) | ✓ | 100.0% | 交易对象性质(ObjectNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AN... |
| 5 | `ObjectCode` | 交易对象编码 | number(10) | ✓ | 90.2% | 交易对象编码(ObjectCode)：当”交易对象性质(ObjectNature)“字段=2，则”交易对象编码(Obje... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID（RID）：与主表“重大事项要约收购(LC_TenderOffer)”的“ID”字段关联，取到要约收购其他数据。

### ObjectNature (交易对象性质)

交易对象性质(ObjectNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM in (1,2,99) ，得到交易对象性质的具体描述：1-自然人，2-企业，99-其他。

### ObjectCode (交易对象编码)

交易对象编码(ObjectCode)：当”交易对象性质(ObjectNature)“字段=2，则”交易对象编码(ObjectCode)“关联”机构基本资料(LC_InstiArchive)“的”CompanyCode  企业编号 “关联，取的相关企业基本资料；其他类别暂无编码。

## SQL示例

```sql
-- 查询 重大事项要约收购附表 数据
SELECT *
FROM lc_tenderofferattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
