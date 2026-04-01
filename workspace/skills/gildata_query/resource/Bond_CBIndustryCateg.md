# Bond_CBIndustryCateg

**中文名**: 中债行业分类

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBIndustryCateg` |
| MySQL表名 | `bond_cbindustrycateg` |
| 中文名 | 中债行业分类 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债金融估值中心发布的中债行业分类数据，包含一级分类和二级分类等。
2.数据范围：2023年6月1日至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 4 | `Issuer` | 发行人 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 6 | `IssuerOrganizationCode` | 发行人组织机构代码 | varchar2(30) | ✓ | 81.77% |  |
| 7 | `ClassifiCategory` | 行业分类-门类 | number(10) | ✓ | 100.0% |  |
| 8 | `ClassifiCategoryDesc` | 行业分类-门类描述 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `ClassifiMajor` | 行业分类-大类 | number(10) | ✓ | 99.98% |  |
| 10 | `ClassifiMajorDesc` | 行业分类-大类描述 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `SocialCreditCode` | 社会统一征信码 | varchar2(30) | ✓ | 79.9% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 中债行业分类 数据
SELECT *
FROM bond_cbindustrycateg
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
