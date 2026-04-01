# Outputs 文件夹

本文件夹用于存放生成的文件，按类型分类组织。

## 目录结构

```
outputs/
├── reports/           # 分析报告
├── charts/            # 数据可视化图表  
├── scripts/           # 脚本工具
├── data/              # 原始数据
└── README.md          # 本说明文件
```

## 文件清单

### 📊 Reports (分析报告)
| 文件 | 描述 |
| :--- | :--- |
| 世纪华通-一页纸.md | 世纪华通个股一页纸分析报告（初版） |
| 世纪华通-一页纸-20260330.md | 世纪华通个股一页纸分析报告（含真实财务数据）✅ |

### 📈 Charts (数据图表)
| 文件 | 描述 |
| :--- | :--- |
| sjht_revenue_profit_chart_chinese.png | 世纪华通近3年营收净利润柱状图（中文版，PNG）|
| sjht_revenue_profit_chart_chinese.pdf | 世纪华通近3年营收净利润柱状图（中文版，PDF）|

### 💻 Scripts (脚本工具)
| 文件 | 描述 |
| :--- | :--- |
| sjht_financial.py | 世纪华通财务数据获取脚本（已修复，可用）✅ |
| sjht_financial_web.py | 世纪华通财务数据获取脚本（网络版）|
| test_db_connection.py | 数据库连通性测试脚本 |

### 📁 Data (原始数据)
| 文件 | 描述 |
| :--- | :--- |
| sjht_full_data.txt | 世纪华通完整财务数据（原始数据，来自数据库）|

## 使用说明

- **所有生成的报告**默认保存到 `reports/` 子文件夹
- **图表文件**保存到 `charts/` 子文件夹  
- **脚本工具**保存到 `scripts/` 子文件夹
- **原始数据**保存到 `data/` 子文件夹
- 按日期和类型组织子文件夹（如需要）
