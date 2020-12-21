import yfinance as yf
import csv
import sys
import time
from selenium import webdriver
import datetime
import random

import pandas as pd


# function
def csv_url_reader(url_obj):
    next_week = (datetime.date.today().isocalendar()[1]) + 1
    week = next_week - 2
    start_date = time.asctime(time.strptime('2020 %d 0' % week, '%Y %W %w'))
    start_date = datetime.datetime.strptime(start_date, '%a %b %d %H:%M:%S %Y')
    dates = [start_date.strftime('%Y-%m-%d')]
    for i in range(1, 7):
        day = start_date + datetime.timedelta(days=i)
        dates.append(day.strftime('%Y-%m-%d'))
    reader = csv.DictReader(url_obj, delimiter=',')
    for line in reader:
        try:
            real_ticker = line["Stock"]
            precision = line["Predecision"]
            if precision == 'TRUE':
                browser = webdriver.Chrome()
                browser.get("https://robinhood.com/stocks/" + real_ticker)
                name = real_ticker
                stockname = browser.find_elements_by_css_selector('header.Jo5RGrWjFiX_iyW3gMLsy')
                for stock in stockname:
                    try:
                        name = stock.find_element_by_css_selector('h1').text
                    except:
                        ('Oops!!', sys.exc_info())
                ratings = browser.find_elements_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92')
                rat = "rating"
                for rating in ratings:
                    try:
                        rat = rating.find_element_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92 h2').text
                    except:
                        ('Oops!!', sys.exc_info())
                tech = "sector"
                try:
                    market_tech = yf.Ticker(real_ticker)
                    tech = market_tech.info.get('sector')
                except:
                    # NOTE IN NEXT RUN - NEED TO INVESTIGATE GURUFOCUS UNK
                    (sys.exc_info())
                browser.get("https://www.gurufocus.com/stock/" + real_ticker + "/summary")
                time.sleep(4 + random.random() * 10)
                gurus = browser.find_elements_by_css_selector("button.el-button.el-popover__reference")
                data = "UNK"
                for guru in gurus:
                    try:
                        data = guru.find_element_by_css_selector("span").text
                    except:
                        ('Oops!', sys.exc_info())
                earning = "NO"
                try:
                    for date in dates:
                        browser.get(
                            "https://finance.yahoo.com/calendar/earnings?from=" + dates[0] + "&to=" + dates[6] + "&day=" + date)
                        time.sleep(4 + random.random() * 10)
                        titles = browser.find_elements_by_css_selector('table tbody tr')
                        for title in titles:
                            earning = title.find_element_by_css_selector('table tbody tr td a').text
                            if earning not in real_ticker:
                                earning = "NO"
                            else:
                                earning = date
                except:
                    print("failed to get earnings report")
                print(name + ', ' + rat + ', ' + data + ', ' + tech + ', ' + earning)
                time.sleep(4 + random.random() * 10)
                browser.quit()
            else:
                print("NA")
        except:
            print("failed to do this stock but will do next")


if __name__ == "__main__":
    with open("tickers.csv") as url_obj:
        csv_url_reader(url_obj)
