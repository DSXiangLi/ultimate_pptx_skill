# Bond_ConBDIssPrjAttch

**中文名**: 可转债发行预案附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDIssPrjAttch` |
| MySQL表名 | `bond_conbdissprjattch` |
| 中文名 | 可转债发行预案附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 7 |
| 版本 | 1 |

## 表描述

内容说明：包含可转换债券在发行预案中列示的各类发行条款。
数据范围：1992-11-01 至今
信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID(RID)：与“可转债发行预案(Bond_ConBDIssueProject)”表的ID字段相关联。 |
| 3 | `InfoType` | 信息类别 | number(10) | ✗ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2624 AND DM >... |
| 4 | `InfoContent` | 信息内容 | clob | ✓ | 100.0% |  |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID(RID)：与“可转债发行预案(Bond_ConBDIssueProject)”表的ID字段相关联。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 2624 AND DM >= 105，得到信息类别的具体描述：105-募集资金用途，201-利率及付息条款，202-利息补偿条款，203-初始转股价确定条款，204-转股价格调整条款，205-转股价格修正条款，206-赎回条款，207-到期赎回条款，208-回售条款，209-转换期条款，210-向原股东配售安排条款。

## SQL示例

```sql
-- 查询 可转债发行预案附表 数据
SELECT *
FROM bond_conbdissprjattch
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
