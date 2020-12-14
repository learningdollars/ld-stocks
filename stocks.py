import yfinance as yf
import csv
import sys
import time
from selenium import webdriver
from next_week import next_suny
from next_week import next_monday
from next_week import day_picked
import random

import pandas as pd
# function
def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    for line in reader:
        try:
            real_ticker = line["Stock"]
            precision = line["Predecision"]
            if precision =='TRUE':
                browser = webdriver.Chrome()
                browser.get("https://robinhood.com/stocks/" + real_ticker)
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
                try:
                    market_tech = yf.Ticker(real_ticker)
                    tech = market_tech.info.get('sector')
                except:
                    (sys.exc_info())
                browser.get("https://www.gurufocus.com/stock/"+real_ticker+"/summary")
                time.sleep(4+random.random()*10)
                gurus = browser.find_elements_by_css_selector("button.el-button.fs-regular.el-button--danger.el-button--mini.el-popover__reference")
                data ="UNK"
                for guru in gurus:
                    try:
                        data = guru.find_element_by_css_selector("span").text
                    except:
                        ('Oops!',sys.exc_info())
                earning = "NO"
                try:
                    browser.get("https://finance.yahoo.com/calendar/earnings?from="+next_monday+"&to="+next_suny+"&day="+day_picked+"")
                    time.sleep(4+random.random()*10)
                    titles = browser.find_elements_by_css_selector('table tbody tr')
                    for title in titles:
                        earning = title.find_element_by_css_selector('table tbody tr td a').text
                        if earning not in real_ticker:
                            earning = "NO"
                        else:
                            earning = day_picked
                except:
                    print("failed to get earnings report")
                try:
                    print(name + ', '+ rat  +', ' + data + ', ' + tech + ', ' + earning)
                except:
                    pass
                time.sleep(4+random.random()*10)
                browser.quit()
            else:
                print("NA")
        except:
            print("failed to do this stock but will do next")
if __name__ =="__main__":
    with open("tickers.csv") as url_obj:
        csv_url_reader(url_obj)