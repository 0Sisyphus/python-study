from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# 获取上一个周几的日期
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    # 绝对值
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(get_previous_byday('Monday'))  # 2024-09-23 17:52:46.388505
print(get_previous_byday('Sunday', datetime(2024, 10, 1)))  # 2024-09-29 00:00:00


# 获取当前周中某天的日期
def get_current_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    # 绝对值
    day_sub = abs(day_num_target - day_num)
    days_ago = (7 + day_sub) % 7
    if days_ago == 0:
        days_ago = 7
    if day_num_target < day_num:
        days_ago = - days_ago
    target_date = start_date + timedelta(days=days_ago)
    return target_date


print(get_current_byday('Monday'))  # 2024-09-23 17:52:46.388653
print(get_current_byday('Sunday', datetime(2024, 10, 1)))  # 2024-10-06 00:00:00
