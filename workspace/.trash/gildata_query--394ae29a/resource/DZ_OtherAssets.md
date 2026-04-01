# DZ_OtherAssets

**中文名**: 资产负债表附注_其他资产

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_OtherAssets` |
| MySQL表名 | `dz_otherassets` |
| 中文名 | 资产负债表附注_其他资产 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：
1.1 描述新会计准则下，上市公司在资产负债表附注中公布的投资性房产、生产性生物资产、油气资产等资产的明细情况。
1.2 对于公告原文披露的项目名称，收录在“科目名称（ItemName）”中；“科目代码（ItemCode）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：2004-12-31至今
4.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具... |
| 6 | `AssetCategory` | 资产类别 | number(10) | ✗ | 100.0% | 资产类别(AssetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND... |
| 7 | `ItemCode` | 科目代码 | number(10) | ✗ | 100.0% | 科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVAL... |
| 8 | `ItemName` | 科目名称 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `CurrencyCode` | 计价货币 | number(10) | ✓ | 49.74% | 计价货币(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 10 | `OpeningNetValue` | 净值期初金额(元) | number(19,4) | ✓ | 90.19% |  |
| 11 | `CurrentIncreaseNV` | 净值本期增加(元) | number(19,4) | ✓ | 21.98% |  |
| 12 | `CurrentDecreaseNV` | 净值本期减少(元) | number(19,4) | ✓ | 9.84% |  |
| 13 | `EndingNetValue` | 净值期末金额(元) | number(19,4) | ✓ | 99.06% |  |
| 14 | `EndingOriginalValue` | 原值期末金额(元) | number(19,4) | ✓ | 91.18% |  |
| 15 | `EndingCalculatingSum` | 期末计提金额(元) | number(19,4) | ✓ | 8.78% |  |
| 16 | `EndingAccuAmortization` | 累计摊销期末金额(元) | number(19,4) | ✓ | 86.82% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。

### AssetCategory (资产类别)

资产类别(AssetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND DM IN (13301,13302,13303)，得到资产类别的具体描述：13301-投资性房产，13302-生产性生物资产，13303-油气资产。

### ItemCode (科目代码)

科目代码(ItemCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1041 AND FVALUE IN (133,999) AND DM NOT IN (32750,32751)，得到科目代码的具体描述：13304-房屋及建筑物，13306-其他投资性房地产，13310-土地使用权，13313-特许使用权，13319-其他使用权，13330-经营权，13340-商标，13343-商誉，13350-软件，13360-专利，13370-专有技术、非专利技术、技术投资，13371-#专有技术，13373-#非专利技术，13381-未探明矿区权益，13382-探明矿区权益，13383-井及相关设施，13384-其他油气资产，13390-其他无形资产，13391-种植业，13392-畜牧养殖业，13393-林业，13394-水产业，13395-其他生产性生物资产，32761-合计特别调整，32767-合计。

### CurrencyCode (计价货币)

计价货币(CurrencyCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM = 1420，得到计价货币的具体描述：1420-人民币元。

## SQL示例

```sql
-- 查询 资产负债表附注_其他资产 数据
SELECT *
FROM dz_otherassets
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
