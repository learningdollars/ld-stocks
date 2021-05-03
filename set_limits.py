from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# constants
TRADE = "https://client.schwab.com/Areas/Trade/Stocks/Entry.aspx?Symbol="
WKLY_GROWTH_EXPECTATION = 1.0072

browser = webdriver.Chrome()
browser.get("https://client.schwab.com/")
print("waiting for user to login")
time.sleep(5)

# can go through stocks we own now
browser.get("https://client.schwab.com/Areas/Accounts/Positions")
equities = browser.find_elements_by_xpath('//tr[@data-pulsr-securitygroup="Equity"]')
owned_equities = {}
for equity in equities:
	ticker = equity.find_elements_by_tag_name('a')[0].text
	owned_equities[ticker] = {}
	owned_equities[ticker]["cost"] = float(equity.find_elements_by_tag_name('a')[1].text[1:].replace(',',''))
	owned_equities[ticker]["quantity"] = int(equities[0].find_elements_by_tag_name('td')[1].text)
	print(ticker, owned_equities[ticker]["cost"], owned_equities[ticker]["quantity"])

# get existing limit orders and reset them
browser.get("https://client.schwab.com/Trade/OrderStatus/ViewOrderStatus.aspx?ViewTypeFilter=All")
cancels = browser.find_elements_by_class_name("link-cancel.button-secondary.rightClickDisable")
for i in len(cancels):
	cancel = browser.find_elements_by_class_name("link-cancel.button-secondary.rightClickDisable")[i]
	cancel.find_element_by_xpath('..')
	whole_limit_call = cancel.find_element_by_xpath('../../../..')
	num_limit_sell = int(whole_limit_call.find_elements_by_tag_name("td")[1].text.split(" ")[0])
	limit_price = float(whole_limit_call.find_elements_by_tag_name("td")[2].text.split(" ")[1].replace("$", "").replace(",", ""))
	relevant_ticker = whole_limit_call.get_attribute('innerHTML').split("Symbol=")[1].split('&amp')[0]
	print("need to adjust limit for", relevant_ticker, num_limit_sell, "shares, curr limit", limit_price)
	cancel.click()
	time.sleep(3)
	confirmation = browser.find_element_by_link_text("Cancel Order")
	confirmation.click()
	time.sleep(3)
	close.click()


# minimize dependencies
# read the csv of stock, date, num shares
# print out the purchase prices to add for each of them
# copy and paste them in
# reget the the csv
# set limit options on new purchases
# cancel + set for old ones that need new

# still need to decide whether spreadsheet or inference is best 

# way to go about it - set the limit every week (round) to the next level required
# so 1.0075, 1.015, is basically 1.45^(n/52), oh so it's just multiply by 1.0072 each week
# now you know the cost basis, the limit option amount, 

orders_section = browser.find_element_by_id("orders")
orders = orders_section.find_elements_by_class_name('header-ticket')

f = open("bought.csv")

	# $3,339.46	
	# getting the cost basis cost of the stocks from bought.csv

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

