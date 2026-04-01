# Bond_RegInfo

**中文名**: 债券注册信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RegInfo` |
| MySQL表名 | `bond_reginfo` |
| 中文名 | 债券注册信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 滚动更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.收录债券的注册进度信息，主要包含券种有小公募、私募、交易所ABS、企业债、交易商协会注册的品种。
2.数据范围：2012年至今
3.信息来源：中债登、交易所、交易商协会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InitialInfoPublDate` | 首次公告日期 | date | ✗ | 100.0% |  |
| 3 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 ... |
| 5 | `ChiName` | 债券名称 | varchar2(200) | ✗ | 100.0% |  |
| 6 | `Issuer` | 发行人 | varchar2(1000) | ✓ | 99.95% |  |
| 7 | `AreaName` | 所属地区 | varchar2(200) | ✓ | 10.43% |  |
| 8 | `Industry` | 所属行业 | varchar2(200) | ✓ | 7.91% |  |
| 9 | `BondNature` | 债券品种 | number(10) | ✓ | 99.98% | 债券品种(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1936，得到债券品种... |
| 10 | `RegTotalValue` | 注册拟发金额(亿) | number(19,8) | ✓ | 98.69% |  |
| 11 | `ProjectStatus` | 项目状态 | number(10) | ✓ | 99.99% | 项目状态(ProjectStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 1937，得到项... |
| 12 | `RegNoticeNumber` | 注册通知书文号 | varchar2(50) | ✓ | 39.4% |  |
| 13 | `ExchangeConNumber` | 交易所确认文件文号 | varchar2(50) | ✓ | 31.34% |  |
| 14 | `RegisterType` | 注册或备案类型 | number(10) | ✓ | 47.05% | 注册或备案类型(RegisterType)与(CT_SystemConst)表中的DM字段关联，令LB = 2310，得... |
| 15 | `AcceptanceDate` | 受理日期 | date | ✓ | 37.95% |  |
| 16 | `LeadUnderwriter` | 承销商/管理人名称 | varchar2(1000) | ✓ | 52.96% |  |
| 17 | `Remark` | 备注 | varchar2(2000) | ✓ | 0.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 AND DM in (69,70,72,136,410007600)，得到信息来源编码的具体描述：69-上海证券交易所，70-深圳证券交易所，72-中国债券信息网，136-中国银行间市场交易商协会，410007600-北京证券交易所。

### BondNature (债券品种)

债券品种(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1936，得到债券品种的具体描述：1-小公募，2-私募，3-ABS ，4-大公募，5-企业债，6-SCP，7-CP，8-MTN，9-DFI，10-PN，11-ABN，12-PRN，13-PB-CP，14-PB-MTN，15-PB-RB，16-PB，17-SMECNII，18-TDFI，19-基础设施REITs，20-PB-DFI，21-CB，22-PB-其他。

### ProjectStatus (项目状态)

项目状态(ProjectStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 1937，得到项目状态的具体描述：1-已受理，2-已反馈，3-已接收反馈意见 ，4-通过 ，5-不通过 ，6-终止 ，7-已申报，8-已回复交易所意见，9-预评中，10-待上会，11-反馈中，12-完成注册，13-提交注册，14-注册结果，15-注册生效，16-不予注册，17-受理反馈待答复，18-已注册，19-已上会，20-中止审核，21-终止受理，22-已撤销申请，23-不予受理，24-已问询，25-审议会议，26-注册通过。

### RegisterType (注册或备案类型)

注册或备案类型(RegisterType)与(CT_SystemConst)表中的DM字段关联，令LB = 2310，得到注册或备案类型的具体描述：1-备案，2-注册。

## SQL示例

```sql
-- 查询 债券注册信息 数据
SELECT *
FROM bond_reginfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
