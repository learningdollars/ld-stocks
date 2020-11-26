import datetime

def next_weekday(today_date,weekday):
    days_ahead = weekday-today_date.weekday()
    if days_ahead <=0:
        days_ahead +=7
    return today_date + datetime.timedelta(days_ahead)
def next_sunday(today_date,weekday):
    days_ahead = weekday - today_date.weekday()
    if days_ahead <=0:
        days_ahead +=13
    return today_date +datetime.timedelta(days_ahead)

today_date = datetime.date.today()
next_monday = (next_weekday(today_date,0).strftime('%m/%d/%Y'))
next_suny = (next_sunday(today_date,0).strftime('%m/%d/%Y'))
# print(next_suny)
# print(next_monday)


# browser = webdriver.Firefox()
# browser.get("https://markets.businessinsider.com/earnings-calendar#date=11/30/2020-12/06/2020&name=&countries=&eventtypes=103,99&tab=ALL")
# # WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Microsoft Corp.']"))).click()
# # browser.quit()
# next_weeks = browser.find_elements_by_css_selector("table.table.instruments.calendar-grid")
# for next_week in next_weeks:
#     let = browser.find_element_by_css_selector("td:nth-child(3)").text
#     # print(let)
#     if let == "Annual General Meeting":
#         # WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Microsoft Corp.']"))).click()
#         ("DOnt Scrape")
#     else:
#         try:
#             title = next_week.find_element(By.CSS_SELECTOR,"table.table.instruments.calendar-grid tbody tr td a strong").text
#             # WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,title))).click()
#             # browser.get("https://markets.businessinsider.com/stocks/"+title+"-stock").click()
#             WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='"+title+"']"))).click()
#             earnings = browser.find_elements_by_class_name("price-section__row")
#             for earning in earnings:
#                 try:
#                     title = earning.find_element_by_css_selector("span.price-section__current-value").text
#                     if title > "1":
#                         print("YES")
#                     else:
#                         print("NO")
#                 except:
#                     print('Oops',sys.exc_info())
#             browser.back()
#         except:
#             print(sys.exc_info())