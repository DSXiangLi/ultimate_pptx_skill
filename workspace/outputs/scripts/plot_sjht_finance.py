#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
世纪华通(002602)近3年营收及净利润柱状图
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 查找中文字体
chinese_font = None
for font in fm.findSystemFonts():
    try:
        name = fm.FontProperties(fname=font).get_name()
        if 'SimHei' in name or 'Noto' in name or 'CJK' in name:
            chinese_font = font
            break
    except:
        continue

if chinese_font:
    plt.rcParams['font.family'] = fm.FontProperties(fname=chinese_font).get_name()
else:
    plt.rcParams['font.family'] = 'DejaVu Sans'
    
plt.rcParams['axes.unicode_minus'] = False

# 世纪华通近3年年度财务数据（单位：亿元）
years = ['2023', '2024', '2025']
revenue = [132.85, 226.19, 272.23]  # 营业收入
net_profit = [5.88, 10.45, 44.42]   # 净利润（2025年为Q3累计）

# 创建图形
fig, ax = plt.subplots(figsize=(12, 7))

# 设置柱状图参数
bar_width = 0.35
x = np.arange(len(years))

# 绘制柱状图
bars1 = ax.bar(x - bar_width/2, revenue, bar_width, label='Revenue (100M)', color='#2E86AB', edgecolor='white', linewidth=1.5)
bars2 = ax.bar(x + bar_width/2, net_profit, bar_width, label='Net Profit (100M)', color='#E94F37', edgecolor='white', linewidth=1.5)

# 添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=11, fontweight='bold')

add_labels(bars1)
add_labels(bars2)

# 设置坐标轴
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Amount (100 Million CNY)', fontsize=14, fontweight='bold')
ax.set_title('SJHT (002602) Revenue & Net Profit 2023-2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.legend(loc='upper left', fontsize=11)

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# 设置y轴范围
ax.set_ylim(0, max(revenue) * 1.25)

# 调整布局
plt.tight_layout()

# 保存图片
output_path = '/home/jovyan/.openclaw/workspace/outputs/charts/sjht_revenue_profit_3years.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Chart saved to: {output_path}")

print("\n=== SJHT (002602) Financial Data 2023-2025 ===")
print(f"{'Year':<10}{'Revenue(100M)':<20}{'Net Profit(100M)':<20}")
print("-" * 50)
for i, year in enumerate(years):
    print(f"{year:<10}{revenue[i]:<20.2f}{net_profit[i]:<20.2f}")
print("-" * 50)
print("Note: 2025 data is Q3 cumulative")