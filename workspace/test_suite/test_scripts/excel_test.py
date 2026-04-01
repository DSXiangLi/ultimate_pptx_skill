#!/usr/bin/env python3
import pandas as pd

# 创建财务数据
data = {
    '年份': [2022, 2023, 2024],
    '营收(亿元)': [142.56, 132.85, 300],
    '净利润(亿元)': [-67.47, 5.24, 55],
    '毛利率(%)': [51.52, 60.51, 66]
}

df = pd.DataFrame(data)

# 保存为Excel文件
df.to_excel('/home/jovyan/.openclaw/workspace/test_suite/test_reports/sjht_excel_test.xlsx', index=False)
print("Excel文件已生成: test_reports/sjht_excel_test.xlsx")