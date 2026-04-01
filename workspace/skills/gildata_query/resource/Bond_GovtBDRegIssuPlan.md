# Bond_GovtBDRegIssuPlan

**中文名**: 地方政府债区域发行计划

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_GovtBDRegIssuPlan` |
| MySQL表名 | `bond_govtbdregissuplan` |
| 中文名 | 地方政府债区域发行计划 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 不定期更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

内容说明：记录财政部披露按区域统计地方政府债券发行计划。
数据范围：2021年至今
信息来源：地方财政局、中国地方政府债券信息公开平台

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `AreaCode` | 区域代码 | number(10) | ✗ | 100.0% | 	 区域代码(AreaCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerC... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `NewLGBGeneral` | 新增债券:一般债券(亿) | number(19,4) | ✓ | 99.49% |  |
| 7 | `NewLGBSpecial` | 新增债券:专项债券(亿) | number(19,4) | ✓ | 99.49% |  |
| 8 | `NewLGBTotal` | 新增债券:合计(亿) | number(19,4) | ✓ | 99.55% |  |
| 9 | `RefiLGBGeneral` | 再融资债券:一般债券(亿) | number(19,4) | ✓ | 83.4% |  |
| 10 | `RefiLGBSpecial` | 再融资债券:专项债券(亿) | number(19,4) | ✓ | 83.4% |  |
| 11 | `RefiLGBTotal` | 再融资债券:合计(亿) | number(19,4) | ✓ | 99.55% |  |
| 12 | `LocalGovtBondGeneral` | 地方政府债:一般债券(亿) | number(19,4) | ✓ | 83.85% |  |
| 13 | `LocalGovtBondSpecial` | 地方政府债:专项债券(亿) | number(19,4) | ✓ | 83.85% |  |
| 14 | `LocalGovtBondTotal` | 地方政府债:合计(亿) | number(19,4) | ✓ | 100.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AreaCode (区域代码)

	
区域代码(AreaCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到区域的地区行政编码、地区中文名称等。

## SQL示例

```sql
-- 查询 地方政府债区域发行计划 数据
SELECT *
FROM bond_govtbdregissuplan
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
