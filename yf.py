from selenium import webdriver
import csv

browser = webdriver.Firefox()
browser.get("https://www.gurufocus.com/stock/AAPL/summary")

markets = browser.find_elements_by_css_selector('button.el-button.fs-regular.el-button--danger.el-button--mini.el-popover__reference')
for market in markets:
    data = market.find_element_by_css_selector('span').text
    print(data)
    browser.quit()



















# # import yfinance as yf
# # import sys
# # data = yf.Ticker("FB")
# # tex = data.info.get('sector')
# # if tex == 'None':
# #     try:
# #         ('Oops',sys.exc_info())
# #     except:
# #         print(tex)
# from selenium import webdriver
# import csv
# import sys
# datas = []
# import yfinance as yf
# def open_yahoo(url_obj):
#     yf.pdr_override()
#     reader = csv.DictReader(url_obj,delimiter = ',')
#     for line in reader:
#         title = line["Stock"]
#         browser = webdriver.Chrome()
#         browser.get("https://www.gurufocus.com/stock/"+title+"/summary")
#         gurus = browser.find_elements_by_css_selector("button.el-button.fs-regular.el-button--danger.el-button--mini.el-popover__reference")
#         for guru in gurus:
#             data = guru.find_element_by_css_selector("span").text
#             datas.append(data)
#             # print(data)
#         try:
#             title = line["Stock"]
#             data = yf.Ticker(title)
#             mar = (data.info.get('sector'))
#             print(mar + str(data))
#         except:
#             print('Oops!',sys.exc_info())
#             print()

# if __name__ =="__main__":
#     with open("tickers1.csv") as url_obj:
#         open_yahoo(url_obj)