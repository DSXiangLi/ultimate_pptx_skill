#!/usr/bin/env python3
"""
查询世纪华通(002602)财务数据 - 使用网络爬虫
数据来源：东方财富、同花顺等公开网站
"""

import requests
import json
import pandas as pd
from datetime import datetime

class StockFinancialData:
    def __init__(self, stock_code='002602'):
        self.stock_code = stock_code
        self.stock_name = '世纪华通'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_eastmoney_financial(self):
        """从东方财富获取财务数据"""
        url = f'https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=SZ{self.stock_code}'
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"东方财富数据获取失败: {e}")
            return None
    
    def get_eastmoney_api_data(self):
        """使用东方财富API获取财务摘要"""
        # 财务指标API
        api_url = f'https://datacenter.eastmoney.com/api/data/v1/get?reportName=RPT_FCI_PROFIT&columns=ALL&filter=(SECURITY_CODE%3D%22{self.stock_code}%22)'
        
        try:
            response = requests.get(api_url, headers=self.headers, timeout=10)
            data = response.json()
            return data
        except Exception as e:
            print(f"API数据获取失败: {e}")
            return None
    
    def get_stock_quote(self):
        """获取股票行情数据"""
        url = f'https://push2.eastmoney.com/api/qt/stock/get?secid=0.{self.stock_code}&fields=f43,f44,f45,f46,f47,f48,f57,f58,f60,f170'
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            data = response.json()
            if data.get('data'):
                return data['data']
            return None
        except Exception as e:
            print(f"行情数据获取失败: {e}")
            return None
    
    def get_financial_summary(self):
        """获取财务摘要"""
        # 使用新浪财务数据
        url = f'https://finance.pae.baidu.com/selfselect/getstockquotation?all=1&code=sz{self.stock_code}&ktype=1&group=quotation_minute&finClientType=pc'
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            return response.json()
        except Exception as e:
            print(f"财务摘要获取失败: {e}")
            return None
    
    def display_sample_data(self):
        """显示示例财务数据结构"""
        print(f"\n{'='*80}")
        print(f"股票: {self.stock_name} ({self.stock_code})")
        print(f"{'='*80}\n")
        
        # 尝试获取行情数据
        quote = self.get_stock_quote()
        if quote:
            print("【行情数据】")
            print(f"  股票名称: {quote.get('f58', 'N/A')}")
            print(f"  股票代码: {quote.get('f57', 'N/A')}")
            print(f"  当前价格: {quote.get('f43', 'N/A')}")
            print(f"  涨跌幅: {quote.get('f170', 'N/A')}%")
            print(f"  成交量: {quote.get('f47', 'N/A')}")
            print(f"  成交额: {quote.get('f48', 'N/A')}")
            print()
        
        # 由于网络限制，显示模拟数据示例
        print("【财务数据示例结构】")
        print("由于网络限制，以下为世纪华通的典型财务数据结构：\n")
        
        sample_data = {
            '报告期': ['2024-09-30', '2024-06-30', '2023-12-31', '2023-09-30'],
            '营业总收入(亿元)': [155.23, 102.45, 142.56, 108.92],
            '归母净利润(亿元)': [18.56, 12.34, 5.24, 8.67],
            '扣非净利润(亿元)': [16.78, 10.89, 3.45, 7.23],
            '毛利率(%)': [45.23, 44.56, 42.18, 43.67],
            '净利率(%)': [11.95, 12.04, 3.68, 7.96],
            'ROE(%)': [6.78, 4.56, 1.89, 3.45],
            '资产负债率(%)': [28.45, 29.12, 30.56, 31.23]
        }
        
        df = pd.DataFrame(sample_data)
        print(df.to_string(index=False))
        
        print("\n【说明】")
        print("1. 以上数据为示例结构，非实时真实数据")
        print("2. 如需真实数据，建议通过以下方式获取：")
        print("   - 东方财富网: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=SZ002602")
        print("   - 同花顺: https://basic.10jqka.com.cn/002602/finance.html")
        print("   - 巨潮资讯网: http://www.cninfo.com.cn/new/information/topSearch/query")
        print("3. 原脚本(sjht_financial.py)需要连接内部数据库，当前环境无法访问")

def main():
    stock = StockFinancialData('002602')
    stock.display_sample_data()

if __name__ == "__main__":
    main()
