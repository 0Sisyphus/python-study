"""
筛选序列中的元素
"""
# 使用列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 筛选后可以对数据进行操作
print([n * 2 for n in mylist if n > 0])
print([n * 2 for n in mylist if n < 0])

# 也可以对不满足的数据替换
print([n if n > 0 else 0 for n in mylist])
print([n if n < 0 else 0 for n in mylist])

# 如果数据量特别大，可以考虑使用生成器表达式
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)


# 如果筛选过程很复杂，可以将复杂的逻辑写在一个单独的函数中
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# 过滤条件的函数可以是任何可调用对象，比如函数、方法、lambda表达式等
ivals = list(filter(is_int, values))
print(ivals)

# itertools.compress() 函数可以按照另一个序列的布尔值选择元素
# 当想要把一个序列的筛选结果施加到另一个相关的序列上时会非常有用
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5) # [False, False, True, False, False, True, True, False]
print(list(compress(addresses, more5))) # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
