# Bond_UnderwriterAmount

**中文名**: 债券发行承销金额

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_UnderwriterAmount` |
| MySQL表名 | `bond_underwriteramount` |
| 中文名 | 债券发行承销金额 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定期更新 |
| 字段数量 | 25 |
| 版本 | 1.02 |

## 表描述

内容说明：收录各类债券的承销商、分销商的名称及机构编号等。
涵盖券种：可转换债券、企业债、金融债、资产支持证券等。
数据范围：1992-08-12 至今
信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 债券主内部编码 | number(10) | ✗ | 100.0% | 债券主内部编码(MainCode)：与“债券代码对照表（Bond_Code）”中的“	统一内部编码(不同市场交易的同一债... |
| 3 | `IssueType` | 发行类型 | number(10) | ✗ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✓ | 100.0% |  |
| 5 | `IssueAndListType` | 发行与上市类别 | number(10) | ✓ | 100.0% | 发行与上市类别(IssueAndListType)与(CT_SystemConst)表中的DM字段关联，令LB =101... |
| 6 | `AgentType` | 承销商类型 | number(10) | ✗ | 100.0% | 承销商类型(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM... |
| 7 | `AgentCode` | 机构代码 | number(10) | ✗ | 100.0% |  |
| 8 | `FullName` | 机构全称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `FullNameDisc` | 机构全称(披露) | varchar2(200) | ✓ | 100.0% |  |
| 10 | `NumPartUnderwriters` | 参与统计承销商个数 | number(10) | ✓ | 100.0% |  |
| 11 | `UnderwritingSumAct` | 承销金额(万元)(实际) | number(19,4) | ✓ | 0.0% |  |
| 12 | `UnderwritingVolAct` | 承销数量(张)(实际) | number(10) | ✓ | 0.0% |  |
| 13 | `UnderwritingRatioAct` | 承销比例(%)(实际) | number(9,4) | ✓ | 0.0% |  |
| 14 | `UnderwritingSumAvg` | 承销金额(万元)(平均分配) | number(19,4) | ✓ | 100.0% |  |
| 15 | `UnderwritingVolAvg` | 承销数量(张)(平均分配) | number(10) | ✓ | 100.0% |  |
| 16 | `UnderwritingRatioAvg` | 承销比例(%)(平均分配) | number(9,4) | ✓ | 100.0% |  |
| 17 | `BoughtDealAmount` | 包销金额(万元)(实际) | number(19,4) | ✓ | 1.49% |  |
| 18 | `BDCommitmentRatio` | 包销比例(%)(实际) | number(9,4) | ✓ | 1.49% |  |
| 19 | `SelfPlacementAmount` | 自营资金获配金额(万元)(实际) | number(19,4) | ✓ | 0.61% |  |
| 20 | `SelfPlacementRatio` | 自营资金获配比例(%)(实际) | number(9,4) | ✓ | 0.61% |  |
| 21 | `IssueCost` | 发行费用(万元) | number(19,4) | ✓ | 31.94% |  |
| 22 | `UnderwritingSpnsrFee` | 承销与保荐费用(万元) | number(19,4) | ✓ | 0.22% |  |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (债券主内部编码)

债券主内部编码(MainCode)：与“债券代码对照表（Bond_Code）”中的“	统一内部编码(不同市场交易的同一债券)（MainCode）”关联，得到债券的交易代码、债券简称等。

### IssueAndListType (发行与上市类别)

发行与上市类别(IssueAndListType)与(CT_SystemConst)表中的DM字段关联，令LB =1016，得到发行与上市类别的具体描述：1-配股，2-发行新股，3-增发新股，4-可转换债券，5-吸收合并，6-基金发行，7-基金扩募，8-企业债券，9-基金营销，10-金融债券，11-股权分置，12-资产支持证券，13-权证发行，14-信用风险，15-港交所基金发行，16-可交换公司债券，17-优先股发行，18-CDR首发，19-CDR增发，20-CDR配股，21-非公开增发，22-公开增发，23-非公开增发配套融资，99-其他证券发行。

### AgentType (承销商类型)

承销商类型(AgentType)与(CT_SystemConst)表中的DM字段关联，令LB = 2177 AND DM IN (1,126,5)，得到承销商类型的具体描述：1-主承销商，5-联席主承销商，126-推广机构/销售机构。

## SQL示例

```sql
-- 查询 债券发行承销金额 数据
SELECT *
FROM bond_underwriteramount
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
