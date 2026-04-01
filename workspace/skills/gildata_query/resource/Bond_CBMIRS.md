# Bond_CBMIRS

**中文名**: 中债债券MIRS

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBMIRS` |
| MySQL表名 | `bond_cbmirs` |
| 中文名 | 中债债券MIRS |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债市场隐含评级的分层信息，包含隐含评级、中债MIRS、存量隐含评级、存量综合MIRS等
2.数据范围：2024年4月30日至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `ImpliedGrade` | 隐含评级 | number(10) | ✓ | 77.66% | 隐含评级(ImpliedGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 2080，得到隐含... |
| 5 | `MIRS` | 中债MIRS | varchar2(20) | ✓ | 100.0% | 中债 MIRS 以“债券档位/隐含评级分档数量”的形式展示，其中，债券档位由小到大表示债券估值信用利差由小到大，“+”表... |
| 6 | `BondRank` | 债券档位 | varchar2(10) | ✓ | 100.0% |  |
| 7 | `ImpliedGradeRankVol` | 隐含评级分档数量 | varchar2(10) | ✓ | 100.0% |  |
| 8 | `StockImpliedGrade` | 存量隐含评级 | number(10) | ✓ | 72.03% | 存量隐含评级(StockImpliedGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 20... |
| 9 | `StockCIMIRS` | 存量综合MIRS | varchar2(20) | ✓ | 93.9% |  |
| 10 | `CIBondRank` | 综合债券档位 | varchar2(10) | ✓ | 93.9% |  |
| 11 | `CIImpliedGradeRankVol` | 综合隐含评级分档数量 | varchar2(10) | ✓ | 93.9% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

### ImpliedGrade (隐含评级)

隐含评级(ImpliedGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 2080，得到隐含评级的具体描述：100-D，200-C，210-CC，220-CCC，300-B-，301-B，302-B+，310-BB-，311-BB，312-BB+，320-BBB-，321-BBB，322-BBB+，400-A-(2)，401-A(2)，402-A+(2)，410-A-，411-A，412-A+，420-AA-(2)，421-AA(2)，422-AA+(2)，430-AA-，431-AA，432-AA+，440-AAA-(2)，441-AAA(2)，442-AAA+(2)，450-AAA-，451-AAA，452-AAA+。

### MIRS (中债MIRS)

中债 MIRS 以“债券档位/隐含评级分档数量”的形式展示，其中，债券档位由小到大表示债券估值信用利差由小到大，“+”表示债券估值信用利差小于第 1 档，“-”表示债券估值信用利差大于最后一档；更加精细化、更具区分度，有助于实施更灵活有效的信用投资与风险管理策略

### StockImpliedGrade (存量隐含评级)

存量隐含评级(StockImpliedGrade)与(CT_SystemConst)表中的DM字段关联，令LB = 2080，得到存量隐含评级的具体描述：100-D，200-C，210-CC，220-CCC，300-B-，301-B，302-B+，310-BB-，311-BB，312-BB+，320-BBB-，321-BBB，322-BBB+，400-A-(2)，401-A(2)，402-A+(2)，410-A-，411-A，412-A+，420-AA-(2)，421-AA(2)，422-AA+(2)，430-AA-，431-AA，432-AA+，440-AAA-(2)，441-AAA(2)，442-AAA+(2)，450-AAA-，451-AAA，452-AAA+。

## SQL示例

```sql
-- 查询 中债债券MIRS 数据
SELECT *
FROM bond_cbmirs
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
