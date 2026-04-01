# Bond_ABSWaterfall

**中文名**: 资产支持证券分配机制

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ABSWaterfall` |
| MySQL表名 | `bond_abswaterfall` |
| 中文名 | 资产支持证券分配机制 |
| 路径 | 聚源新版数据库 > 债券数据库 > 资产支持证券信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录资产支持证券发行说明书公布的现金流分配机制，包括证券端在正常、违约、加速清偿等情景下的偿付顺序，包括银行间和交易所ABS，分配机制以整个项目维度展示
2.数据范围：目前涵盖银行间ABS 2017年12月31日之后到期的项目
3.信息来源：募集说明书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 数据日期 | date | ✓ | 99.99% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 and DM... |
| 5 | `ConditionOne` | 事件一 | number(10) | ✗ | 100.0% | 事件一(ConditionOne)与(Bond_SystemConst)表中的DM字段关联，令LB = 101，得到事件... |
| 6 | `ConditionTwo` | 事件二 | number(10) | ✗ | 100.0% | 事件二(ConditionTwo)与(Bond_SystemConst)表中的DM字段关联，令LB = 102，得到事件... |
| 7 | `CollAccount` | 收款账户 | number(10) | ✗ | 100.0% | 收款账户(CollAccount)与(Bond_SystemConst)表中的DM字段关联，令LB = 103，得到收款... |
| 8 | `PaymentAccount` | 付款账户 | number(10) | ✓ | 13.21% | 付款账户(PaymentAccount)与(Bond_SystemConst)表中的DM字段关联，令LB = 104，得... |
| 9 | `PriorityNo` | 偿付序号 | number(10) | ✗ | 100.0% |  |
| 10 | `TrancheInnerCode` | 涉及个券内码 | number(10) | ✓ | 54.27% | 涉及个券内码（TrancheInnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（Inne... |
| 11 | `PaymentItem` | 偿付项目 | number(10) | ✗ | 100.0% | 偿付项目(PaymentItem)与(Bond_SystemConst)表中的DM字段关联，令LB = 106，得到偿付... |
| 12 | `Proportional` | 同顺序偿还 | number(10) | ✓ | 11.49% | 同顺序偿还(Proportional)与(Bond_SystemConst)表中的DM字段关联，令LB = 105，得到... |
| 13 | `IfRevolvingPeriod` | 是否循环购买期 | number(10) | ✓ | 13.42% | 是否循环购买期(IfRevolvingPeriod)与(Bond_SystemConst)表中的DM字段关联，令LB =... |
| 14 | `Iflimitative` | 金额限制 | number(10) | ✓ | 25.41% | 金额限制(Iflimitative)与(Bond_SystemConst)表中的DM字段关联，令LB = 107，得到金... |
| 15 | `Limitation` | 限额描述 | varchar2(1000) | ✓ | 2.05% |  |
| 16 | `IfInclUnpaid` | 是否包括累计未付 | number(10) | ✓ | 12.89% | 是否包括累计未付(IfInclUnpaid)与(Bond_SystemConst)表中的DM字段关联，令LB = 108... |
| 17 | `Text` | 偿付顺序描述 | varchar2(2000) | ✓ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；对于多只债券的ABS项目，还可与“债券代码关联（Bond_CodeRelated）”中的“内部编码（InnerCode）”关联，得到此ABS项目中其他的债券（关联代码内部编码）

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 and DM in (200103,200204,600301)，得到信息来源的具体描述：200103-募集说明书，200204-受托机构报告，600301-评级公告。

### ConditionOne (事件一)

事件一(ConditionOne)与(Bond_SystemConst)表中的DM字段关联，令LB = 101，得到事件一的具体描述：1-违约前，2-违约后，3-信托终止后，4-差额补足，5-到期分配，6-续发终止前，7-续发终止后，8-信托提前终止，9-临时分配，10-循环期提前分配，11-提前结束循环购买期前，12-提前结束循环购买期后，13-再融资分配，14-展期前，15-展期后，16-回款充足，17-回款不足，18-发生早偿事件后，19-发生保险生效事件后，20-REITs份额变现分配，21-特定事件。

### ConditionTwo (事件二)

事件二(ConditionTwo)与(Bond_SystemConst)表中的DM字段关联，令LB = 102，得到事件二的具体描述：1-未加速清偿，2-加速清偿后，3-正常，4-回售后，5-回购后。

### CollAccount (收款账户)

收款账户(CollAccount)与(Bond_SystemConst)表中的DM字段关联，令LB = 103，得到收款账户的具体描述：1-收益账，2-本金账，3-总分配账。

### PaymentAccount (付款账户)

付款账户(PaymentAccount)与(Bond_SystemConst)表中的DM字段关联，令LB = 104，得到付款账户的具体描述：1-税收账户，2-费用和开支账户，3-证券账户。

### TrancheInnerCode (涉及个券内码)

涉及个券内码（TrancheInnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

### PaymentItem (偿付项目)

偿付项目(PaymentItem)与(Bond_SystemConst)表中的DM字段关联，令LB = 106，得到偿付项目的具体描述：101-利息，102-本金，103-次级期间收益，104-REITs分配后收益，201-转入收益账，202-转入本金账，203-留存在原账户，204-转入储备账户，301-循环购买使用，302-余额作为次级收益，501-税收，601-费用和开支，999-按其他约定运用。

### Proportional (同顺序偿还)

同顺序偿还(Proportional)与(Bond_SystemConst)表中的DM字段关联，令LB = 105，得到同顺序偿还的具体描述：1-按未偿比例偿还，2-按REITs分配比例偿还。

### IfRevolvingPeriod (是否循环购买期)

是否循环购买期(IfRevolvingPeriod)与(Bond_SystemConst)表中的DM字段关联，令LB = 109，得到是否循环购买期的具体描述：1-循环购买期，2-摊还期，3-自定义区间1，4-自定义区间2。

## SQL示例

```sql
-- 查询 资产支持证券分配机制 数据
SELECT *
FROM bond_abswaterfall
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
