from datetime import datetime

# 字符串转换为日期
text = '2024-09-23'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)  # 2024-09-23 00:00:00
z = datetime.now()
diff = z - y
print(diff)

# 日期转换为字符串
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)  # Sunday September 23, 2024
nice_z = datetime.strftime(z, '%Y-%m-%d')
print(nice_z)  # 2024-09-23


# 但是strptime纯python实现，性能糟糕
# 可以手动实现，如：
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


print(parse_ymd('2024-09-23'))  # 2024-09-23 00:00:00
