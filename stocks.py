import yfinance as yf
import csv
import time
from selenium import webdriver

import pandas as pd
stock_name = []
rate = []
guru_value = []
markets = []
# function
def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    for line in reader:
        # url = line["URL"]
        precision = line["Predecision"]
        title = line["Stock"]
        # print(url +' ' + title)
        if precision =='TRUE':
            browser = webdriver.Chrome()
            browser.get("https://robinhood.com/stocks/" + title)
            stockname = browser.find_elements_by_css_selector('header.Jo5RGrWjFiX_iyW3gMLsy')
            for stock in stockname:
                name = stock.find_element_by_css_selector('h1').text
                stock_name.append(name)
            ratings = browser.find_elements_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92')
            for rating in ratings:
                rat = rating.find_element_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92 h2').text
                # print(rat + ' '+ precision)
                rate.append(rat)
            # assert title in browser.title
            # Getting Guru multiple sites
            browser.get("https://www.gurufocus.com/stock/"+title+"/summary")
            gurus = browser.find_elements_by_css_selector("button.el-button.fs-regular.el-button--danger.el-button--mini.el-popover__reference")
            for guru in gurus:
                val = guru.find_element_by_css_selector("span").text
                guru_value.append(val)
            # Market Technology
            market_tech = yf.Ticker(title)
            tech = market_tech.info.get('sector')
            markets.append(tech)
            # Output
            print(name + ' '+ rat + ' ' + val + ' ' + tech)
            df = pd.DataFrame(list(zip(stock_name,rate,guru_value,markets)), columns=['Stock_Name','Rating','Guru_value','Market'])
            df.to_csv('Final.csv',index=False)
            browser.quit()
            time.sleep(2)
        else:
            print("NA")

if __name__ =="__main__":
    with open("sheet1.csv") as url_obj:
        csv_url_reader(url_obj)