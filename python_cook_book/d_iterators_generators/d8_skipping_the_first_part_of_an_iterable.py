"""
跳过可迭代对象中的前一部分元素
"""
from itertools import dropwhile, islice

## 1. itertools.dropwhile()

# 跳过可迭代对象中开始部分满足某个特定测试的元素，从第一个满足测试的元素开始返回
with open('../static/秋夜.txt') as f:
    for line in dropwhile(lambda line: '秋夜' in line, f):
        print(line, end='')

## 2. itertools.islice

# 在这个例子中，islice()的最后一个参数 None 用来表示想要前 3 个元素之外的所有元素，
# 而不是只要前 3 个元素
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
