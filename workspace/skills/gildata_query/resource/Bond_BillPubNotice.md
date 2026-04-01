# Bond_BillPubNotice

**中文名**: 票据催告公示

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BillPubNotice` |
| MySQL表名 | `bond_billpubnotice` |
| 中文名 | 票据催告公示 |
| 路径 | 聚源新版数据库 > 债券数据库 > 票据基本信息 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：记录风险票据信息，如票面金额、出票日期、出票人等
2.数据范围：2015-6-18 至今
3.信息来源：人民法院公告网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 3 | `BillCode` | 票号 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `BillTypeCode` | 票据类型代码 | number(10) | ✗ | 100.0% | 票据类型代码（BillTypeCode）：1001-银票，1002-商票 |
| 5 | `ParValue` | 票面金额(元) | number(20,4) | ✓ | 97.71% |  |
| 6 | `IssueDate` | 出票日期 | date | ✓ | 87.08% |  |
| 7 | `MaturityDate` | 到期日 | date | ✓ | 74.45% |  |
| 8 | `Drawer` | 出票人 | varchar2(200) | ✓ | 91.92% |  |
| 9 | `DrawerID` | 出票人公司代码 | number(10) | ✓ | 82.75% |  |
| 10 | `PayBankAcct` | 付款银行 | varchar2(200) | ✓ | 84.68% |  |
| 11 | `StatusCategory` | 状态类别 | varchar2(40) | ✗ | 100.0% |  |
| 12 | `Applicant` | 申请人 | varchar2(200) | ✓ | 99.98% |  |
| 13 | `ApplicantID` | 申请人公司代码 | number(10) | ✓ | 92.19% |  |
| 14 | `PubOrgName` | 发布机构 | varchar2(200) | ✓ | 99.98% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BillTypeCode (票据类型代码)

票据类型代码（BillTypeCode）：1001-银票，1002-商票

## SQL示例

```sql
-- 查询 票据催告公示 数据
SELECT *
FROM bond_billpubnotice
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
