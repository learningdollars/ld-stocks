import datetime
import time


def next_week_dates():
    next_week = (datetime.date.today().isocalendar()[1]) + 1
    week = next_week - 2
    start_date = time.asctime(time.strptime('2020 %d 0' % week, '%Y %W %w'))
    start_date = datetime.datetime.strptime(start_date, '%a %b %d %H:%M:%S %Y')
    dates = [start_date.strftime('%Y-%m-%d')]
    for i in range(1, 7):
        day = start_date + datetime.timedelta(days=i)
        dates.append(day.strftime('%Y-%m-%d'))
    print(dates)


next_week_dates()