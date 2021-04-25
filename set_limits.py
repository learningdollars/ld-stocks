from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://client.schwab.com/")
print("waiting for user to login")
time.sleep(5)
TRADE = "https://client.schwab.com/Areas/Trade/Stocks/Entry.aspx?Symbol="

f = open("bought.csv")

for stock in f:
	ticker = stock.strip()
	print("setting limit for ", stock)
	browser.get(TRADE + ticker)
	action = browser.find_element_by_id("ddlAction_0")
	action.click()
	