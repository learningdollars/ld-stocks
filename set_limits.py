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
# can go through stocks in https://client.schwab.com/Areas/Accounts/Positions
browser.get("https://client.schwab.com/Areas/Accounts/Positions")
equities = browser.find_elements_by_xpath('//tr[@data-pulsr-securitygroup="Equity"]')

for equity in equities:
	ticker = equity.find_elements_by_tag_name('a')[0].text
	cost = equity.find_elements_by_tag_name('a')[1].text[1:]
	cost = float(cost.replace(',',''))
	quantity = int(equities[0].find_elements_by_tag_name('td')[1].text)
	# $3,339.46	
	# getting the cost basis cost of the stocks from bought.csv

# get orders
browser.get("https://client.schwab.com/Trade/OrderStatus/ViewOrderStatus.aspx?ViewTypeFilter=All")
orders_section = browser.find_elements_by_id("orders")
orders = orders_section.find_elements_by_class_name('header-ticket')
order_limitsellquant = {}
for order in orders:


for stock in f:
	ticker = stock.strip()
	print("==== setting initial limit for ", stock)
	browser.get(TRADE + ticker)
	
	action = Select(browser.find_element_by_id("ddlAction_0"))
	action.select_by_visible_text("Sell")
	
	# need to grab the quantity owned right now -- see above

	# need to grab the quantity we already have a limit sell for right now -- get from the bought.csv
	

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
	# check how many shares for which we have already set a limit sell -- check the bought.csv

	# if so, change the limit sell if needed, o/w set the limit sell -- using the same limit sell setting functionality above -- but first have to press cancel on the existing order

	# check the date when the shares were purchased, and put the limit sell for the appropriate amount based on that -- we should probably still retain the bought csv and store the dates when we bought each amount on our end 

	# if it's been over a year, sell the security so you can count the loss for tax purposes - list out the securities to sell -- again inferred from the bought.csv

