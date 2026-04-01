#!/usr/bin/env python3
from docx import Document
from docx.shared import Inches

# 创建Word文档
doc = Document()
doc.add_heading('世纪华通(002602)投资分析报告', 0)

# 添加段落
doc.add_paragraph('生成时间: 2026-03-30')
doc.add_paragraph('这是一份测试Word文档生成功能的示例报告。')

# 添加表格
table = doc.add_table(rows=1, cols=4)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '年份'
hdr_cells[1].text = '营收(亿元)'
hdr_cells[2].text = '净利润(亿元)'
hdr_cells[3].text = '毛利率'

# 添加数据行
row_cells = table.add_row().cells
row_cells[0].text = '2022'
row_cells[1].text = '142.56'
row_cells[2].text = '-67.47'
row_cells[3].text = '51.52%'

# 保存文档
doc.save('/home/jovyan/.openclaw/workspace/test_suite/test_reports/sjht_word_test.docx')
print("Word文档已生成: test_reports/sjht_word_test.docx")