from selenium import webdriver
import sys

browser = webdriver.Firefox()
browser.get("https://markets.businessinsider.com/stocks/msft-stock")
earnings = browser.find_elements_by_class_name("price-section__row")
for earning in earnings:
    try:
        title = earning.find_element_by_css_selector("span.price-section__current-value").text
        if title > "1":
            title = "YES"
        else:
            title = "NO"
        browser.quit()
    except:
        ("Oops",sys.exc_info)
    
    print(title)