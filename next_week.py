import datetime

def next_weekday(today_date,weekday):
    days_ahead = weekday-today_date.weekday()
    if days_ahead <=0:
        days_ahead +=6
    return today_date + datetime.timedelta(days_ahead)
def next_sunday(today_date,weekday):
    days_ahead = weekday - today_date.weekday()
    if days_ahead <=0:
        days_ahead +=12
    return today_date +datetime.timedelta(days_ahead)
def the_date(today_date,weekday):
    days_ahead = weekday-today_date.weekday()
    if days_ahead <=0:
        days_ahead +=7
    return today_date + datetime.timedelta(days_ahead)
today_date = datetime.date.today()
next_monday = (next_weekday(today_date,0).strftime('%Y-%m-%d'))
next_suny = (next_sunday(today_date,0).strftime('%Y-%m-%d'))
day_picked = (the_date(today_date,0).strftime('%Y-%m-%d'))