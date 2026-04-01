# LC_FixedAssetsDepreciation

**中文名**: 资产负债表附注_固定资产及折旧明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_FixedAssetsDepreciation` |
| MySQL表名 | `lc_fixedassetsdepreciation` |
| 中文名 | 资产负债表附注_固定资产及折旧明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.描述新会计准则下，上市公司固定资产及折旧的明细情况，包括固定资产的原值、累计折旧、减值准备、账面价值、净值等各项的期初、期间变化和期末数据。
2.对于公告原文披露的项目名称，收录在“固定资产名称（FixedAssetName）”中；“固定资产分类（FixedAssetType）”则对披露的科目进行了归类，以便于横向比较。
3.数据范围：2000-12-31至今
4.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✓ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具... |
| 6 | `FixedAssetName` | 固定资产名称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `FixedAssetType` | 固定资产分类 | number(10) | ✓ | 100.0% | 固定资产分类(FixedAssetType)与(CT_SystemConst)表中的DM字段关联，令LB = 2209 ... |
| 8 | `FixedAssetNo` | 序号 | number(10) | ✓ | 100.0% | 序号（FixedAssetNo）：本字段描述各固定资产在公告原文上的排列序号，以方便展示。 |
| 9 | `OpeningOriginalCost` | 原值期初数(元) | number(19,4) | ✓ | 98.88% |  |
| 10 | `CurrentIncreaseOC` | 原值本期增加(元) | number(19,4) | ✓ | 90.74% |  |
| 11 | `CurrentDecreaseOC` | 原值本期减少(元) | number(19,4) | ✓ | 99.64% |  |
| 12 | `EndingOriginalCost` | 原值期末数(元) | number(19,4) | ✓ | 99.57% |  |
| 13 | `OpeningAccuDepreciation` | 累计折旧期初数(元) | number(19,4) | ✓ | 98.44% |  |
| 14 | `CurrentIncreaseAD` | 累计折旧本期增加(元) | number(19,4) | ✓ | 98.88% |  |
| 15 | `CurrentDecreaseAD` | 累计折旧本期减少(元) | number(19,4) | ✓ | 99.26% |  |
| 16 | `EndingAccuDepreciation` | 累计折旧期末数(元) | number(19,4) | ✓ | 99.22% |  |
| 17 | `OpeningDepreReserves` | 减值准备期初数(元) | number(19,4) | ✓ | 19.59% |  |
| 18 | `CurrentIncreaseDR` | 减值准备本期增加(元) | number(19,4) | ✓ | 10.09% |  |
| 19 | `CurrentDecreaseDR` | 减值准备本期减少(元) | number(19,4) | ✓ | 11.73% |  |
| 20 | `EndingDepreReserves` | 减值准备期末数(元) | number(19,4) | ✓ | 20.07% |  |
| 21 | `OpeningBookValue` | 账面价值期初数(元) | number(19,4) | ✓ | 98.79% |  |
| 22 | `CurrentIncreaseBV` | 账面价值本期增加(元) | number(19,4) | ✓ | 48.1% |  |
| 23 | `CurrentDecreaseBV` | 账面价值本期减少(元) | number(19,4) | ✓ | 23.29% |  |
| 24 | `EndingBookValue` | 账面价值期末数(元) | number(19,4) | ✓ | 99.44% |  |
| 25 | `OpeningNetValue` | 净值期初数(元) | number(19,4) | ✓ | 98.88% |  |
| 26 | `CurrentIncreaseNV` | 净值本期增加(元) | number(19,4) | ✓ | 47.8% |  |
| 27 | `CurrentDecreaseNV` | 净值本期减少(元) | number(19,4) | ✓ | 23.0% |  |
| 28 | `EndingNetValue` | 净值期末数(元) | number(19,4) | ✓ | 99.58% |  |
| 29 | `Remarks` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整，5-专项合并调整，6-专项合并未调整。

### FixedAssetType (固定资产分类)

固定资产分类(FixedAssetType)与(CT_SystemConst)表中的DM字段关联，令LB = 2209 AND FVALUE IN (1,9)，得到固定资产分类的具体描述：10010-土地、房屋及建筑物，10020-路桥及构筑物，11010-机器机械设备，11020-运输设备，11030-电气设备，11040-电子设备，11050-计算机及辅助设备，11060-通讯设备，11070-仪器仪表、计量标准器具及量具、衡器，11080-办公设备，12010-文艺体育设备，12020-航空航天工业专用设备，13010-图书文物及陈列品，14010-家具用具，15010-经营租赁租出设备，15020-融资租入固定资产，16010-其他固定资产，99998-合计特别调整，99999-合计。

### FixedAssetNo (序号)

序号（FixedAssetNo）：本字段描述各固定资产在公告原文上的排列序号，以方便展示。

## SQL示例

```sql
-- 查询 资产负债表附注_固定资产及折旧明细 数据
SELECT *
FROM lc_fixedassetsdepreciation
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
