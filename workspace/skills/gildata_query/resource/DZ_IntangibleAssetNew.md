# DZ_IntangibleAssetNew

**中文名**: 资产负债表附注_无形资产

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_IntangibleAssetNew` |
| MySQL表名 | `dz_intangibleassetnew` |
| 中文名 | 资产负债表附注_无形资产 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 27 |
| 版本 | 1 |

## 表描述

1.内容说明：
1.1 描述新会计准则下，上市公司无形资产的明细情况。
1.2 对于公告原文披露的项目名称，收录在“科目名称（ItemName）”中；“科目代码（ItemCode）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：1998-12-31至今
4.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具... |
| 6 | `ItemCode` | 科目代码 | number(10) | ✗ | 100.0% | 科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVAL... |
| 7 | `ItemName` | 科目名称 | varchar2(200) | ✗ | 100.0% |  |
| 8 | `InitialValue` | 原值(元) | number(19,4) | ✓ | 97.8% |  |
| 9 | `OpeningBalance` | 期初金额(元) | number(19,4) | ✓ | 83.91% |  |
| 10 | `CalculatingSumStart` | 期初计提金额(元) | number(19,4) | ✓ | 0.06% |  |
| 11 | `CurrentIncrease` | 本期增加(元) | number(19,4) | ✓ | 23.67% |  |
| 12 | `IncreaseByMA` | 其中:购并增加(元) | number(19,4) | ✓ | 0.01% |  |
| 13 | `IncreaseByWriteBack` | 本期转回增加(元) | number(19,4) | ✓ | 0.03% |  |
| 14 | `IncreaseByOtherWay` | 其他增加(元) | number(19,4) | ✓ | 0.02% |  |
| 15 | `CurrentDecrease` | 本期减少(元) | number(19,4) | ✓ | 13.16% |  |
| 16 | `DecreaseByTransferredOut` | 其中:本期转出(元) | number(19,4) | ✓ | 0.83% |  |
| 17 | `DecreaseByAmortization` | 本期摊销(元) | number(19,4) | ✓ | 4.79% |  |
| 18 | `DecreaseByOtherWay` | 其他减少(元) | number(19,4) | ✓ | 0.08% |  |
| 19 | `EndingBalance` | 期末金额(元) | number(19,4) | ✓ | 99.44% |  |
| 20 | `CalculatingSumEnd` | 期末计提金额(元) | number(19,4) | ✓ | 7.84% |  |
| 21 | `AccumulatedAmortization` | 累计摊销(元) | number(19,4) | ✓ | 94.38% |  |
| 22 | `ResidualAmortizationTerm` | 剩余摊销期限 | varchar2(200) | ✓ | 4.6% |  |
| 23 | `GetWay` | 取得方式 | varchar2(200) | ✓ | 3.69% |  |
| 24 | `Remarks` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 25 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。

### ItemCode (科目代码)

科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVALUE IN (133,999) AND DM NOT IN (13306,13381,13382,13383,13384,13390,13391,13392,13393,13394,13395,32750,32751)，得到科目代码的具体描述：13304-房屋及建筑物，13310-土地使用权，13313-特许使用权，13319-其他使用权，13330-经营权，13340-商标，13343-商誉，13350-软件，13360-专利，13370-专有技术、非专利技术、技术投资，13371-#专有技术，13373-#非专利技术，32761-合计特别调整，32767-合计。

## SQL示例

```sql
-- 查询 资产负债表附注_无形资产 数据
SELECT *
FROM dz_intangibleassetnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
