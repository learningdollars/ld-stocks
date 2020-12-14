from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd
from next_week import next_monday
from next_week import next_suny
i=0
earn = []
while i<1:
    try:
        browser = webdriver.Chrome()
        browser.get("https://finance.yahoo.com/calendar/earnings?from="+next_monday+"&to="+next_suny+"&day=2020-12-21")
        titles = browser.find_elements_by_css_selector('table tbody tr')
        for title in titles:
            earning = title.find_element_by_css_selector('table tbody tr td a').text
            earn.append(earning)
        i+=1
    except:
        print(sys.exc_info())
final = pd.DataFrame(list(zip(earn)),columns=['Ticker'])
final.to_csv("Final.csv",index=False)