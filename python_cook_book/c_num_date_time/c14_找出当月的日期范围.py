import calendar
from datetime import datetime, timedelta


def get_month_range(start_date=None):
    if start_date is None:
        start_date = datetime.today()
    # 返回指定年份和月份的第一天是星期几，以及这个月有多少天
    a, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    # 获取这个月的第一天和最后一天
    start_date = start_date.replace(day=1)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


first_day, last_day, = get_month_range()

for d in date_range(first_day, last_day, timedelta(days=1)):
    print(d)
