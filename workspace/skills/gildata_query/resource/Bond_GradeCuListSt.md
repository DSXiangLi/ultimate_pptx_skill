# Bond_GradeCuListSt

**中文名**: 评级客户名单统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_GradeCuListSt` |
| MySQL表名 | `bond_gradeculistst` |
| 中文名 | 评级客户名单统计 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券评级信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.记录各大评级公司定期统计并发布债务融资时信用评级的企业名单。
2.数据范围：2006-01-06 至今
3.信息来源：评级公司官网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `PubTitle` | 公告标题 | varchar2(500) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 AND DM... |
| 5 | `PubOrgName` | 发布机构 | varchar2(500) | ✓ | 100.0% |  |
| 6 | `PubOrgCode` | 发布机构编号 | number(10) | ✗ | 100.0% |  |
| 7 | `StatBeginDate` | 统计起始日期 | date | ✗ | 100.0% |  |
| 8 | `StatEndDate` | 统计截止日期 | date | ✓ | 100.0% |  |
| 9 | `NB` | 序号 | number(10) | ✓ | 100.0% |  |
| 10 | `InstitutionName` | 机构名称 | varchar2(500) | ✓ | 100.0% |  |
| 11 | `InstitutionCode` | 机构编号 | number(10) | ✗ | 100.0% |  |
| 12 | `Remark` | 备注 | varchar2(1000) | ✓ | 0.0% |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 AND DM IN (71,72,99)，得到信息来源的具体描述：71-中国货币网，72-中国债券信息网，99-其他。

## SQL示例

```sql
-- 查询 评级客户名单统计 数据
SELECT *
FROM bond_gradeculistst
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
