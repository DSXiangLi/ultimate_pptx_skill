# Bond_ConBDCallPutInfo

**中文名**: 可转债赎回和回售

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDCallPutInfo` |
| MySQL表名 | `bond_conbdcallputinfo` |
| 中文名 | 可转债赎回和回售 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 43 |
| 版本 | 1.1 |

## 表描述

1.收录可转换债券回售或赎回的相关信息。
2.包括权利描述、执行原因、行权日期、回售/赎回价格、回售/赎回金额等信息。
3.数据范围：1992-11-01 至今
4.信息来源：上交所、深交所、北交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `CBType` | 可转债类型 | number(10) | ✓ | 100.0% | 可转债类型(CBType)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到可转债类型的具... |
| 4 | `CallProtection` | 赎回/回售保护期(月) | number(18,2) | ✓ | 59.71% | 赎回/回售保护期(月)(CallProtection)：当行权类型(OpType)=101-发行人赎回权时，该字段维护赎... |
| 5 | `LastCovertDay` | 强制转股日 | date | ✓ | 0.02% |  |
| 6 | `LastCovertPrice` | 强制转股价(元) | number(19,4) | ✓ | 0.02% |  |
| 7 | `InfoPublDate` | 公告日期 | date | ✓ | 100.0% |  |
| 8 | `OpType` | 行权类型 | number(10) | ✓ | 100.0% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN ... |
| 9 | `OpTypeSecond` | 行权类型二级 | number(10) | ✓ | 100.0% | 行权类型二级(OpTypeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2063 AN... |
| 10 | `OptionMark` | 权利标识 | number(10) | ✓ | 10.65% | 权利标识(OptionMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2286 ，得到权利标... |
| 11 | `OpRemark` | 权利描述 | clob | ✓ | 13.69% |  |
| 12 | `ExpectedExerciseDate` | 权利可能行使日 | date | ✓ | 41.66% |  |
| 13 | `OpProgress` | 行权进程 | number(10) | ✓ | 100.0% | 行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程... |
| 14 | `IfOption` | 是否行权 | number(10) | ✓ | 42.4% | 是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN... |
| 15 | `EnforceReason` | 执行原因 | varchar2(2000) | ✓ | 42.41% |  |
| 16 | `CallTermStartDate` | 行权申请起始日 | date | ✓ | 5.23% |  |
| 17 | `CallTermEndDate` | 行权申请截止日 | date | ✓ | 5.23% |  |
| 18 | `CallRegDate` | 赎回登记日 | date | ✓ | 6.45% |  |
| 19 | `CommOptionDate` | 行权操作日 | date | ✓ | 17.55% |  |
| 20 | `CallPrice` | 赎回/回售价格(含税,元/张) | number(19,4) | ✓ | 25.81% |  |
| 21 | `CallPriceTaxed` | 赎回/回售价格(扣税,元/张) | number(19,4) | ✓ | 5.48% |  |
| 22 | `IfIncludeInterest` | 是否包含利息 | number(10) | ✓ | 25.78% | 是否包含利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 99... |
| 23 | `Interest` | 利息(元) | number(19,4) | ✓ | 21.36% |  |
| 24 | `LeastOpVol` | 最低操作金额(元) | number(19,4) | ✓ | 1.75% |  |
| 25 | `CallCode` | 回售/赎回代码 | varchar2(10) | ✓ | 0.68% |  |
| 26 | `CallName` | 回售/赎回简称 | varchar2(50) | ✓ | 0.69% |  |
| 27 | `CommOpApplStTime` | 行权申请受理开始时间 | varchar2(10) | ✓ | 0.13% |  |
| 28 | `CommOpApplEdTime` | 行权申请受理截止时间 | varchar2(10) | ✓ | 0.13% |  |
| 29 | `CallPieces` | 赎回/回售债券张数(张) | number(19,4) | ✓ | 11.32% |  |
| 30 | `CallVol` | 赎回/回售金额(元) | number(19,4) | ✓ | 11.32% |  |
| 31 | `CallOrPutResultPublDate` | 回售/赎回结果公告日 | date | ✓ | 3.63% |  |
| 32 | `OutstandingBDVol` | 债券剩余金额(元) | number(19,4) | ✓ | 11.11% |  |
| 33 | `AllocatingCallMonDay` | 行权后款项到账日 | date | ✓ | 11.65% |  |
| 34 | `RevokeStartDate` | 撤销起始日 | date | ✓ | 0.56% |  |
| 35 | `RevokeEndDate` | 撤销截止日 | date | ✓ | 0.56% |  |
| 36 | `ExeReachStartDate` | 触发条件满足区间起始日 | date | ✓ | 23.74% |  |
| 37 | `ExeReachEndDate` | 触发条件满足区间截止日 | date | ✓ | 34.84% |  |
| 38 | `StopExeStartDate` | 触发不行权区间起始日 | date | ✓ | 18.4% |  |
| 39 | `StopExeEndDate` | 触发不行权区间截止日 | date | ✓ | 18.49% |  |
| 40 | `TriggerRecountDay` | 触发条件重新计算日 | date | ✓ | 20.15% |  |
| 41 | `CallNoticeDate` | 强制赎回公告日 | date | ✓ | 4.9% |  |
| 42 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 43 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### CBType (可转债类型)

可转债类型(CBType)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到可转债类型的具体描述：1-常规债券，2-分离交易可转债，3-本息分离交易债券，4-可交换公司债券。

### CallProtection (赎回/回售保护期(月))

赎回/回售保护期(月)(CallProtection)：当行权类型(OpType)=101-发行人赎回权时，该字段维护赎回保护期(月)；当行权类型(OpType)=201-持有人回售权时，该字段维护回售保护期(月)。

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN (101,105,201,109,110,601)，得到行权类型的具体描述：101-发行人赎回权，105-发行人调整票面利率选择权，109-回拨选择权，110-可转债转股价格修正，201-持有人回售权，601-投资者保护条款。

### OpTypeSecond (行权类型二级)

行权类型二级(OpTypeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2063 AND DM IN (10101,10102,10501,10902,11001,20101,20102,20103,20104,20105,60101,60102,60103)，得到行权类型二级的具体描述：10101-发行人赎回权，10102-可转债到期赎回，10501-发行人调整票面利率选择权，10902-品种间回拨选择权，11001-可转债转股价格修正，20101-持有人回售权，20102-有条件回售，20103-无条件回售，20104-时点回售，20105-附加回售，60101-交叉违约，60102-控制权变更，60103-事先约束。

### OptionMark (权利标识)

权利标识(OptionMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2286 ，得到权利标识的具体描述：1001-向上调整，1002-向下调整，1003-不确定调整方向，2001-可撤销，2002-不可撤销。

### OpProgress (行权进程)

行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程的具体描述：1-发行时权利约定，2-行权提示与结果。

### IfOption (是否行权)

是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行权的具体描述：1-是，2-否。

### IfIncludeInterest (是否包含利息)

是否包含利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含利息的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 可转债赎回和回售 数据
SELECT *
FROM bond_conbdcallputinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
