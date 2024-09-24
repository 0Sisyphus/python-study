"""
分组
"""

import itertools
from operator import itemgetter

# 使用itertools分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 先排序
rows.sort(key=lambda r: r['date'])
# 再分组
# groupby()只能检查连 续的项，不首先排序的话，将无法按所想的方式来对记录分组
# for date, items in itertools.groupby(rows, key=lambda r: r['date']):
for date, items in itertools.groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
