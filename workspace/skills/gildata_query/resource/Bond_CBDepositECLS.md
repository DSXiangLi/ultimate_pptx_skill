# Bond_CBDepositECLS

**中文名**: 中债存款预期信用损失(标准)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDepositECLS` |
| MySQL表名 | `bond_cbdepositecls` |
| 中文名 | 中债存款预期信用损失(标准) |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中债发布的存款预期信用损失的标准化数据，包括存款机构代码和信用损失比例等数据
2.数据范围：2021-12-7 至今
3.信息来源：中债登

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 存款机构代码 | number(10) | ✗ | 100.0% | 存款机构代码(CompanyCode): 与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `YearsToMaturity` | 待偿期 | number(18,8) | ✗ | 100.0% |  |
| 5 | `MaturityDesc` | 期限描述 | varchar2(20) | ✓ | 100.0% |  |
| 6 | `CreditLossR` | 信用损失比例(%) | number(18,8) | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (存款机构代码)

存款机构代码(CompanyCode): 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

## SQL示例

```sql
-- 查询 中债存款预期信用损失(标准) 数据
SELECT *
FROM bond_cbdepositecls
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
