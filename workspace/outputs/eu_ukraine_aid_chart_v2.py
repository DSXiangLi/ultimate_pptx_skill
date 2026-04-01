import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 欧洲对乌克兰援助数据（单位：亿欧元）
# 数据来源：德国基尔世界经济研究所 Ukraine Support Tracker 及欧盟官方数据
years = ['2022', '2023', '2024', '2025', '2026(Plan)']

# 援助金额（亿欧元）- 基于搜索结果整理
military_aid = [130, 160, 220, 320, 350]  # 军事援助
financial_aid = [120, 130, 150, 150, 300]  # 财政/预算援助
humanitarian_aid = [60, 60, 80, 50, 50]   # 人道主义援助

x = np.arange(len(years))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.bar(x - width, military_aid, width, label='Military Aid', color='#e74c3c')
bars2 = ax.bar(x, financial_aid, width, label='Financial Aid', color='#3498db')
bars3 = ax.bar(x + width, humanitarian_aid, width, label='Humanitarian Aid', color='#2ecc71')

# 添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Aid Amount (Billion EUR)', fontsize=12)
ax.set_title('Europe Aid to Ukraine by Year (2022-2026)\nData Source: Kiel Institute Ukraine Support Tracker', fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper left')

# 添加总计数据
totals = [m + f + h for m, f, h in zip(military_aid, financial_aid, humanitarian_aid)]
for i, total in enumerate(totals):
    ax.annotate(f'Total: {total}B',
                xy=(i, max(military_aid[i], financial_aid[i], humanitarian_aid[i]) + 30),
                ha='center', fontsize=10, fontweight='bold', color='#c0392b')

ax.set_ylim(0, 400)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart.png', dpi=150, bbox_inches='tight')
print("Chart saved to: /home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart.png")

# 打印数据汇总
print("\n=== EU Aid to Ukraine Summary ===")
print(f"{'Year':<12} {'Military':<12} {'Financial':<12} {'Humanitarian':<12} {'Total':<12}")
print("-" * 60)
for i, year in enumerate(years):
    print(f"{year:<12} {military_aid[i]:<12} {financial_aid[i]:<12} {humanitarian_aid[i]:<12} {totals[i]:<12}")
print("-" * 60)
print(f"{'2022-2025':<12} {sum(military_aid[:-1]):<12} {sum(financial_aid[:-1]):<12} {sum(humanitarian_aid[:-1]):<12} {sum(totals[:-1]):<12}")

# 创建第二张图：堆叠柱状图
fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.bar(years, military_aid, label='Military Aid', color='#e74c3c')
ax2.bar(years, financial_aid, bottom=military_aid, label='Financial Aid', color='#3498db')
ax2.bar(years, humanitarian_aid, bottom=[m+f for m,f in zip(military_aid, financial_aid)], label='Humanitarian Aid', color='#2ecc71')

# 添加总计标签
for i, total in enumerate(totals):
    ax2.annotate(f'{total}B EUR',
                xy=(i, total + 10),
                ha='center', fontsize=11, fontweight='bold', color='#c0392b')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Aid Amount (Billion EUR)', fontsize=12)
ax2.set_title('Europe Aid to Ukraine by Year (Stacked)\nData Source: Kiel Institute Ukraine Support Tracker', fontsize=14, pad=20)
ax2.legend(loc='upper left')
ax2.set_ylim(0, 800)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart_stacked.png', dpi=150, bbox_inches='tight')
print("\nStacked chart saved to: /home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart_stacked.png")
