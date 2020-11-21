import csv
from selenium import webdriver

import pandas as pd
stock_name = []
rate = []
# function
def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimiter = ',')
    browser = webdriver.Chrome()
    for line in reader:
        try:
            url = line["URL"]
            title = line["Title"]
            # print(url +' ' + title)
            browser.get(url)
            stockname = browser.find_elements_by_css_selector('header.Jo5RGrWjFiX_iyW3gMLsy')
            for stock in stockname:
                name = stock.find_element_by_css_selector('h1').text
                stock_name.append(name)
            ratings = browser.find_elements_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92')
            for rating in ratings:
                rat = rating.find_element_by_css_selector('div._1fEdz1YPOLpLW1Ow3rKh92 h2').text
                print(rat)
                if rat == ' ':
                    print('NA')
                rate.append(rat)
            assert title in browser.title
            df = pd.DataFrame(list(zip(stock_name,rate)), columns=['Stock_Name','Rating'])
            df.to_csv('Final.csv',index=False)
        except:
            print("NA")
    browser.quit()


if __name__ =="__main__":
    with open("tickers.csv") as url_obj:
        csv_url_reader(url_obj)
