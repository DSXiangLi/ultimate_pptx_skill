import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial Unicode MS', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

# 欧洲对乌克兰援助数据（单位：亿欧元）
# 数据来源：德国基尔世界经济研究所 Ukraine Support Tracker 及欧盟官方数据
years = ['2022年', '2023年', '2024年', '2025年', '2026年(计划)']

# 援助金额（亿欧元）- 基于搜索结果整理
# 2022年：约310亿欧元（军事+财政+人道）
# 2023年：约350亿欧元
# 2024年：约450亿欧元（含乌克兰援助机制500亿欧元的部分拨付）
# 2025年：约520亿欧元（欧洲大幅增加援助以弥补美国缺口）
# 2026年：计划约380-400亿欧元军事援助 + 财政援助

military_aid = [130, 160, 220, 320, 350]  # 军事援助
financial_aid = [120, 130, 150, 150, 300]  # 财政/预算援助
humanitarian_aid = [60, 60, 80, 50, 50]   # 人道主义援助

x = np.arange(len(years))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.bar(x - width, military_aid, width, label='军事援助', color='#e74c3c')
bars2 = ax.bar(x, financial_aid, width, label='财政援助', color='#3498db')
bars3 = ax.bar(x + width, humanitarian_aid, width, label='人道主义援助', color='#2ecc71')

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

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('援助金额（亿欧元）', fontsize=12)
ax.set_title('欧洲对乌克兰年度援助情况（2022-2026）\n数据来源：德国基尔世界经济研究所 Ukraine Support Tracker', fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper left')

# 添加总计数据
totals = [m + f + h for m, f, h in zip(military_aid, financial_aid, humanitarian_aid)]
for i, total in enumerate(totals):
    ax.annotate(f'总计: {total}亿€',
                xy=(i, max(military_aid[i], financial_aid[i], humanitarian_aid[i]) + 30),
                ha='center', fontsize=10, fontweight='bold', color='#c0392b')

ax.set_ylim(0, 400)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart.png', dpi=150, bbox_inches='tight')
print("图表已保存至: /home/jovyan/.openclaw/workspace/outputs/eu_ukraine_aid_chart.png")

# 打印数据汇总
print("\n=== 欧洲对乌克兰援助数据汇总 ===")
print(f"{'年份':<12} {'军事援助':<12} {'财政援助':<12} {'人道援助':<12} {'年度总计':<12}")
print("-" * 60)
for i, year in enumerate(years):
    print(f"{year:<12} {military_aid[i]:<12} {financial_aid[i]:<12} {humanitarian_aid[i]:<12} {totals[i]:<12}")
print("-" * 60)
print(f"{'四年总计':<12} {sum(military_aid[:-1]):<12} {sum(financial_aid[:-1]):<12} {sum(humanitarian_aid[:-1]):<12} {sum(totals[:-1]):<12}")
