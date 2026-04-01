# LC_IntangibleAssetNew

**中文名**: 资产负债表附注_无形资产

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IntangibleAssetNew` |
| MySQL表名 | `lc_intangibleassetnew` |
| 中文名 | 资产负债表附注_无形资产 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.描述新会计准则下，上市公司无形资产的明细情况。
2.对于公告原文披露的项目名称，收录在“科目名称（ItemName）”中；“科目代码（ItemCode）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：1998-12-31至今
4.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✓ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具... |
| 6 | `ItemCode` | 科目代码 | number(10) | ✓ | 100.0% | 科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVAL... |
| 7 | `ItemName` | 科目名称 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `InitialValue` | 原值(元) | number(19,4) | ✓ | 97.73% |  |
| 9 | `OpeningBalance` | 期初金额(元) | number(19,4) | ✓ | 83.52% |  |
| 10 | `CalculatingSumStart` | 期初计提金额(元) | number(19,4) | ✓ | 0.06% |  |
| 11 | `CurrentIncrease` | 本期增加(元) | number(19,4) | ✓ | 22.76% |  |
| 12 | `IncreaseByMA` | 其中:购并增加(元) | number(19,4) | ✓ | 0.01% |  |
| 13 | `IncreaseByWriteBack` | 本期转回增加(元) | number(19,4) | ✓ | 0.03% |  |
| 14 | `IncreaseByOtherWay` | 其他增加(元) | number(19,4) | ✓ | 0.02% |  |
| 15 | `CurrentDecrease` | 本期减少(元) | number(19,4) | ✓ | 13.46% |  |
| 16 | `DecreaseByTransferredOut` | 其中:本期转出(元) | number(19,4) | ✓ | 0.86% |  |
| 17 | `DecreaseByAmortization` | 本期摊销(元) | number(19,4) | ✓ | 4.96% |  |
| 18 | `DecreaseByOtherWay` | 其他减少(元) | number(19,4) | ✓ | 0.08% |  |
| 19 | `EndingBalance` | 期末金额(元) | number(19,4) | ✓ | 99.48% |  |
| 20 | `CalculatingSumEnd` | 期末计提金额(元) | number(19,4) | ✓ | 7.97% |  |
| 21 | `AccumulatedAmortization` | 累计摊销(元) | number(19,4) | ✓ | 94.22% |  |
| 22 | `ResidualAmortizationTerm` | 剩余摊销期限 | varchar2(200) | ✓ | 4.77% |  |
| 23 | `GetWay` | 取得方式 | varchar2(200) | ✓ | 3.82% |  |
| 24 | `Remarks` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。

### ItemCode (科目代码)

科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVALUE IN (133,999) ，得到科目代码的具体描述：13304-房屋及建筑物，13306-其他投资性房地产，13310-土地使用权，13313-特许使用权，13319-其他使用权，13330-经营权，13340-商标，13343-商誉，13350-软件，13360-专利，13370-专有技术、非专利技术、技术投资，13371-#专有技术，13373-#非专利技术，13381-未探明矿区权益，13382-探明矿区权益，13383-井及相关设施，13384-其他油气资产，13390-其他无形资产，13391-种植业，13392-畜牧养殖业，13393-林业，13394-水产业，13395-其他生产性生物资产，32750-营业收入合计特别调整，32751-营业成本合计特别调整，32761-合计特别调整，32767-合计。

## SQL示例

```sql
-- 查询 资产负债表附注_无形资产 数据
SELECT *
FROM lc_intangibleassetnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
