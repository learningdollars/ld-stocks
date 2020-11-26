from selenium import webdriver
import sys
from selenium.common import exceptions
import csv
from next_week import next_suny
from next_week import next_monday

browser = webdriver.Chrome()
def csv_url(url_obj):
    readers = csv.DictReader(url_obj)
    for reader in readers:
        predecision = reader["Predecision"]
        title = reader["Stock"]
        print(title + " "+ predecision)
        if predecision == "TRUE":
            try:
                browser.get("https://markets.businessinsider.com/earnings-calendar#date="+next_monday+"-"+next_suny+"&name=&countries=&eventtypes=103,99&tab=ALL")
                check_earnings = browser.find_elements_by_css_selector("table.table.instruments.calendar-grid")
                for check_earning in check_earnings:
                    check_event = check_earning.find_element_by_css_selector("tr td:nth-child(3)").text
                    if check_event == "MID CAP" or check_event == "Annual General Meeting":
                        ("Dont Scrape")
                    else:
                        browser.get("https://markets.businessinsider.com/stocks/"+title+"-stock")
                        earning_clicks = browser.find_elements_by_class_name("price-section__row")
                        for earning_click in earning_clicks:
                            try:
                                money = earning_click.find_element_by_css_selector("span.price-section__current-value").text
                                if money > "0":
                                    money = "YES"
                                else:
                                    money = "NO"
                            except:
                                sys.exc_info()
            except exceptions.StaleElementReferenceException:
                pass
            browser.quit()
        # Print NA if predecision is NOT TRUE
        else:
            print("NA")


if __name__ =="__main__":
    with open("tickers1.csv") as url_obj:
        csv_url(url_obj)