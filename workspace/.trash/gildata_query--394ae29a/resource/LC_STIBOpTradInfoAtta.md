# LC_STIBOpTradInfoAtta

**中文名**: 科创板交易所日公开信息附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBOpTradInfoAtta` |
| MySQL表名 | `lc_stiboptradinfoatta` |
| 中文名 | 科创板交易所日公开信息附表 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：收录交易所公布的，触发日收盘价涨跌幅达到15％、日振幅达到30%、日换手率达到30％ 等各类披露条件的科创板成交前五名的营业部信息以及成交明细等。
2.数据范围：证券上市之日-至今
3.信息来源：上海证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 与科创板交易所日公开信息（LC_STIBOpTradInfo）表的ID关联，得到对应异动类型的详细信息。 |
| 3 | `ReportArea` | 统计方式 | number(10) | ✗ | 100.0% | 统计方式(ReportArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式... |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `SalesDepartmentName` | 营业部名称 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `BOCode` | 营业部编号 | number(10) | ✓ | 100.0% | 营业部编号(BOCode)：与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关... |
| 7 | `SecuCoBelongedCode` | 营业部所属券商编号 | number(10) | ✓ | 100.0% | 营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编... |
| 8 | `SecuCoBelonged` | 营业部所属券商 | varchar2(80) | ✓ | 100.0% |  |
| 9 | `BuySum` | 买入金额(元) | number(19,4) | ✓ | 50.11% |  |
| 10 | `SaleSum` | 卖出金额(元) | number(19,4) | ✓ | 49.92% |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

与科创板交易所日公开信息（LC_STIBOpTradInfo）表的ID关联，得到对应异动类型的详细信息。

### ReportArea (统计方式)

统计方式(ReportArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1363，得到统计方式的具体描述：10-买卖金额，11-买入金额，13-卖出金额。

### BOCode (营业部编号)

营业部编号(BOCode)：与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部的具体信息。

### SecuCoBelongedCode (营业部所属券商编号)

营业部所属券商编号(SecuCoBelongedCode)与“机构基本资料(LC_InstiArchive)”中的企业编号(CompanyCode)关联，得到营业部所属券商的具体信息。

## SQL示例

```sql
-- 查询 科创板交易所日公开信息附表 数据
SELECT *
FROM lc_stiboptradinfoatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
