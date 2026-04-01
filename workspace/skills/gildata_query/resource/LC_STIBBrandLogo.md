# LC_STIBBrandLogo

**中文名**: 科创板公司产品品牌

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBBrandLogo` |
| MySQL表名 | `lc_stibbrandlogo` |
| 中文名 | 科创板公司产品品牌 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

1.内容说明：记录科创板公司产品品牌logo，记录商标的整体情况，包括注册、续用、LOGO图片、专用权期限等
2.数据范围：待定
3.信息来源：国家工商行政管理总局

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `ApplicationNum` | 申请/注册号 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `BrandName` | 产品品牌名称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `ApplicationDate` | 申请日期 | date | ✓ | 100.0% |  |
| 6 | `INTType` | 国际分类 | number(10) | ✓ | 100.0% |  |
| 7 | `registerDate` | 注册公告日期 | date | ✓ | 99.98% |  |
| 8 | `PatentsStartDate` | 专用权期限起始 | date | ✗ | 100.0% |  |
| 9 | `PatentsEndDate` | 专用权期限截止 | date | ✓ | 99.96% |  |
| 10 | `Agency` | 代理/办理机构 | varchar2(100) | ✓ | 95.57% |  |
| 11 | `logoState` | 商标状态 | number(10) | ✓ | 100.0% | 商标状态（logoState）：该字段固定以下常量：1-注册；2-注销 |
| 12 | `WriteOffDate` | 注销日期 | date | ✓ | 0.0% |  |
| 13 | `Content` | 商标图标 | blob | ✓ | 88.95% |  |
| 14 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM i... |
| 15 | `Structure` | 商标结构 | number(10) | ✓ | 41.87% | 商标结构(Structure)与(CT_SystemConst)表中的DM字段关联，令LB = 2152，得到商标结构的... |
| 16 | `IfMain` | 是否主商标 | number(10) | ✓ | 0.0% | 是否主商标(IfMain)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in ... |
| 17 | `Height` | 商标高度 | number(10) | ✓ | 100.0% |  |
| 18 | `Width` | 商标宽度 | number(10) | ✓ | 100.0% |  |
| 19 | `Color` | 色彩情况 | number(10) | ✓ | 99.37% | 色彩情况(Color)与(CT_SystemConst)表中的DM字段关联，令LB = 2154，得到色彩情况的具体描述... |
| 20 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### logoState (商标状态)

商标状态（logoState）：该字段固定以下常量：1-注册；2-注销

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM in (10,21,26,27,28)，得到文件格式的具体描述：10-JPG，21-GIF，26-BMP，27-SWF，28-PNG。

### Structure (商标结构)

商标结构(Structure)与(CT_SystemConst)表中的DM字段关联，令LB = 2152，得到商标结构的具体描述：1-上下组合，2-左右组合，3-圆型，4-其他。

### IfMain (是否主商标)

是否主商标(IfMain)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否主商标的具体描述：1-是，2-否。

### Color (色彩情况)

色彩情况(Color)与(CT_SystemConst)表中的DM字段关联，令LB = 2154，得到色彩情况的具体描述：10-黑白，20-彩色。

## SQL示例

```sql
-- 查询 科创板公司产品品牌 数据
SELECT *
FROM lc_stibbrandlogo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
