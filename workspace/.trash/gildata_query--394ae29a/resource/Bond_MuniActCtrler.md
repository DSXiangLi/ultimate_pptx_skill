# Bond_MuniActCtrler

**中文名**: 城投疑似实际控制人表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_MuniActCtrler` |
| MySQL表名 | `bond_muniactctrler` |
| 中文名 | 城投疑似实际控制人表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 城投专题信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.本表收录了城投平台的实际控制人信息、政府对城投的控制类型、政府持股比例、政府对城投的控股路径等信息，用于判断城投在股权维度上的政府参与度。
2.其中政府对城投的控制类型分为直接控股、间接控股两种。
3.其中政府对城投的控股路径为：当最短控股路径=1时，城投平台为政府的子公司。当最短控股路径=2时，城投平台为政府的孙公司。……

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 4 | `ActCtrlCompanyCode` | 实际控制人公司代码 | number(10) | ✗ | 100.0% |  |
| 5 | `ControllerType` | 实际控制人类型 | number(10) | ✓ | 100.0% | 实际控制人类型(ControllerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783... |
| 6 | `Controltype` | 控制类型 | number(10) | ✓ | 100.0% | 控制类型(Controltype)与(CT_SystemConst)表中的DM字段关联，令LB= 2509，得到控制类型... |
| 7 | `EquityRatio` | 投资比例 | number(9,6) | ✓ | 99.97% |  |
| 8 | `PathLevel` | 路径层级 | varchar2(2000) | ✓ | 100.0% |  |
| 9 | `PathLevelMin` | 最短路径 | number(10) | ✓ | 100.0% |  |
| 10 | `PathLevelMax` | 最长路径 | number(10) | ✓ | 100.0% |  |
| 11 | `PathAmount` | 路径数量 | number(10) | ✓ | 100.0% |  |
| 12 | `IfEffective` | 是否生效 | number(10) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ControllerType (实际控制人类型)

实际控制人类型(ControllerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2)，得到实际控制人类型的具体描述：1-自然人，2-企业。

### Controltype (控制类型)

控制类型(Controltype)与(CT_SystemConst)表中的DM字段关联，令LB= 2509，得到控制类型的具体描述：1-直接控股，2-间接控股。

## SQL示例

```sql
-- 查询 城投疑似实际控制人表 数据
SELECT *
FROM bond_muniactctrler
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
