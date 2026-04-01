# MF_REITsRestricted

**中文名**: 基础设施基金(REITs)限售

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsRestricted` |
| MySQL表名 | `mf_reitsrestricted` |
| 中文名 | 基础设施基金(REITs)限售 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1 |

## 表描述

1.内容说明：收录基础设施证券投资基金限售方式，限售的企业、限售股份明细.
2.数据范围：2021年至今
3.信息来源：基金公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1880，得到信息来源的具... |
| 5 | `ResLocation` | 限售场所 | number(10) | ✓ | 100.0% | 限售场所(ResLocation)与(CT_SystemConst)表中的DM字段关联，令LB=1652，得到限售场所的... |
| 6 | `ResSharesType` | 限售份额性质 | number(10) | ✓ | 99.95% | 限售份额性质(ResSharesType)与(CT_SystemConst)表中的DM字段关联，令LB=2459，得到限... |
| 7 | `SerialNumber` | 限售对象账户序号 | number(10) | ✗ | 100.0% |  |
| 8 | `SecuAccountNumber` | 证券账户号码 | varchar2(40) | ✓ | 2.55% |  |
| 9 | `SubjectTypeCode` | 主体类型代码 | number(10) | ✓ | 100.0% | 主体类型代码(SubjectTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得... |
| 10 | `ResBidderType` | 限售对象类型 | number(10) | ✓ | 100.0% | 限售对象类型(ResBidderType)与(CT_SystemConst)表中的DM字段关联，令LB=1825，得到限... |
| 11 | `ResBidderName` | 限售对象名称 | varchar2(200) | ✓ | 100.0% |  |
| 12 | `ResBidderCode` | 限售对象编码 | number(10) | ✓ | 71.26% | 当限售对象性质(RestrictedNature)=2-企业时，限售对象编码(BidderCode)和机构基本资料表(L... |
| 13 | `ResShares` | 限售份额(份) | number(18,0) | ✓ | 100.0% |  |
| 14 | `ResType` | 限售类型 | number(10) | ✓ | 100.0% | 限售类型(ResType)与(CT_SystemConst)表中的DM字段关联，令LB=2458，得到限售类型的具体描述... |
| 15 | `LockResTerm` | 限售锁定期限(月) | number(10) | ✓ | 100.0% |  |
| 16 | `Notes` | 备注(锁定期限) | varchar2(200) | ✓ | 0.05% |  |
| 17 | `LockResStartDate` | 锁定限售起始日期 | date | ✓ | 100.0% |  |
| 18 | `EFloatListedStartDate` | 预计可上市流通起始日 | date | ✓ | 100.0% |  |
| 19 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1880，得到信息来源的具体描述：1-基金定期报告，101-招募说明书，102-提前/延长募集期，103-基金分红，104-份额拆分折算，105-基金合同生效，106-上市交易公告书，107-开放/暂停申赎等，108-公司股东/高管变更，109-通讯地址/电话变更，110-基金经理变更，111-战略投资者场内限售及场外锁定公告，112-限售解禁公告，201-固有资金投资，202-收益集中支付，203-风险提示，204-新增代销机构，205-估值调整，206-费率优惠，207-更新招募书，999-其他。

### ResLocation (限售场所)

限售场所(ResLocation)与(CT_SystemConst)表中的DM字段关联，令LB=1652，得到限售场所的具体描述：1-场内，2-场外，3-场内和场外。

### ResSharesType (限售份额性质)

限售份额性质(ResSharesType)与(CT_SystemConst)表中的DM字段关联，令LB=2459，得到限售份额性质的具体描述：1-原始权益人及关联方基金份额发售总量的20%持有期自上市之日起不少于60个月，2-原始权益人及关联方基金份额发售总量超过20%部分持有期自上市之日起不少于36个月，3-其他专业机构投资者持有份额限售。

### SubjectTypeCode (主体类型代码)

主体类型代码(SubjectTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到主体类型代码的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### ResBidderType (限售对象类型)

限售对象类型(ResBidderType)与(CT_SystemConst)表中的DM字段关联，令LB=1825，得到限售对象类型的具体描述：1-公募基金，2-社保基金或社保基金组合，3-个人或个人自有资金投资账户，4-其他，5-企业年金计划，6-机构自营投资账户，7-证券公司集合资产管理计划，8-基金公司或其资产管理子公司一对一，9-保险资金投资账户，10-证券公司限额特定资产管理计划，11-基金公司或其资产管理子公司一对多，12-QFII投资账户，13-私募基金，14-证券公司定向资产管理计划，15-集合信托计划，16-保险机构资产管理产品，17-期货公司或其资产管理子公司一对多。

### ResBidderCode (限售对象编码)

当限售对象性质(RestrictedNature)=2-企业时，限售对象编码(BidderCode)和机构基本资料表(LC_InstiArchive)中的CompanyCode关联。

### ResType (限售类型)

限售类型(ResType)与(CT_SystemConst)表中的DM字段关联，令LB=2458，得到限售类型的具体描述：1-原始权益人及其同一控制下关联方，2-其他专业机构投资者战略配售限售。

## SQL示例

```sql
-- 查询 基础设施基金(REITs)限售 数据
SELECT *
FROM mf_reitsrestricted
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
