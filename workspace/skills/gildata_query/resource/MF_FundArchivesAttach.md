# MF_FundArchivesAttach

**中文名**: 公募基金概况附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundArchivesAttach` |
| MySQL表名 | `mf_fundarchivesattach` |
| 中文名 | 公募基金概况附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.02 |

## 表描述

1.本表主要记录了证监会基金分类、银河证券基金分类、基金运作方式、封闭期、货币基金收益分配方式等数据内容。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书、临时公告，还有证监会官网等。
4.12-国金基金分类、13-国金基金类别、15-银河基金分类（旧版分类）、56-聚源基金分类（旧版分类）自2019年起不再维护。
81-基金类型(公告)自2023年起不再维护。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 3 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 4 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `TypeCode` | 类别代码 | number(10) | ✗ | 100.0% | 类别代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 and DM n... |
| 7 | `TypeName` | 类别 | varchar2(50) | ✓ | 100.0% | TypeCode=12-国金基金分类、13-国金基金类别、56-聚源基金分类已停止维护 |
| 8 | `DataCode` | 数据代码 | number(10) | ✓ | 92.01% | 数据代码（DataCode）：与“系统常量表”中的“代码（DM）”关联，得到“数据代码”的具体描述，关联条件如下： 当T... |
| 9 | `DataName` | 数据 | varchar2(50) | ✓ | 64.42% |  |
| 10 | `DataValue` | 数值 | number(10) | ✓ | 8.08% | 数值（DataValue）：一般展示时间长度类数据，与DataName和DataCode结合使用，此时DataName一... |
| 11 | `StartDate` | 生效日期 | date | ✓ | 93.4% |  |
| 12 | `EndDate` | 取消日期 | date | ✓ | 36.17% |  |
| 13 | `Remark` | 备注说明 | varchar2(500) | ✓ | 38.82% |  |
| 14 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 15 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金的交易代码、简称等。

### TypeCode (类别代码)

类别代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 and DM not in (16,17,74,75,61,62,80,87)，得到类别代码的具体描述：10-证监会基金分类，11-晨星基金分类，12-国金基金分类，13-国金基金类别，14-运作方式(公告)，15-银河基金分类，18-银河证券分类2017版，20-基金运作方式，31-货币基金收益分配日期，32-货币基金收益分配方式，33-基金级别，35-基金伞形系列，41-基金投资类型变动，51-基金封闭期，52-基金保本期，53-定开基金封闭期，55-短期理财型基金运作周期，56-聚源基金分类(旧)，71-投资区域，72-定开基金开放期类型，73-基金持有期，76-封闭运作期(含受限开放期)，77-科创板基金，78-大集合转公募运作，79-开放频率，81-基金类型(公告)，82-基金涨跌幅限制(%)，83-MOM基金，84-公募REITs，85-北交所基金，86-创业板基金，90-个人养老金投资基金份额，91-申万宏源公募基金基础分类，92-中证REITs资产分类。

### TypeName (类别)

TypeCode=12-国金基金分类、13-国金基金类别、56-聚源基金分类已停止维护

### DataCode (数据代码)

数据代码（DataCode）：与“系统常量表”中的“代码（DM）”关联，得到“数据代码”的具体描述，关联条件如下：
当TypeCode=10，LB=1737；
当TypeCode=11，LB=1093；
当TypeCode=12，LB=1565 AND DM < 100；
当TypeCode=13，LB=1565 AND DM >= 100；
当TypeCode=14，LB=1210：DataCode 1-契约型封闭式（实际含义表示封闭式）、2-开放式、3-LOF、4-ETF；
当TypeCode=15，LB=1641；
当TypeCode=18，LB=2017；
当TypeCode=20，DataCode 1=全程开放、2=循环运作、3=全程封闭、5=开放式带固定封闭期；
当TypeCode=31，LB=1250；
当TypeCode=32，LB=1273；
当TypeCode=33，LB=1417；
当TypeCode=35，LB=1418；
当TypeCode=41，LB=1249；
当TypeCode=53，LB=2010；
当TypeCode=55，LB=1752；
当TypeCode=71，LB=1973；
当TypeCode=73，LB=2097;
当TypeCode=81，LB=1249; 
当TypeCode=72，LB=2178；
当 TypeCode=76，LB=1752，
当 TypeCode=74，DataCode 1=低风险，2=中低风险，3 =中风险 ，4=中高风险，5=高风险；
当 TypeCode=76，DataCode 365=年，30=月，1=自然日。
对于11-晨星基金分类 及 15-银河基金分类，在系统常量表的FVALUE字段，标示出常量分类是否有效：1-有效；0-失效；对于18-银河证券分类2017版，在基金分类表（MF_FundType）表可以查到基金分类的层级关系。；

### DataValue (数值)

数值（DataValue）：一般展示时间长度类数据，与DataName和DataCode结合使用，此时DataName一般表示单位。例如：当TypeCode为51时，该字段表示基金封闭期的时长，当TypeCode为53时，该字段表示定开基金封闭期的时长，当TypeCode为55时，该字段表示短期理财型基金的运作周期时长，依此类推。

## SQL示例

```sql
-- 查询 公募基金概况附表 数据
SELECT *
FROM mf_fundarchivesattach
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
