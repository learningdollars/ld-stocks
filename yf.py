from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import sys
from selenium.common import exceptions
import csv
import pandas as pd
from next_week import next_suny
from next_week import next_monday
import time
import yfinance as yf

# market_tech = yf.Ticker("MSFT")
# print(market_tech.info.get('sector'))


title_ticker = []
event_ticker = []
url_ticker = []



browser = webdriver.Firefox()
browser.get("https://markets.businessinsider.com/earnings-calendar#date="+next_monday+"-"+next_suny+"&name=&countries=&eventtypes=103,99&tab=ALL")
i = 0
while i<4:
    try:
        earnings = browser.find_elements_by_tag_name("#calendar_grid_container > div.table-responsive > table > tbody > tr")
        for earning in earnings:
            try:
                title = earning.find_element_by_css_selector("#calendar_grid_container > div.table-responsive > table > tbody > tr > td > a > strong").text
                href = earning.find_element_by_css_selector("#calendar_grid_container > div.table-responsive > table > tbody > tr > td > a").get_attribute("href")
                eventTicker = earning.find_element_by_css_selector("#calendar_grid_container > div.table-responsive > table > tbody > tr > td:nth-child(3)").text

                # title = earning.find_element_by_css_selector("#calendar_grid_container > div.table-responsive > table > tbody > tr > td > a > strong")
                title_ticker.append(title)
                event_ticker.append(eventTicker)
                url_ticker.append(href)
            except:
                pass
            print('Getting nth-child(11)')
            javascript = browser.find_element_by_xpath('//*[@id="calendar_grid_container"]/div[2]/div[2]/a[11]')
            browser.execute_script("arguments[0].click();",javascript)
            time.sleep(3)
            # 
            i = 0
            while i<5:
                try:
                    print('Getting nth-child(12)')
                    javascriptClick = WebDriverWait(browser,200).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="calendar_grid_container"]/div[2]/div[2]/a[12]')))
                    browser.execute_script("arguments[0].click();",javascriptClick)
                    time.sleep(10)
                    print("Done")
                    i+=1
                except exceptions.StaleElementReferenceException:
                    pass
            while i<10:
                try:
                    print('Getting nth-child(11) Again')
                    jsClick = WebDriverWait(browser,200).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="calendar_grid_container"]/div[2]/div[2]/a[11]')))
                    browser.execute_script("arguments[0].click();",jsClick)
                    time.sleep(10)
                    print("Done Clicking 11th")
                    i+=1
                except exceptions.StaleElementReferenceException:
                    pass
            while i<4:
                try:
                    print("Getting 12th child again")
                    jsClicks = WebDriverWait(browser,200).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="calendar_grid_container"]/div[2]/div[2]/a[12]')))
                    browser.execute_script("arguments[0].click();",jsClicks)
                    time.sleep(10)
                    print("Done")
                    i +=1
                except exceptions.StaleElementReferenceException:
                    pass
    except exceptions.StaleElementReferenceException:
        pass
final = pd.DataFrame(list(zip(title_ticker,event_ticker,url_ticker)),columns=['Ticker','Event','URL'])
final.to_csv("Final.csv",index=False)
