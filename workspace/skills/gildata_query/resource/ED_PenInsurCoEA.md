# ED_PenInsurCoEA

**中文名**: 养老保险公司企业年金业务情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `ED_PenInsurCoEA` |
| MySQL表名 | `ed_peninsurcoea` |
| 中文名 | 养老保险公司企业年金业务情况 |
| 路径 | 聚源新版数据库 > 机构数据库 > 保险公司 |
| 更新频率 | 季更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.收录保险机构企业年金业务情况，包括企业年金受托管理业务缴费、企业年金投资管理业务缴费、养老保障及其他委托管理业务缴费、企业年金受托管理资产、企业年金投资管理资产等。
2.数据范围：2007-06-30至今
3.信息来源：中国保监会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `StatPeriod` | 统计区间 | number(10) | ✗ | 100.0% | 统计区间（StatPeriod）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1... |
| 6 | `CompanyCode` | 公司编码 | number(10) | ✗ | 100.0% | 公司编码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 7 | `CompanyName` | 公司名称 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `EATrustValue` | 企业年金受托管理业务缴费 | number(19,4) | ✓ | 21.62% |  |
| 9 | `EAInvestValue` | 企业年金投资管理业务缴费 | number(19,4) | ✓ | 32.82% |  |
| 10 | `EAValue` | 企业年金缴费 | number(19,4) | ✓ | 61.0% |  |
| 11 | `OASEntrustValue` | 养老保障及其他委托管理业务缴费 | number(19,4) | ✓ | 35.52% |  |
| 12 | `EATrustAsset` | 企业年金受托管理资产 | number(19,4) | ✓ | 82.63% |  |
| 13 | `EAInvestAsset` | 企业年金投资管理资产 | number(19,4) | ✓ | 83.78% |  |
| 14 | `OASEntrustAsset` | 养老保障及其他委托管理资产 | number(19,4) | ✓ | 36.68% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StatPeriod (统计区间)

统计区间（StatPeriod）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1074”，得到数据的具体统计区间。   3-期末累计

### CompanyCode (公司编码)

公司编码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到公司的其他基本资料。

## SQL示例

```sql
-- 查询 养老保险公司企业年金业务情况 数据
SELECT *
FROM ed_peninsurcoea
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
