import yfinance as yf
data = yf.Ticker("BRK.A")
print(data.info)
import csv

# import yfinance as yf
# def open_yahoo(url_obj):
#     yf.pdr_override()
#     reader = csv.DictReader(url_obj,delimiter = ',')
#     for line in reader:
#         title = line["Stock"]
#         data = yf.Ticker(title)
#         print(data.info.get('sector'))

# if __name__ =="__main__":
#     with open("sheet1.csv") as url_obj:
#         open_yahoo(url_obj)