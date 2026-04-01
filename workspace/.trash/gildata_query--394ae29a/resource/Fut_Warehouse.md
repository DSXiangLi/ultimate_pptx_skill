# Fut_Warehouse

**中文名**: 国内商品期货交割仓库

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_Warehouse` |
| MySQL表名 | `fut_warehouse` |
| 中文名 | 国内商品期货交割仓库 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 36 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录以品种维度划分的国内三大期货交易所的交割仓库、厂库和车船板的信息，包括仓库名称、存货地址、联系人、联系方式等内容。
2.数据范围：2001年至今
3.信息来源：上海期货交易所（上海国际能源中心）、大连商品期货交易所、郑州商品期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `Exchange` | 交易所 | number(10) | ✗ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 4 | `InvolvedPlate` | 涉及概念板块 | number(10) | ✓ | 67.08% | 涉及概念板块(InvolvedPlate)与(CT_SystemConst)表中的DM字段关联，令LB = 2317，得... |
| 5 | `VarietyInnerCode` | 品种内部编码 | number(10) | ✗ | 100.0% | 品种内部编码(VarietyInnerCode)与期货品种(Fut_FuturesContract)的(Contract... |
| 6 | `WarehouseType` | 交割仓库类型 | number(10) | ✗ | 100.0% | 交割仓库类型(WarehouseType)与(CT_SystemConst)表中的DM字段关联，令LB = 2316，得... |
| 7 | `WarehouseCode` | 仓库编号 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `Warehouse` | 仓库全称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `WarehouseAbbr` | 仓库简称 | varchar2(100) | ✓ | 75.89% |  |
| 10 | `BranchWarehouse` | 分库名称 | varchar2(200) | ✓ | 6.85% |  |
| 11 | `InventoryAddr` | 存货地址 | varchar2(200) | ✓ | 73.58% |  |
| 12 | `OfficeAddr` | 办公地址 | varchar2(200) | ✓ | 49.64% |  |
| 13 | `State` | 省份 | number(10) | ✓ | 100.0% | 省份(State)与(LC_AreaCode)表中的AreaInnerCode字段关联，令IfEffected = 1 ... |
| 14 | `Contactman` | 联系人 | varchar2(200) | ✓ | 99.89% |  |
| 15 | `Tel` | 电话 | varchar2(200) | ✓ | 50.21% |  |
| 16 | `MobilePhone` | 手机 | varchar2(200) | ✓ | 90.63% |  |
| 17 | `Email` | 邮箱 | varchar2(200) | ✓ | 15.66% |  |
| 18 | `Fax` | 传真 | varchar2(200) | ✓ | 41.09% |  |
| 19 | `PostCode` | 邮编 | varchar2(6) | ✓ | 76.1% |  |
| 20 | `DestinationStation` | 到达站(港) | varchar2(200) | ✓ | 57.39% |  |
| 21 | `WarehousePAD` | 仓库升贴水(元/吨) | number(18,4) | ✓ | 70.95% |  |
| 22 | `WarehousePADDesc` | 仓库升贴水(描述) | varchar2(200) | ✓ | 10.44% |  |
| 23 | `DeliverySpeed` | 日发货速度(吨/天) | number(18,4) | ✓ | 36.43% |  |
| 24 | `MaxSWR` | 标准仓单最大量(吨) | number(18,4) | ✓ | 24.11% |  |
| 25 | `StorageCapacity` | 最低保障库容(万吨) | number(18,4) | ✓ | 23.79% |  |
| 26 | `WarehouseQuota` | 厂库额度(万吨) | number(18,4) | ✓ | 7.88% |  |
| 27 | `BenchOrNon` | 基准非基准库 | varchar2(200) | ✓ | 41.44% |  |
| 28 | `DeliveryState` | 所属交割区域 | varchar2(100) | ✓ | 2.06% |  |
| 29 | `DeliveryArea` | 交割专区 | varchar2(200) | ✓ | 9.09% |  |
| 30 | `Remark` | 备注 | clob | ✓ | 47.73% |  |
| 31 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 32 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 33 | `EndDate` | 截止日期 | date | ✓ | 20.53% |  |
| 34 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 35 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 36 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN(10,11,13,15,17,20)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所，20-中国金融期货交易所。

### InvolvedPlate (涉及概念板块)

涉及概念板块(InvolvedPlate)与(CT_SystemConst)表中的DM字段关联，令LB = 2317，得到涉及概念板块的具体描述：1-贵金属，2-有色金属，3-煤焦钢矿，4-非金属建材，5-能源，6-化工，7-油脂油料，8-软商品，9-谷物，10-农副产品，11-基本金属，12-农产品，13-能源化工，14-国债期货，15-航运指数，16-股指期货。

### VarietyInnerCode (品种内部编码)

品种内部编码(VarietyInnerCode)与期货品种(Fut_FuturesContract)的(ContractInnerCode)字段关联，得到该期货品种的基础信息。

### WarehouseType (交割仓库类型)

交割仓库类型(WarehouseType)与(CT_SystemConst)表中的DM字段关联，令LB = 2316，得到交割仓库类型的具体描述：1-交割仓库，2-交割厂库，3-车板交割场所，4-保税交割仓库，5-集团交割仓库，6-直库，7-分库，8-金库。

### State (省份)

省份(State)与(LC_AreaCode)表中的AreaInnerCode字段关联，令IfEffected = 1 AND FirstLevelCode = 1000，得到省份的具体描述：144110000-北京市，144120000-天津市，144130000-河北省，144140000-山西省，144150000-内蒙古自治区，144160000-辽宁省，144170000-吉林省，144180000-黑龙江省，144190000-上海市，144200000-江苏省，144210000-浙江省，144220000-安徽省，144230000-福建省，144240000-江西省，144250000-山东省，144260000-河南省，144270000-湖北省，144280000-湖南省，144290000-广东省，144300000-广西壮族自治区，144310000-海南省，144320000-重庆市，144330000-四川省，144340000-贵州省，144350000-云南省，144360000-西藏自治区，144370000-陕西省，144380000-甘肃省，144390000-青海省，144400000-宁夏回族自治区，144410000-新疆维吾尔自治区，144420000-中国台湾省，144430000-中国香港特别行政区，144440000-中国澳门特别行政区。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 国内商品期货交割仓库 数据
SELECT *
FROM fut_warehouse
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
