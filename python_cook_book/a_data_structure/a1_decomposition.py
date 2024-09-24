"""
分解操作
"""
# 任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量
# 唯一的要求是变量的总数和结构要与序列相吻合
from collections import defaultdict

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name)  # ACME
print(day)  # 21

# 有时候，你可能只想分解其中一部分，丢弃其他的值。 对于这种情况 Python 并没有提供特殊的语法。 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了
_, shares, price, _ = data
print(shares)  # 50
print(price)  # 91.1

# 只要对象恰好是可迭代的，那么就可以执行分解操作。 这包括字符串、文件、迭代器以及生成器
s = 'Hello'
a, b, c, d, e = s
print(a)

