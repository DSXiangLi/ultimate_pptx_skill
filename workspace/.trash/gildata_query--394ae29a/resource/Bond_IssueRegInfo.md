# Bond_IssueRegInfo

**中文名**: 债券发行登记注册信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IssueRegInfo` |
| MySQL表名 | `bond_issuereginfo` |
| 中文名 | 债券发行登记注册信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

1.记录债券发行时，在中国银行间交易商协会登记注册的相关信息同时还包含了同业存单的发行计划。
2.数据范围：2008-04-15 至今
3.信息来源：中国银行间交易商协会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 99.85% |  |
| 3 | `RegMeetingDate` | 注册会议日期 | date | ✓ | 74.37% |  |
| 4 | `BondNature` | 债券类型 | number(10) | ✓ | 96.8% | 债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型... |
| 5 | `RegNoticeNumber` | 注册通知编号 | varchar2(50) | ✗ | 100.0% |  |
| 6 | `CurrencyUnit` | 计价货币 | number(10) | ✓ | 100.0% | 计价货币(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and ... |
| 7 | `InitialRegValue` | 初始注册金额(元) | number(19,4) | ✓ | 97.37% |  |
| 8 | `ChangeAfterRegV` | 变更后注册金额(元) | number(19,4) | ✓ | 2.26% |  |
| 9 | `RegTotalValue` | 注册总金额(元) | number(19,4) | ✓ | 1.23% |  |
| 10 | `RegNoticeIssue` | 注册通知书发出日 | date | ✗ | 100.0% |  |
| 11 | `RegValidEndDate` | 注册有效终止日 | date | ✓ | 92.82% |  |
| 12 | `IssueEndDate` | 首发截止日 | date | ✓ | 29.0% |  |
| 13 | `ValidMaturity` | 有效期期限 | number(10) | ✓ | 100.0% | 有效期期限(ValidMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1723 AN... |
| 14 | `IssueMaturity` | 首发期限 | number(10) | ✓ | 28.96% | 首发期限(IssueMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1723 AND... |
| 15 | `LeadUnderwriter` | 主承销商 | number(10) | ✓ |  |  |
| 16 | `CompanyCode` | 发行人 | number(10) | ✗ | 100.0% | 发行人(CompanyCode)：关联LC_InstiArchive表中的CompanyCode字段 |
| 17 | `InnerCode` | 发行债券代码 | number(10) | ✓ |  |  |
| 18 | `IfInstalment` | 是否可分期 | number(10) | ✓ | 90.59% | 是否可分期(IfInstalment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND ... |
| 19 | `Remark` | 备注说明 | varchar2(500) | ✓ | 48.75% |  |
| 20 | `RegisterType` | 注册类型 | number(10) | ✓ | 3.14% | 注册类型(RegisterType)与(CT_SystemConst)表中的DM字段关联，令LB = 1913，得到注册... |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BondNature (债券类型)

债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型的具体描述：1-企业债券，2-金融债券，3-金融次级债，4-国债现货，5-央行票据，6-短期融资券，7-MBS(房贷支持)，8-ABS(其他支持)，9-混合资本债券，10-可转换债券，11-国库现金管理，12-资产证券化，13-公司债券，14-中期票据，15-转债分离公司债，16-地方政府债券，17-中小企业集合票据，18-集合债券，19-超短期融资券，20-非公开定向债务融资工具，21-次级定期债务，22-中小企业区域集优票据，23-政府支持债券，24-中小企业私募债券，25-资产支持票据，26-小微企业扶持债券，27-二级资本债券，28-中小企业可交换私募债，29-可交换公司债券，30-同业存单，31-区域集优中期票据，32-项目收益票据，33-项目收益债券，34-证券公司短期公司债券，35-保险公司资本补充债券，36-非公开发行公司债，37-信用风险缓释凭证，38-信用联结票据，39-其他一级资本工具，40-标准化票据，41-自贸区债，42-TLAC非资本债券，99-其他。

### CurrencyUnit (计价货币)

计价货币(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1420)，得到计价货币的具体描述：1000-美元，1420-人民币元。

### ValidMaturity (有效期期限)

有效期期限(ValidMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1723 AND DM IN (2,22,23)，得到有效期期限的具体描述：2-2M，22-2Y，23-3Y。

### IssueMaturity (首发期限)

首发期限(IssueMaturity)与(CT_SystemConst)表中的DM字段关联，令LB = 1723 AND DM IN (2,3,4)，得到首发期限的具体描述：2-2M，3-3M，4-6M。

### CompanyCode (发行人)

发行人(CompanyCode)：关联LC_InstiArchive表中的CompanyCode字段

### IfInstalment (是否可分期)

是否可分期(IfInstalment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否可分期的具体描述：1-是，2-否。

### RegisterType (注册类型)

注册类型(RegisterType)与(CT_SystemConst)表中的DM字段关联，令LB = 1913，得到注册类型的具体描述：1-债务融资工具DFI，2-绿色债务融资工具GN，3-自贸试验区债务融资工具F-CP，4-债务融资工具TDFI，5-人民币债券(RB)，6-债券融资工具CB。

## SQL示例

```sql
-- 查询 债券发行登记注册信息 数据
SELECT *
FROM bond_issuereginfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
