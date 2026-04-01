# Bond_YieldBasicInfoCB

**中文名**: 债券收益率基本要素

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_YieldBasicInfoCB` |
| MySQL表名 | `bond_yieldbasicinfocb` |
| 中文名 | 债券收益率基本要素 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券利差专题 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `MainCode` | 债券统一代码 | number(10) | ✓ | 100.0% |  |
| 4 | `EndDate` | 估值日期 | date | ✗ | 100.0% |  |
| 5 | `CompoundMethod` | 利率类型 | number(10) | ✓ | 99.99% | 利率类型(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 6 | `FRNRefRateText` | 浮动利率计息基准 | number(10) | ✓ | 4.66% |  |
| 7 | `FRNRefRateDate` | 浮动利率计息基准日 | date | ✓ | 1.01% |  |
| 8 | `FRNRefRate` | 基准利率 | number(19,8) | ✓ | 0.0% |  |
| 9 | `VPYield` | 估价收益率 | number(18,10) | ✓ | 100.0% |  |
| 10 | `ImpliedGrade` | 隐含评级代码 | number(10) | ✓ | 68.22% |  |
| 11 | `ImpliedGradeDesc` | 隐含评级 | varchar2(10) | ✓ | 68.22% |  |
| 12 | `TrueRemainMaturity` | 实际待偿期 | number(18,8) | ✓ | 100.0% |  |
| 13 | `CredibilityCode` | 可信度代码 | number(10) | ✗ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 14 | `CredibilityDesc` | 可信度 | varchar2(50) | ✓ | 100.0% |  |
| 15 | `TotalSize` | 剩余总规模 | number(19,8) | ✓ | 100.0% |  |
| 16 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompoundMethod (利率类型)

利率类型(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AND DM in (1,3,4,5,6)，得到利率类型的具体描述：1-单利(固定利率)，3-浮动利率，4-累进利率，5-贴现，6-无序利率。

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

## SQL示例

```sql
-- 查询 债券收益率基本要素 数据
SELECT *
FROM bond_yieldbasicinfocb
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
