#!/usr/bin/env python3
from pptx import Presentation
from pptx.util import Inches

# 创建PPT演示文稿
prs = Presentation()

# 第1页：标题页
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "世纪华通(002602)投资分析"
subtitle.text = "生成时间: 2026-03-30"

# 第2页：财务摘要
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "财务亮点"
content = slide.placeholders[1]
content.text = "• 2024年营收预计300亿元\n• 净利润预计55亿元\n• 毛利率提升至66%"

# 第3页：投资建议
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "投资建议"
content = slide.placeholders[1]
content.text = "• AI算力业务成为新增长引擎\n• 游戏出海带来增量空间\n• 目标价区间7-9元"

# 保存PPT文件
prs.save('/home/jovyan/.openclaw/workspace/test_suite/test_reports/sjht_ppt_test.pptx')
print("PPT文件已生成: test_reports/sjht_ppt_test.pptx")