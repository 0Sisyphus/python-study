"""
给切片命名
"""
# 代码中如果有很多硬编码的索引值，将导致可读性和可维护性都不佳。
# 可以通过命名切片来解决这个问题。
# 命名切片的语法是在切片的中括号内加上一个名称，例如：

record = '....................100.......513.25..........'
SHARES = slice(20, 23)
PRICE = slice(30, 36)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)  # 51325.0

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a]) # [2, 3]

# 利用切片对象可以实现对列表的原地修改
items[a] = [10, 11]
print(items) # [0, 1, 10, 11, 4, 5, 6]

# 删除元素
del items[a]
print(items) # [0, 1, 4, 5, 6]


# 定义一个切片对象
s = slice(1, 10, 2)

# 打印切片对象的属性
print("Start:", s.start)
print("Stop:", s.stop)
print("Step:", s.step)

# indices方法
s = slice(1, 10, 2)
print(s.indices(5))  # (1, 5, 2)
s = slice(1, 100, 2)
a = 'helloWorld'
for i in range(*s.indices(len(a))):
    print(a[i]) # e l o W r d


