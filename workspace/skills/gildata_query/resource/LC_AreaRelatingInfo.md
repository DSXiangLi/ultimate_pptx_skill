# LC_AreaRelatingInfo

**中文名**: 国家城市相关信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AreaRelatingInfo` |
| MySQL表名 | `lc_arearelatinginfo` |
| 中文名 | 国家城市相关信息 |
| 路径 | 聚源新版数据库 > 常量库 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

内容说明：本表以国家城市代码表(LC_AreaCode)中，各个国家、城市、地区为中心，记录该国家、城市、地区的一些关联信息。
数据范围：包含电话区号、所属地理分区、以及ISO披露的标准AlphaCode等
信息来源：ISO、国家标准化管理委员会等相关发布网站和统计网站

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `AreaInnerCode` | 地区内部编码 | number(10) | ✗ | 100.0% | 地区内部编码(AreaInnerCode)与(LC_AreaCode)表中的AreaInnerCode字段关联，得到类别... |
| 3 | `Type` | 类别 | number(10) | ✗ | 100.0% | 类别(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 2198，得到类别的具体描述：10-国... |
| 4 | `AreaValue` | 地区数值 | number(10) | ✓ | 23.9% | 当类别(Type) in  (1000,8002,2003)时，地区数值(AreaValue)与(LC_AreaCode... |
| 5 | `AreaDate` | 地区数据 | varchar2(100) | ✓ | 76.09% | 当类别(Type) not in (1000,8002,2003) 时，地区数据(AreaDate)为具体类别的信息。 |
| 6 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 7 | `EndDate` | 截止日期 | date | ✓ | 0.53% |  |
| 8 | `Remark` | 备注 | varchar2(500) | ✓ | 17.58% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AreaInnerCode (地区内部编码)

地区内部编码(AreaInnerCode)与(LC_AreaCode)表中的AreaInnerCode字段关联，得到类别的具体描述

### Type (类别)

类别(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 2198，得到类别的具体描述：10-国际电话区号，20-中国电话区号，1000-中国地理区划，2001-Alpha-2(ISO)，2002-Alpha-3(ISO)，2003-国家所属洲，3000-中国地区邮编，3001-中国清算中心代码(1992)，8001-经济区所属城市，8002-公司主营构成地区划分关系，9000-地区别名。

### AreaValue (地区数值)

当类别(Type) in  (1000,8002,2003)时，地区数值(AreaValue)与(LC_AreaCode)表中的AreaInnerCode字段关联，得到该类别的具体信息。

### AreaDate (地区数据)

当类别(Type) not in (1000,8002,2003) 时，地区数据(AreaDate)为具体类别的信息。

## SQL示例

```sql
-- 查询 国家城市相关信息 数据
SELECT *
FROM lc_arearelatinginfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
