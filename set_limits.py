from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import time
import sys

# constants
WKLY_GROWTH_EXPECTATION = 1.0072
REGULAR_LIMIT_URL = "https://client.schwab.com/Areas/Trade/Stocks/Entry.aspx?Symbol="
EXTENDED_HOURS_LIMIT_URL = "https://client.schwab.com/Areas/Trade/Stocks/ExtendedHours/Entry.aspx"
SCHWAB_HOME = "https://client.schwab.com/"
POSITIONS = "https://client.schwab.com/Areas/Accounts/Positions"
ORDERS = "https://client.schwab.com/Trade/OrderStatus/ViewOrderStatus.aspx?ViewTypeFilter=All"

def set_regular_limit_option(relevant_ticker, num_limit_sell, limit_price, browser):
	browser.get(REGULAR_LIMIT_URL+relevant_ticker)
	action = Select(browser.find_element_by_id("ddlAction_0"))
	action.select_by_visible_text("Sell")
	quantity_input = browser.find_element_by_id("txtQty_0")
	quantity_input.send_keys(str(num_limit_sell))
	ordertype = Select(browser.find_element_by_id("ddlType_0"))
	ordertype.select_by_visible_text("Limit")
	limitamt_input = browser.find_element_by_id("txtLimit_0")
	limitamt_input.send_keys(str(limit_price*WKLY_GROWTH_EXPECTATION))
	timing = Select(browser.find_element_by_id("ddlTiming_0"))
	timing.select_by_visible_text("Good Until Canceled")
	review_order = browser.find_element_by_id("btnReview")
	review_order.click()
	time.sleep(3)
	confirm = browser.find_element_by_id("btnConfirm")
	confirm.click()
	print("set regular limit option for", relevant_ticker)

def set_extended_hours_limit_option(relevant_ticker, num_limit_sell, limit_price, browser):
	browser.get(EXTENDED_HOURS_LIMIT_URL)
	symbol_input = browser.find_element_by_id("txtSym_0")
	symbol_input.send_keys(relevant_ticker)
	symbol_input.send_keys(Keys.RETURN)
	action = Select(browser.find_element_by_id("ddlAction_0"))
	action.select_by_visible_text("Sell")
	quantity_input = browser.find_element_by_id("txtQty_0")
	quantity_input.send_keys(num_limit_sell)
	limit_input = browser.find_element_by_id("txtLimit_0")
	limit_input.send_keys(limit_price*WKLY_GROWTH_EXPECTATION)
	review = browser.find_element_by_id("btnReview")
	review.click()
	time.sleep(3)
	confirm = browser.find_element_by_id("btnConfirm")
	confirm.click()
	print("set extended hours limit option for", relevant_ticker)

version = sys.argv[1]
browser = webdriver.Chrome()
browser.get(SCHWAB_HOME)
print("waiting for user to login")
time.sleep(10 + random.random())

# can go through stocks we own now
browser.get(POSITIONS)
time.sleep(3 + random.random())
equities = browser.find_elements_by_xpath('//tr[@data-pulsr-securitygroup="Equity"]')
owned_equities = {}
print("=== owned equities ===")
for equity in equities:
	try:
		ticker = equity.find_elements_by_tag_name('a')[0].text
		owned_equities[ticker] = {}
		owned_equities[ticker]["cost"] = float(equity.find_elements_by_tag_name('a')[1].text[1:].replace(',',''))
		owned_equities[ticker]["quantity"] = int(equities[0].find_elements_by_tag_name('td')[1].text)
		print(ticker, owned_equities[ticker]["cost"], owned_equities[ticker]["quantity"])
	except:
		print("failed on this stock, moving to next")

# get existing limit orders and reset them
browser.get(ORDERS)
time.sleep(3 + random.random())
cancels = browser.find_elements_by_class_name("link-cancel.button-secondary.rightClickDisable")
print("=== existing limits to reset ===")
for i in range(0, len(cancels)):
	#try:
	browser.get("https://client.schwab.com/Trade/OrderStatus/ViewOrderStatus.aspx?ViewTypeFilter=All")
	time.sleep(3 + random.random())
	cancel = browser.find_elements_by_class_name("link-cancel.button-secondary.rightClickDisable")[i]
	cancel.find_element_by_xpath('..')
	whole_limit_call = cancel.find_element_by_xpath('../../../..')
	num_limit_sell = int(whole_limit_call.find_elements_by_tag_name("td")[1].text.split(" ")[0])
	limit_price = float(whole_limit_call.find_elements_by_tag_name("td")[2].text.split(" ")[1].replace("$", "").replace(",", ""))
	relevant_ticker = whole_limit_call.get_attribute('innerHTML').split("Symbol=")[1].split('&amp')[0]
	time.sleep(3 + random.random())
	# note we only want to cancel the existing limit options if it's during the regular period, if early period we let the old ones remain
	if version == "regular": 	
		print("YES need to adjust limit for", relevant_ticker, num_limit_sell, "shares, curr limit", limit_price)	
		# first cancel the current limit sell
		cancel.click()
		time.sleep(3 + random.random())
		confirmation = browser.find_element_by_link_text("Cancel Order")
		confirmation.click()
		time.sleep(3 + random.random())
		close.click()
		# now reset it
		set_regular_limit_option(relevant_ticker, num_limit_sell, limit_price, browser)
	else:
		print("NO need to adjust limit for", relevant_ticker, num_limit_sell, "shares, curr limit", limit_price, "- in early hours")
	owned_equities[ticker]["number_limit_adjusted"] += 1
	time.sleep(3 + random.random())
	#except:
	#	print("failed on this stock, moving to next")

print("=== set limits ===")
# set initial limit sells
time.sleep(3 + random.random())
if version == "early":
	for ticker, oe in owned_equities.items():
		#try:
		set_regular_limit_option(ticker, oe["quantity"] - oe["number_limit_adjusted"], oe["cost"], browser)
		#except:
		#	print("failed on this stock, moving to next")

# set extended hours limit sells
time.sleep(3 + random.random())
if version == "regular":
	for ticker, oe in owned_equities.items():
		try:
			set_extended_hours_limit_option(ticker, oe["quantity"] - oe["number_limit_adjusted"], oe["cost"], browser)
		except:
			print("failed on this stock, moving to next")

print("don't forget to copy and paste the output into the running_log.txt, with the date")
