from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# constants
TRADE = "https://client.schwab.com/Areas/Trade/Stocks/Entry.aspx?Symbol="
INITIAL_GROWTH = 1.0075

browser = webdriver.Chrome()
browser.get("https://client.schwab.com/")
print("waiting for user to login")
time.sleep(5)

f = open("bought.csv")
# may not even need the bought csv
# can go through stocks in https://client.schwab.com/Areas/Accounts/Positions

for stock in f:
	ticker = stock.strip()
	print("==== setting initial limit for ", stock)
	browser.get(TRADE + ticker)
	
	action = Select(browser.find_element_by_id("ddlAction_0"))
	action.select_by_visible_text("Sell")
	
	# need to grab the quantity owned right now
	# need to grab the quantity we already have a limit sell for right now
	# need to find the difference - that's the amount we need to initially limit sell
	
	quantity_to_limit_sell = 1
	print(quantity_to_limit_sell, "shares")
	quantity_input = browser.find_element_by_id("txtQty_0")
	quantity_input.send_keys(str(quantity_to_limit_sell))
	
	ordertype = Select(browser.find_element_by_id("ddlType_0"))
	ordertype.select_by_visible_text("Limit")

	# need to grab the cost we bought the stock for
	purchase_price = 3341
	
	initial_limit = round(purchase_price*INITIAL_GROWTH, 2)
	limitamt_input = browser.find_element_by_id("txtLimit_0")
	limitamt_input.send_keys(str(initial_limit))

	review_order = browser.find_element_by_id("btnReview")
	review_order.click()

	print("==== changing limit for ", stock)
	# check how many shares for which we have already set a limit sell

	# if so, change the limit sell if needed, o/w set the limit sell
	
	# check the date when the shares were purchased, and put the limit sell for the appropriate amount based on that

	# if it's been over a year, sell the security so you can count the loss for tax purposes - list out the securities to sell