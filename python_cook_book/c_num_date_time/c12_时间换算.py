from datetime import timedelta
# timedelta的作用是表示两个时间之间的差值，或者用来创建一个时间间隔。
# timedelta 对象的构造函数接受以下参数：
# days：天数，可以是正数或负数。
# seconds：秒数，可以是正数或负数。
# microseconds：微秒数，可以是正数或负数。
# milliseconds：毫秒数，可以是正数或负数。
# minutes：分钟数，可以是正数或负数。
# hours：小时数，可以是正数或负数。
# weeks：星期数，可以是正数或负数。
# timedelta不能使用月份参数
a = timedelta(days=2, hours=6)
print(a)
b = timedelta(hours=4.5)
print(b)
c = a + b
print(c)
print(c.days)
print(c.seconds)
print(c.total_seconds())

# 表示具体时间
from datetime import datetime
a = datetime(2012, 9, 13)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d) # 99 days, 0:00:00
# 获取当前时间
now = datetime.today()
print(now)

# from dateutil.relativedelta import relativedelta 无法安装

