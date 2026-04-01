# Bond_MunicipalAreaInfo

**中文名**: 城投行政级别及区域信息表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_MunicipalAreaInfo` |
| MySQL表名 | `bond_municipalareainfo` |
| 中文名 | 城投行政级别及区域信息表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 城投专题信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 30 |
| 版本 | 1.01 |

## 表描述

1.本表收录了城投平台的实际控制人、行政级别及其所属区域等信息。
2.区域主体：共有两种方法来确定城投的区域信息，1）按城投的最终实控人来确定城投的区域信息 2）按城投平台业务所在地来确定城投的区域信息。区域主体类型=1时，代表行政级别、相关区域等信息是通过城投实控人来确定的。区域主体类型=2时，代表行政级别、相关区域等信息是通过城投业务实际发生地来确定的。
3.是否有效：是否有效字段标识了该条记录的是否是该城投的最新区域信息，是否有效为否的是历史区域信息。截止日期是实控人/区域信息的变更时间。
4.数据范围：聚源口径城投、所有中债样本券城投（含历史的记录）

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 城投公司代码 | number(10) | ✗ | 100.0% | 城投公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compan... |
| 3 | `CompanyName` | 城投公司名称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `ClasEntityType` | 区域主体类型 | number(10) | ✗ | 100.0% | 1-实际控制人 2-城投平台 |
| 5 | `EndDate` | 截止日期 | date | ✓ | 99.6% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 7 | `Grade` | 行政级别 | number(10) | ✓ | 99.77% | 行政级别(Grade)与(CT_SystemConst)表中的DM字段关联，令LB = 2409，得到行政级别的具体描述... |
| 8 | `GradeSecond` | 行政级别细分 | number(10) | ✓ | 99.77% | 行政级别细分(GradeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2410 AND... |
| 9 | `AreaCode` | 所属地区代码 | number(10) | ✓ | 96.32% | 所属地区代码（AreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerC... |
| 10 | `Area` | 所属地区名称 | varchar2(100) | ✓ | 99.98% |  |
| 11 | `AreaLevelMark` | 特殊地区标识 | number(10) | ✓ | 99.96% | 1-省市县   2-直辖市    3-国家级新区  |
| 12 | `FirstAreaCode` | 省/直辖市/国家级新区代码 | number(10) | ✓ | 99.96% | 省/直辖市/国家级新区代码（FirstAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编... |
| 13 | `FirstArea` | 省/直辖市/国家级新区 | varchar2(100) | ✓ | 99.96% |  |
| 14 | `SecdAreaCode` | 副省级自治州代码 | number(10) | ✓ | 0.05% | 副省级自治州代码（SecdAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（Area... |
| 15 | `SecdArea` | 副省级自治州 | varchar2(100) | ✓ | 0.05% |  |
| 16 | `ThirdAreaCode` | 市代码 | number(10) | ✓ | 85.25% | 市代码（ThirdAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInne... |
| 17 | `ThirdArea` | 市 | varchar2(100) | ✓ | 85.25% |  |
| 18 | `ForthAreaCode` | 区县代码 | number(10) | ✓ | 51.96% | 区县代码（ForthAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInn... |
| 19 | `ForthArea` | 区县 | varchar2(100) | ✓ | 51.96% |  |
| 20 | `Town` | 镇 | varchar2(100) | ✓ | 0.18% |  |
| 21 | `Street` | 街道 | varchar2(100) | ✓ | 0.08% |  |
| 22 | `Zone` | 园区 | varchar2(100) | ✓ | 10.65% |  |
| 23 | `ZoneCode` | 园区代码 | number(10) | ✓ | 6.26% | 园区代码（ZoneCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCod... |
| 24 | `ZoneType` | 所属园区类型 | number(10) | ✓ | 9.49% | 所属园区类型(ZoneType)与(CT_SystemConst)表中的DM字段关联，令LB = 2169，得到所属园区... |
| 25 | `ControllerCode` | 实际控制人代码 | number(10) | ✗ | 100.0% | 实际控制人代码（ControllerCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Co... |
| 26 | `ControllerName` | 实际控制人名称 | varchar2(100) | ✓ | 100.0% |  |
| 27 | `ControllerType` | 实际控制人类型 | number(10) | ✓ | 95.43% | 实际控制人类型(ControllerType)与(CT_SystemConst)表中的DM字段关联，令LB = 2167... |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 30 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (城投公司代码)

城投公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### ClasEntityType (区域主体类型)

1-实际控制人 2-城投平台

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

### Grade (行政级别)

行政级别(Grade)与(CT_SystemConst)表中的DM字段关联，令LB = 2409，得到行政级别的具体描述：1-省级行政区，2-副省级行政区，3-地级行政区，4-区县级行政区，5-其它。

### GradeSecond (行政级别细分)

行政级别细分(GradeSecond)与(CT_SystemConst)表中的DM字段关联，令LB = 2410 AND DM NOT IN (502)，得到行政级别细分的具体描述：101-省，102-自治区，103-直辖市，201-副省级省会，202-计划单列市，203-副省级自治州，301-省会，302-地级市，303-自治州，304-盟，305-地区，401-县级市，402-县，403-自治县，404-旗，405-自治旗，406-林区，407-特区，408-市辖区，501-园区，503-国家级新区，504-新疆生产建设兵团，505-村镇街道。

### AreaCode (所属地区代码)

所属地区代码（AreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码、中文名称等。

### AreaLevelMark (特殊地区标识)

1-省市县   2-直辖市    3-国家级新区 

### FirstAreaCode (省/直辖市/国家级新区代码)

省/直辖市/国家级新区代码（FirstAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码、中文名称等。

### SecdAreaCode (副省级自治州代码)

副省级自治州代码（SecdAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码、中文名称等。

### ThirdAreaCode (市代码)

市代码（ThirdAreaCode）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码、中文名称等。

## SQL示例

```sql
-- 查询 城投行政级别及区域信息表 数据
SELECT *
FROM bond_municipalareainfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
