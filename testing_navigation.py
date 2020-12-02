from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from next_week import next_monday
from next_week import  next_suny
import  sys
from selenium.common import exceptions
import time
href_e = []
print("Opening.......................................................................")
browser = webdriver.Firefox()
browser.get("https://markets.businessinsider.com/earnings-calendar#date="+next_monday+"-"+next_suny+"&name=&countries=&eventtypes=103,99&tab=ALL")
# 
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
