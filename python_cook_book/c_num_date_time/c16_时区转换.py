# 使用pytz模块
from datetime import datetime

import pytz
from pytz import timezone

d = datetime.now()
print(d)
# 美国芝加哥时间
central = timezone('US/Central')
us_d = central.localize(d)
print(us_d)
# 中国上海时间
central = timezone('Asia/Shanghai')
cn_d = central.localize(d)
print(cn_d)
# 日本东京时间
central = timezone('Asia/Tokyo')
jp_d = central.localize(d)
print(jp_d)

# 世界统一时间
utc_d = jp_d.astimezone(pytz.utc)
print(utc_d)
