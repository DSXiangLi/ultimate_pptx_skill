# Bond_BDCreditGrading

**中文名**: 债项信用评级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BDCreditGrading` |
| MySQL表名 | `bond_bdcreditgrading` |
| 中文名 | 债项信用评级 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券评级信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 25 |
| 版本 | 1.07 |

## 表描述

1.涵盖券种：短期融资券、可转换债券、企业债券、金融债券、金融次级债、银行间和交易所资产支持证券、混合资本债券等。
2.包含债券的长期评级、短期评级。
3.涵盖所有历史变动记录。
4.数据范围：1996-1-15 至今
5.信息来源：中债登、货币网、上清所、上交所、深交所、评级公司官网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 99.46% |  |
| 5 | `RateMethod` | 债券评级方式 | number(10) | ✓ | 100.0% | 债券评级方式(RateMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1856 and ... |
| 6 | `CRDate` | 评级日期 | date | ✗ | 100.0% |  |
| 7 | `CRAsCode` | 评级机构代码 | number(10) | ✗ | 100.0% | 评级机构代码（CRAsCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCo... |
| 8 | `CRAsName` | 评级机构名称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `CRTypeCode` | 评级类别 | number(10) | ✓ | 100.0% | 评级类别(CRTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1397 AND DM... |
| 10 | `CRCode` | 信用级别代码 | number(10) | ✗ | 100.0% | 信用级别代码（CRCode）：与“系统常量表”中的“常量代码（DM）”关联，“LB”根据“评级类别（CRTypeCode... |
| 11 | `CRDesc` | 信用级别描述 | varchar2(50) | ✓ | 100.0% |  |
| 12 | `CRSystem` | 评级体系 | number(10) | ✓ | 100.0% | 评级体系(CRSystem)与(CT_SystemConst)表中的DM字段关联，令LB = 1002 AND DM I... |
| 13 | `CRAnticipate` | 评级展望 | varchar2(100) | ✓ | 3.85% |  |
| 14 | `CROutlook` | 展望 | number(10) | ✓ | 3.85% | 展望(CROutlook)与(CT_SystemConst)表中的DM字段关联，令LB = 1704 AND DM IN... |
| 15 | `CRStatus` | 评级状态 | number(10) | ✓ | 100.0% | 评级状态(CRStatus)：评级公司公告披露撤销评级，评级状态更新为失效。与(系统常量表)中的DM字段关联，令LB =... |
| 16 | `ChangeReson` | 评级状态变更说明 | varchar2(500) | ✓ | 0.01% |  |
| 17 | `CRWish` | 评级意愿 | number(10) | ✓ | 100.0% | 评级意愿(CRWish)与(CT_SystemConst)表中的DM字段关联，令LB = 2043，得到评级意愿的具体描... |
| 18 | `RatingEffectiveEndDate` | 评级有效期截止日期 | date | ✓ | 7.14% |  |
| 19 | `LastCRDate` | 上次评级日期 | date | ✓ | 68.29% |  |
| 20 | `LastCRCode` | 上次评级代码 | number(10) | ✓ | 68.29% |  |
| 21 | `LastCRDesc` | 上次评级描述 | varchar2(50) | ✓ | 68.29% |  |
| 22 | `CRChange` | 评级变动方向 | varchar2(10) | ✓ | 68.29% |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (债券内部编码)

债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### RateMethod (债券评级方式)

债券评级方式(RateMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1856 and DM IN (1,2)，得到债券评级方式的具体描述：1-首次评级，2-跟踪评级。

### CRAsCode (评级机构代码)

评级机构代码（CRAsCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到评级机构的具体名称、基本信息等。

### CRTypeCode (评级类别)

评级类别(CRTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1397 AND DM IN (1,2)，得到评级类别的具体描述：1-证券短期，2-证券长期。

### CRCode (信用级别代码)

信用级别代码（CRCode）：与“系统常量表”中的“常量代码（DM）”关联，“LB”根据“评级类别（CRTypeCode）”来确定。
当评级类别（CRTypeCode） = 1 时，令“LB = 1407”，得到证券的短期信用评级描述：
99- A-1+，95- A-1，90- A-1-，85- A-2，75- A-3，65- B，55- C，45- D；
       当评级类别（CRTypeCode） = 2 时，令“LB IN (1372,1704)”，得到证券的长期信用评级描述 (LB=1372)：1000- AAA+，
999- AAA，990- AAA-，980- AA+，970- AA，960- AA-，950- A+，940- A，930- A-，899- BBB+，895- BBB，891- BBB-，880-BB+，870- BB，860-BB-，850-B+，840- B，830- B-，799- CCC，770- CC，760- C，740- D;   (LB = 1704 AND (DM < 200 OR DM IN (401,405,407)))：
101- Aaa，102-Aa1，103- Aa2，104- Aa3 等。

### CRSystem (评级体系)

评级体系(CRSystem)与(CT_SystemConst)表中的DM字段关联，令LB = 1002 AND DM IN (1,2)，得到评级体系的具体描述：1-国内，2-国际。

### CROutlook (展望)

展望(CROutlook)与(CT_SystemConst)表中的DM字段关联，令LB = 1704 AND DM IN (1201,1202,1203,1204,1205,1206,1207,1208,1209)，得到展望的具体描述：1201-正面，1202-稳定，1203-负面，1204-待定，1205-RUR(U)，1206-观望，1207-列入观察(上调)，1208-列入观察(下调)，1209-列入观察(不确定)。

### CRStatus (评级状态)

评级状态(CRStatus)：评级公司公告披露撤销评级，评级状态更新为失效。与(系统常量表)中的DM字段关联，令LB = 1422，得到评级状态的具体描述：1-正常，3-暂时失效。

### CRWish (评级意愿)

评级意愿(CRWish)与(CT_SystemConst)表中的DM字段关联，令LB = 2043，得到评级意愿的具体描述：1-主动评级，2-委托评级。

## SQL示例

```sql
-- 查询 债项信用评级 数据
SELECT *
FROM bond_bdcreditgrading
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
