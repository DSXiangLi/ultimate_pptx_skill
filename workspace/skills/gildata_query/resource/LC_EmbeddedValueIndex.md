# LC_EmbeddedValueIndex

**中文名**: 保险公司内含价值分析指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_EmbeddedValueIndex` |
| MySQL表名 | `lc_embeddedvalueindex` |
| 中文名 | 保险公司内含价值分析指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 季更新 |
| 字段数量 | 23 |
| 版本 | 1.01 |

## 表描述

1.根据报告期公布的数据进行内含价值的分析与预测，以反映保险公司内含价值相关指标的纵比分析、同比分析。
2.仅收录保险公司在报告期末未调整的合并报表。
3.该表中各科目的单位均为人民币元。
4.数据范围：2005-12-31至今
5.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 5 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `EmbeddedValuePS` | 每股总内含价值 | number(19,4) | ✓ | 93.14% | 每股总内含价值（EmbeddedValuePS）=集团内含价值/报告期末总股本 |
| 8 | `EmbeddedValuePSLife` | 每股寿险业务内含价值 | number(19,4) | ✓ | 90.29% | 每股寿险业务内含价值（EmbeddedValuePSLife）=集团应占寿险业务内含价值/报告期末总股本 |
| 9 | `EmbeddedValuePSGeneral` | 每股非寿险业务内含价值 | number(19,4) | ✓ | 90.29% | 每股非寿险业务内含价值（EmbeddedValuePSGeneral）=集团应占非寿险业务内含价值/报告期末总股本 |
| 10 | `NewBusinessValuePS` | 每股新业务价值 | number(19,4) | ✓ | 67.43% | 每股新业务价值（NewBusinessValuePS）=集团应占新业务价值/报告期末总股本 |
| 11 | `ANAVPS` | 每股调整净资产价值 | number(19,4) | ✓ | 86.29% | 每股调整净资产价值（ANAVPS）=集团经调整净资产价值/报告期末总股本 |
| 12 | `VIFBPS` | 每股有效业务价值 | number(19,4) | ✓ | 93.14% | 每股有效业务价值（VIFBPS）=集团应占有效业务价值/报告期末总股本 |
| 13 | `EmbeddedValueGR` | 集团内含价值增长率(%) | number(18,6) | ✓ | 92.0% | 集团内含价值增长率（EmbeddedValueGR）=（本期集团内含价值/上年同期集团内含价值-1）*100；1：只计算... |
| 14 | `EVOfInforceBusinessGR` | 集团有效业务价值增长率(%) | number(18,6) | ✓ | 88.0% | 集团有效业务价值增长率（EVOfInforceBusinessGR）=（本期应占有效业务价值/上年同期应占有效业务价值-... |
| 15 | `NewBusinessValueGR` | 新业务价值增长率(%) | number(18,6) | ✓ | 61.14% | 新业务价值增长率（NewBusinessValueGR）=（本期应占新业务价值/上年同期应占新业务价值-1）*100；1... |
| 16 | `LifeVIFBGR` | 寿险有效业务内含价值增长率(%) | number(18,6) | ✓ | 88.57% | 寿险有效业务内含价值增长率（LifeVIFBGR）=（本期集团应占寿险业务内含价值/上年同期集团应占寿险业务内含价值-1... |
| 17 | `LifeEVRatio` | 寿险业务内含价值占比(%) | number(18,6) | ✓ | 95.43% | 寿险业务内含价值占比（LifeEVRatio）=（集团应占寿险业务内含价值/集团内含价值）*100% |
| 18 | `GeneralEVRatio` | 非寿险业务内含价值占比(%) | number(18,6) | ✓ | 95.43% | 非寿险业务内含价值占比（GeneralEVRatio）=（集团应占非寿险业务内含价值/集团内含价值）*100% |
| 19 | `ANAVRatio` | 调整净资产价值占比(%) | number(18,6) | ✓ | 89.14% | 调整净资产价值占比（ANAVRatio）=（集团经调整净资产价值/集团内含价值）*100% |
| 20 | `VIFBRatio` | 有效业务价值占比(%) | number(18,6) | ✓ | 96.0% | 有效业务价值占比（VIFBRatio）=（集团应占有效业务价值/集团内含价值）*100% |
| 21 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### EmbeddedValuePS (每股总内含价值)

每股总内含价值（EmbeddedValuePS）=集团内含价值/报告期末总股本

### EmbeddedValuePSLife (每股寿险业务内含价值)

每股寿险业务内含价值（EmbeddedValuePSLife）=集团应占寿险业务内含价值/报告期末总股本

### EmbeddedValuePSGeneral (每股非寿险业务内含价值)

每股非寿险业务内含价值（EmbeddedValuePSGeneral）=集团应占非寿险业务内含价值/报告期末总股本

### NewBusinessValuePS (每股新业务价值)

每股新业务价值（NewBusinessValuePS）=集团应占新业务价值/报告期末总股本

### ANAVPS (每股调整净资产价值)

每股调整净资产价值（ANAVPS）=集团经调整净资产价值/报告期末总股本

### VIFBPS (每股有效业务价值)

每股有效业务价值（VIFBPS）=集团应占有效业务价值/报告期末总股本

### EmbeddedValueGR (集团内含价值增长率(%))

集团内含价值增长率（EmbeddedValueGR）=（本期集团内含价值/上年同期集团内含价值-1）*100；1：只计算年报数据中的该项指标；2：若“上年同期集团内含价值”为负时，结果填列为空值。

### EVOfInforceBusinessGR (集团有效业务价值增长率(%))

集团有效业务价值增长率（EVOfInforceBusinessGR）=（本期应占有效业务价值/上年同期应占有效业务价值-1）*100；1：只计算年报数据中的该项指标；2：若“上年同期应占有效业务价值”为负时，结果填列为空值。

## SQL示例

```sql
-- 查询 保险公司内含价值分析指标 数据
SELECT *
FROM lc_embeddedvalueindex
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
