# MF_ChargeRateInfo

**中文名**: 公募基金费率信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ChargeRateInfo` |
| MySQL表名 | `mf_chargerateinfo` |
| 中文名 | 公募基金费率信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.本表记录基金的相关费率数据及执行情况，包括认购费、申购费、赎回费、管理费、托管费等详细费用。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ExcuteDate` | 执行日期 | date | ✗ | 100.0% |  |
| 7 | `CancelDate` | 取消日期 | date | ✓ | 43.77% |  |
| 8 | `ChargeRateType` | 费率类别 | number(10) | ✗ | 100.0% | 费率类别(ChargeRateType)与(CT_SystemConst)表中的DM字段关联，令LB=1895，得到费率... |
| 9 | `ApplyingMarket` | 适用场所 | number(10) | ✗ | 100.0% | 适用场所(ApplyingMarket)：1-场内，2-场外，3-场内场外 |
| 10 | `ChargePattern` | 收费模式 | number(10) | ✗ | 100.0% | 收费模式(ChargePattern)：1-前端，2-后端 |
| 11 | `Channel` | 渠道 | number(10) | ✗ | 100.0% | 渠道(Channel)：1-全渠道，11-直销柜台，12-直销网上 |
| 12 | `ClientType` | 适用客户类型 | number(10) | ✗ | 100.0% | 适用客户类型(ClientType)与(CT_SystemConst)表中的DM字段关联，令LB=1807，得到适用客户... |
| 13 | `ChargeRateDiv` | 费率划分区间编码 | number(10) | ✓ | 100.0% | 费率划分区间编码(ChargeRateDiv)：110-申购金额类，120-申购份额类，130-持有期限类，150-收益... |
| 14 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 15 | `DivIntervalDes` | 费率划分区间描述 | varchar2(1000) | ✓ | 64.1% |  |
| 16 | `ChargeRateIntervalBe` | 费率划分区间起始数值 | number(19,4) | ✓ | 64.05% |  |
| 17 | `ChargeRateIntervalEd` | 费率划分区间截止数值 | number(19,4) | ✓ | 45.16% |  |
| 18 | `IfApplyBegin` | 是否包含费率划分区间起始数值 | number(10) | ✓ | 45.58% | 是否包含费率划分区间起始数值(IfApplyBegin)：1-是，0-否 |
| 19 | `IfApplyEnd` | 是否包含费率划分区间截止数值 | number(10) | ✓ | 45.15% | 是否包含费率划分区间截止数值(IfApplyEnd)：1-是，0-否 |
| 20 | `ChargeRateDes` | 费率描述 | varchar2(1000) | ✓ | 100.0% |  |
| 21 | `MinChargeRate` | 费率最低值 | number(19,9) | ✓ | 99.94% |  |
| 22 | `MaxChargeRate` | 费率最高值 | number(19,9) | ✓ | 99.94% |  |
| 23 | `ChargeRateCur` | 费率币种 | number(10) | ✓ | 100.0% | 费率币种(ChargeRateCur)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND D... |
| 24 | `ChargeRateUnit` | 费率单位 | number(10) | ✓ | 100.0% | 费率单位(ChargeRateUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND ... |
| 25 | `FloChargeRate` | 费率计算方式 | varchar2(1000) | ✓ | 0.11% |  |
| 26 | `Notes` | 备注说明 | varchar2(1000) | ✓ | 4.59% |  |
| 27 | `IfEffected` | 是否最新生效 | number(10) | ✓ | 100.0% | 是否最新生效(IfEffected)：1-是，2-否 |
| 28 | `IfExecuted` | 是否当前执行 | number(10) | ✓ | 100.0% | 是否当前执行(IfExecuted)：1-是，2-否 |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ChargeRateType (费率类别)

费率类别(ChargeRateType)与(CT_SystemConst)表中的DM字段关联，令LB=1895，得到费率类别的具体描述：10-认购费，11-日常申购费，12-日常赎回费，13-转换费，14-转换补差费，15-管理费，16-托管费，17-指数许可费，18-原份额赎回费，19-营销费，20-增值服务费，21-附加管理费，22-定期定额申购费，23-定期定额赎回费，24-注册登记费，25-行政管理费，26-经常性开支比率，27-受托人费用。

### ApplyingMarket (适用场所)

适用场所(ApplyingMarket)：1-场内，2-场外，3-场内场外

### ChargePattern (收费模式)

收费模式(ChargePattern)：1-前端，2-后端

### Channel (渠道)

渠道(Channel)：1-全渠道，11-直销柜台，12-直销网上

### ClientType (适用客户类型)

适用客户类型(ClientType)与(CT_SystemConst)表中的DM字段关联，令LB=1807，得到适用客户类型的具体描述：10-一般投资者，20-养老金客户，30-住房公积金客户，40-机构投资者，50-一般投资者+养老金客户，60-REITs战略投资者，70-REITs网下投资者，80-REITs公众投资者，99-其他特定客户。

### ChargeRateDiv (费率划分区间编码)

费率划分区间编码(ChargeRateDiv)：110-申购金额类，120-申购份额类，130-持有期限类，150-收益率类，160-净值增长率类，170-单一费率，180-受限开放期类，190-自由开放期类，200-累计净值类，210-净资产类，220-年化收益率类，230-七日年化收益率类，240-封闭期类，250-自动赎回期类，260-实际费率，280-净收入，999-其他

### IfApplyBegin (是否包含费率划分区间起始数值)

是否包含费率划分区间起始数值(IfApplyBegin)：1-是，0-否

### IfApplyEnd (是否包含费率划分区间截止数值)

是否包含费率划分区间截止数值(IfApplyEnd)：1-是，0-否

### ChargeRateCur (费率币种)

费率币种(ChargeRateCur)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM IN (1420,1000,1010,1020,1100,1120,1160,1220,1320,1330,1360,1430,3030,5010,3000)，得到费率币种的具体描述：1000-美元，1100-港元，1120-印度尼西亚卢比，1160-日本元，1220-马来西亚林吉特，1320-新加坡元，1330-韩国元，1360-泰国铢，1420-人民币元，1430-台湾元，3000-欧元，3030-英镑，5010-加拿大元。

### ChargeRateUnit (费率单位)

费率单位(ChargeRateUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1208 AND DM IN (6, 7)，得到费率单位的具体描述：6-%，7-元。

## SQL示例

```sql
-- 查询 公募基金费率信息 数据
SELECT *
FROM mf_chargerateinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
