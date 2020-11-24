import yfinance as yf
import csv
import sys
import time
from selenium import webdriver

import pandas as pd
# function
def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    for line in reader:
        # url = line["URL"]
        precision = line["Predecision"]
        title = line["Stock"]
        # print(url +' ' + title)
        if precision =='TRUE':
            browser = webdriver.Firefox()
            browser.get("https://robinhood.com/stocks/" + title)
            stockname = browser.find_elements_by_css_selector('header.Jo5RGrWjFiX_iyW3gMLsy')
            for stock in stockname:
                try:
                    name = stock.find_element_by_css_selector('h1').text
                except:
                    ('Oops!!',sys.exc_info)
            ratings = browser.find_elements_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92')
            for rating in ratings:
                try:
                    rat = rating.find_element_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92 h2').text
                except:
                    ('Oops!!',sys.exc_info())
            # assert title in browser.title
            # Market Technology
            try:
                market_tech = yf.Ticker(title)
                tech = market_tech.info.get('sector')
            except:
                ('Oops!',sys.exc_info())
            # Getting Guru multiple sites
            browser.get("https://www.gurufocus.com/stock/"+title+"/summary")
            gurus = browser.find_elements_by_css_selector("button.el-button.fs-regular.el-button--danger.el-button--mini.el-popover__reference")
            for guru in gurus:
                try:
                    data = guru.find_element_by_css_selector("span").text
                except:
                    ('Oops!',sys.exc_info())
            # Output
            browser.get("https://markets.businessinsider.com/stocks/"+title+"-stock")
            earnings = browser.find_elements_by_class_name("price-section__row")
            for earning in earnings:
                try:
                    title = earning.find_element_by_css_selector("span.price-section__current-value").text
                    if title > "1":
                        title = "YES"
                    else:
                        title = "NO"
                except:
                    ('Oops',sys.exc_info())
            print((name + ', '+ rat  +', ' + data + ', ' + str(tech) + ', ' + title))
            browser.quit()
            time.sleep(2)
        else:
            print("NA")

if __name__ =="__main__":
    with open("tickers1.csv") as url_obj:
        csv_url_reader(url_obj)