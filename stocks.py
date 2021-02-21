import csv
import datetime
import random
import sys
import time

import pandas as pd
import yfinance as yf
from selenium import webdriver

# EDIT GET THE FIRST 100 PLUS THE STOCKS WE LIKE BY DEFAULT


# function
def csv_url_reader(url_obj):
    next_week = (datetime.date.today().isocalendar()[1]) % 52 + 1
    week = next_week - 2
    start_date = time.asctime(time.strptime("2021 %d 0" % week, "%Y %W %w"))
    start_date = datetime.datetime.strptime(start_date, "%a %b %d %H:%M:%S %Y")
    dates = [start_date.strftime("%Y-%m-%d")]
    for i in range(1, 7):
        day = start_date + datetime.timedelta(days=i)
        dates.append(day.strftime("%Y-%m-%d"))
    reader = csv.DictReader(url_obj, delimiter=",")

    earnings_reports = None
    for line in reader:
        try:
            real_ticker = line["Stock"]
            precision = line["Predecision"]
            if precision == "TRUE":
                browser = webdriver.Chrome()
                browser.get("https://robinhood.com/stocks/" + real_ticker)
                name = real_ticker
                stockname = browser.find_elements_by_css_selector(
                    "header.Jo5RGrWjFiX_iyW3gMLsy"
                )
                for stock in stockname:
                    try:
                        name = stock.find_element_by_css_selector("h1").text
                    except:
                        ("Oops!!", sys.exc_info())
                ratings = browser.find_elements_by_css_selector(
                    "div._1fEdz1YPOLpLW1Ow3rKh92"
                )
                rat = "rating"
                for rating in ratings:
                    try:
                        rat = rating.find_element_by_css_selector(
                            "div._1fEdz1YPOLpLW1Ow3rKh92 h2"
                        ).text
                    except:
                        ("Oops!!", sys.exc_info())
                tech = "sector"
                try:
                    market_tech = yf.Ticker(real_ticker)
                    tech = market_tech.info.get("sector")
                except:
                    # NOTE IN NEXT RUN - NEED TO INVESTIGATE GURUFOCUS UNK
                    (sys.exc_info())
                browser.get(
                    "https://www.gurufocus.com/stock/"
                    + real_ticker
                    + "/summary"
                )
                time.sleep(4 + random.random() * 10)
                gurus = browser.find_elements_by_css_selector(
                    "button.el-button.el-popover__reference"
                )
                data = "UNK"
                for guru in gurus:
                    try:
                        data = guru.find_element_by_css_selector("span").text
                    except:
                        ("Oops!", sys.exc_info())
                earning = "NO"
                to_report = earning
                if earnings_reports:
                    if real_ticker in earnings_reports:
                        earning = earnings_reports[real_ticker]
                else:
                    try:
                        earnings_reports = {}
                        for date in dates:
                            browser.get(
                                f"https://finance.yahoo.com/calendar/earnings?from={dates[0]}&to={dates[6]}&day={date}"
                            )
                            time.sleep(4 + random.random() * 10)
                            titles = browser.find_elements_by_css_selector(
                                "table tbody tr"
                            )
                            for title in titles:
                                earning = title.find_element_by_css_selector(
                                    "table tbody tr td a"
                                ).text
                                print(earning, "has an earnings report")
                                earnings_reports[earning] = date
                        print("earnings_reports: ", earnings_reports)
                        to_report = earnings_reports[earning]
                    except:
                        print("failed to get earnings report")
                print(
                    f"{name}, {rat}, {data}, {tech}, {to_report}"
                )
                time.sleep(4 + random.random() * 10)
                browser.quit()
            else:
                print("NA")
        except:
            print("failed to do this stock but will do next")


if __name__ == "__main__":
    with open("tickers.csv") as url_obj:
        csv_url_reader(url_obj)
