# MF_PurAndRedStatusA

**中文名**: 公募基金销售状态更改附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PurAndRedStatusA` |
| MySQL表名 | `mf_purandredstatusa` |
| 中文名 | 公募基金销售状态更改附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

收录公募基金申赎状态更改表涉及的多维度数据，包括合并限额的相关基金代码、特殊平台的公司代码、限额等信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与MF_PurAndRedStatus的ID关联，获取基金销售状态的相关信息。 |
| 3 | `TypeCode` | 类别代码 | number(10) | ✗ | 100.0% | 类别代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=2649，得到类别代码的具体描... |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `DataCode` | 代码 | number(10) | ✓ | 100.0% | 代码（DataCode）：当TypeCode=1，与“证券主表（SecuMain）”中的“证券内部编码（InnerCod... |
| 6 | `DataNum` | 数据 | varchar2(100) | ✓ | 2.11% |  |
| 7 | `DataValue` | 数值 | number(19,2) | ✓ | 2.11% |  |
| 8 | `Unit` | 单位 | number(10) | ✓ | 2.11% | 单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND DM IN (16,7,... |
| 9 | `Remark` | 备注说明 | varchar2(500) | ✓ | 0.1% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与MF_PurAndRedStatus的ID关联，获取基金销售状态的相关信息。

### TypeCode (类别代码)

类别代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=2649，得到类别代码的具体描述：1-合并限额基金代码，2-特殊平台机构代码。

### DataCode (代码)

代码（DataCode）：当TypeCode=1，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到合并限额相关基金代码的基本信息；当TypeCode=2，与“机构基本资料（LC_InstiArchive）”中“企业编号（CompanyCode）”关联，得到特殊平台机构代码的基本信息。

### Unit (单位)

单位(Unit)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND DM IN (16,7,14)，得到单位的具体描述：7-元，14-美元，16-份。

## SQL示例

```sql
-- 查询 公募基金销售状态更改附表 数据
SELECT *
FROM mf_purandredstatusa
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
