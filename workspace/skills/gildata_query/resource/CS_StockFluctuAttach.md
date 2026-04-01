# CS_StockFluctuAttach

**中文名**: 境内股票交易公开营业部信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockFluctuAttach` |
| MySQL表名 | `cs_stockfluctuattach` |
| 中文名 | 境内股票交易公开营业部信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

内容说明：记录沪深京交易所披露的股票在交易异常波动期间证券公司交易席位的公开买卖信息
数据范围：1997-02至今
信息来源：上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 与境内股票交易公开信息表(CS_StockFluctuation)的ID关联，得到对应营业部交易的详细信息。 |
| 3 | `BSDirection` | 买卖方向 | number(10) | ✗ | 100.0% | 买卖方向(BSDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到买卖方... |
| 4 | `FluctuationRank` | 异动排名 | number(10) | ✗ | 100.0% |  |
| 5 | `SalesDepartmentName` | 营业部名称 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `BOCode` | 营业部编号 | number(10) | ✓ | 99.82% | 营业部编号(BOCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联... |
| 7 | `SecuCoBelonged` | 营业部所属券商 | varchar2(80) | ✓ | 99.92% |  |
| 8 | `SecuCoBelongedCode` | 营业部所属券商编号 | number(10) | ✓ | 99.92% | 营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编... |
| 9 | `TotalBuySaleSum` | 买卖合计金额(元) | number(19,4) | ✓ | 99.87% |  |
| 10 | `BuySum` | 买入金额(元) | number(19,4) | ✓ | 81.08% |  |
| 11 | `SellSum` | 卖出金额(元) | number(19,4) | ✓ | 81.24% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

与境内股票交易公开信息表(CS_StockFluctuation)的ID关联，得到对应营业部交易的详细信息。

### BSDirection (买卖方向)

买卖方向(BSDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到买卖方向的具体描述：10-买卖金额，11-买入金额，13-卖出金额。

### BOCode (营业部编号)

营业部编号(BOCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部的具体信息；与“企业数据-名称更改(LC_NameHistorical)”中的企业编号(CompanyCode)关联，得到营业部名称变革信息，不同历史阶段可能存在营业部同名情况，需结合名称更改判断是否为同一营业部。

### SecuCoBelongedCode (营业部所属券商编号)

营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到所属券商的具体信息；与“企业数据-名称更改(LC_NameHistorical)”中的企业编号(CompanyCode)关联，得到所属券商名称变革信息。

## SQL示例

```sql
-- 查询 境内股票交易公开营业部信息 数据
SELECT *
FROM cs_stockfluctuattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
