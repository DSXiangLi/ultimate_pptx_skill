# LC_IntangibleAsset

**中文名**: 主营业务与产品_工业产权等无形资产

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IntangibleAsset` |
| MySQL表名 | `lc_intangibleasset` |
| 中文名 | 主营业务与产品_工业产权等无形资产 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.工业产权等无形资产类别、名称、所有权归属、取得或使用方式，项目具体说明。
2.数据范围：2000-12-22至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布时间 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.94% |  |
| 5 | `SN` | 序号 | number(10) | ✓ | 100.0% |  |
| 6 | `Type` | 无形资产类别 | number(10) | ✓ | 100.0% | 无形资产类别(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 1233，得到无形资产类别的具... |
| 7 | `Name` | 无形资产名称 | varchar2(100) | ✓ | 99.82% |  |
| 8 | `Ownership` | 所有权归属 | number(10) | ✓ | 99.99% | 所有权归属(Ownership)与(CT_SystemConst)表中的DM字段关联，令LB = 1229，得到所有权归... |
| 9 | `AcquiringOrUsingWays` | 取得或使用方式 | number(10) | ✓ | 99.99% | 取得或使用方式(AcquiringOrUsingWays)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 10 | `Statements` | 项目具体说明 | clob | ✓ | 10.33% |  |
| 11 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Type (无形资产类别)

无形资产类别(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 1233，得到无形资产类别的具体描述：1-商标，2-土地使用权，3-非专利技术，4-专利技术，5-特许经营权。

### Ownership (所有权归属)

所有权归属(Ownership)与(CT_SystemConst)表中的DM字段关联，令LB = 1229，得到所有权归属的具体描述：1-上市公司，2-控股股东，3-非控股股东，4-间接股东，5-其它单位。

### AcquiringOrUsingWays (取得或使用方式)

取得或使用方式(AcquiringOrUsingWays)与(CT_SystemConst)表中的DM字段关联，令LB = 1248，得到取得或使用方式的具体描述：1-独立拥有，2-无偿使用，3-有偿使用，4-无偿转让，5-有偿受让，6-有偿租赁，7-外部引进。

## SQL示例

```sql
-- 查询 主营业务与产品_工业产权等无形资产 数据
SELECT *
FROM lc_intangibleasset
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
