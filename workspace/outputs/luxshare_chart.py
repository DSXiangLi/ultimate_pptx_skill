#!/usr/bin/env python3
"""
功能: 查询立讯精密(002475)最近三年营收和净利润，绘制柱状图
"""

import pymysql
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from decimal import Decimal

# ============ 中文字体设置 ============
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
print("使用字体: SimHei")

# ============ 数据库连接 ============
conn = pymysql.connect(
    host='10.65.69.253', port=3306, 
    user='ro_ciawind_yanjiuzu@tn_pro_ciawind#cl_p_ob4_sj', 
    password='Ro_Ci09a_Y6jz', 
    database='gildata', charset='utf8mb4'
)
cur = conn.cursor()

# 查询立讯精密的年报数据
company_code = 80190
cur.execute(f"""SELECT EndDate, TotalOperatingRevenue, NetProfit 
FROM LC_IncomeStatementAll 
WHERE CompanyCode = {company_code} 
AND IfAdjusted = 2 AND IfMerged = 1 AND AccountingStandards = 1
AND MONTH(EndDate) = 12
ORDER BY EndDate DESC 
LIMIT 3""")
rows = cur.fetchall()
conn.close()

# 处理数据
years = []
revenue = []  # 营收（亿元）
profit = []   # 净利润（亿元）

for r in reversed(rows):  # 按年份正序排列
    date = r[0]
    year = date.year
    rev = float(r[1]) / 100000000  # 转换为亿元
    prof = float(r[2]) / 100000000
    years.append(str(year))
    revenue.append(rev)
    profit.append(prof)
    print(f"{year}年: 营收 {rev:.2f}亿元, 净利润 {prof:.2f}亿元")

# 绘制柱状图
fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(years))
width = 0.35

bars1 = ax.bar(x - width/2, revenue, width, label='营业收入', color='#4472C4', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, profit, width, label='净利润', color='#ED7D31', edgecolor='black', linewidth=0.5)

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=12, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_xlabel('年度', fontsize=13)
ax.set_ylabel('金额（亿元）', fontsize=13)
ax.set_title('立讯精密(002475) 最近三年营收与净利润', fontsize=15, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.legend(loc='upper left', fontsize=12)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim(0, max(revenue) * 1.15)

# 添加数据来源标注
ax.text(0.99, 0.01, '数据来源: 恒生聚源', 
        transform=ax.transAxes, fontsize=9, 
        verticalalignment='bottom', horizontalalignment='right',
        color='gray')

plt.tight_layout()

# 保存图片
output_path = '/home/jovyan/.openclaw/workspace/outputs/luxshare_revenue_profit.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n图表已保存: {output_path}")

plt.show()

# 输出数据表格
print("\n" + "="*60)
print("立讯精密(002475) 最近三年财务数据汇总")
print("="*60)
print(f"{'年度':<10} {'营业收入(亿元)':<18} {'净利润(亿元)':<18} {'净利率(%)':<12}")
print("-"*60)
for i, year in enumerate(years):
    rev = revenue[i]
    prof = profit[i]
    margin = (prof / rev * 100)
    print(f"{year:<10} {rev:<18.2f} {prof:<18.2f} {margin:<12.2f}")
print("="*60)
