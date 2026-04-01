# Bond_SBFC_CF

**中文名**: 标准债券远期转换因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SBFC_CF` |
| MySQL表名 | `bond_sbfc_cf` |
| 中文名 | 标准债券远期转换因子 |
| 路径 | 聚源新版数据库 > 债券数据库 > 标准债券远期合约 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.该表记录标准债券远期转换因子
2.数据范围：2015-04-06 至今
3.信息来源：货币网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `IssuanceOrg` | 发布机构 | number(10) | ✓ | 100.0% | 发布机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 AND D... |
| 4 | `ContractInnerCode` | 合约内部编码 | number(10) | ✓ | 100.0% | 合约内部编码（ContractInnerCode）：与“标准债券远期合约基本信息（Bond_SBFC_Info）”中的“... |
| 5 | `InnerCode` | 债券内部编码 | number(10) | ✓ | 100.0% | 债券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 6 | `ConversionFactors` | 转换因子 | number(19,8) | ✓ | 77.02% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IssuanceOrg (发布机构)

发布机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1183 AND DM IN (71,134)，得到发布机构的具体描述：71-中国货币网，134-上海清算所。

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“标准债券远期合约基本信息（Bond_SBFC_Info）”中的“合约内部编码（ContractInnerCode）”关联，得到该合约的基础信息。

### InnerCode (债券内部编码)

债券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 标准债券远期转换因子 数据
SELECT *
FROM bond_sbfc_cf
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
