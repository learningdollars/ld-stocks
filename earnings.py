from selenium import webdriver
import sys
import pandas as pd
from next_week import next_monday
from next_week import next_suny
import datetime
import time

i = 0
earn = []
while i < 1:
    try:
        next_week = (datetime.date.today().isocalendar()[1]) + 1
        week = next_week - 2
        start_date = time.asctime(time.strptime('2020 %d 0' % week, '%Y %W %w'))
        start_date = datetime.datetime.strptime(start_date, '%a %b %d %H:%M:%S %Y')
        dates = [start_date.strftime('%Y-%m-%d')]
        for i in range(1, 7):
            day = start_date + datetime.timedelta(days=i)
            dates.append(day.strftime('%Y-%m-%d'))
        browser = webdriver.Chrome()
        for date in dates:
            browser.get(
                "https://finance.yahoo.com/calendar/earnings?from=" + dates[0] + "&to=" + dates[6] + "&day=" + date)
            titles = browser.find_elements_by_css_selector('table tbody tr')
            for title in titles:
                earning = title.find_element_by_css_selector('table tbody tr td a').text
                print(earning)
            i += 1
    except:
        print(sys.exc_info())
# final = pd.DataFrame(list(zip(earn)), columns=['Ticker'])
# final.to_csv("Final.csv", index=False)
