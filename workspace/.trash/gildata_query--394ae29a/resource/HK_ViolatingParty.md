# HK_ViolatingParty

**中文名**: 港股违规当事人表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_ViolatingParty` |
| MySQL表名 | `hk_violatingparty` |
| 中文名 | 港股违规当事人表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.新建港股违规当事人表，记录香港证监会和香港联交所披露的违规主体及处罚事项；
2.历史数据：2001年至今；
3.数据来源：港交所及香港证监会。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EventCode` | 事件编号 | number(10) | ✗ | 100.0% | 事件编号（EventCode）：与“港股违规事项表（HK_Irregularities）”中的“事件编号（EventCo... |
| 3 | `PartyName` | 当事人 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `PartyType` | 当事人性质 | number(10) | ✓ | 100.0% | 当事人性质（PartyType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1... |
| 5 | `PartyCode` | 当事人编码 | number(10) | ✓ | 22.66% | 当事人编码（PartyCode）：当当事人性质=2企业时，当事人编码（PartyCode）与港股企业概括表（HK_Com... |
| 6 | `Relationship` | 关联关系 | number(10) | ✓ | 77.3% | 关联关系（Relationship）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=... |
| 7 | `RelataCompany` | 关联上市公司 | number(10) | ✓ | 77.18% | 关联上市公司（RelataCompany）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyC... |
| 8 | `Punishment` | 处罚措施 | number(10) | ✓ | 100.0% | 处罚措施（Punishment）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“2... |
| 9 | `ViolatingIssues` | 违规事项 | varchar2(2000) | ✓ | 100.0% |  |
| 10 | `Misdeeds` | 违规行为 | varchar2(2000) | ✓ | 100.0% |  |
| 11 | `EnforcAction` | 执法行动 | clob | ✓ | 28.71% |  |
| 12 | `PenaltyAmount` | 处罚金额 | number(19,4) | ✓ | 8.83% |  |
| 13 | `PenaltyCurrency` | 处罚币种 | number(10) | ✓ | 8.83% | 处罚币种（PenaltyCurrency）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令... |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### EventCode (事件编号)

事件编号（EventCode）：与“港股违规事项表（HK_Irregularities）”中的“事件编号（EventCode）”关联得到违规事件的描述。

### PartyType (当事人性质)

当事人性质（PartyType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1783”，得到“当事人性质”描述。
       1-自然人,2-企业,3-证券品种,99-其他

### PartyCode (当事人编码)

当事人编码（PartyCode）：当当事人性质=2企业时，当事人编码（PartyCode）与港股企业概括表（HK_CompanyArchives）的公司代码（CompanyCode）关联，获取到当事人的其他信息。

### Relationship (关联关系)

关联关系（Relationship）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1746”，得到“关联关系”描述。
       1-本公司,2-公司大股东,3-公司前大股东,4-公司股东,5-公司前股东等

### RelataCompany (关联上市公司)

关联上市公司（RelataCompany）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### Punishment (处罚措施)

处罚措施（Punishment）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“2106”，得到“处罚措施”描述。
       10-冻结资产,20-检控,30-批评,40-谴责,50-指控等

### PenaltyCurrency (处罚币种)

处罚币种（PenaltyCurrency）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“处罚币种”描述。
       1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑， 5010-加拿大元，6010-澳大利亚元

## SQL示例

```sql
-- 查询 港股违规当事人表 数据
SELECT *
FROM hk_violatingparty
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
