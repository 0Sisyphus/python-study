"""
字典的运算
"""

# 1. 求字典的键的最小值和最大值
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 如果直接用max(). min()，发现只处理键
print(max(prices))  # IBM
print(min(prices))  # AAPL
# 可以直接比较值，但无法获取key信息
print(max(prices.values()))  # 612.78
print(min(prices.values()))  # 10.75
# 可以通过lambda表达式来实现，但无法获取value信息
print(max(prices, key=lambda k: prices[k]))  # AAPL
print(min(prices, key=lambda k: prices[k]))  # FB
print(prices[max(prices, key=lambda k: prices[k])])  # 612.78
print(prices[min(prices, key=lambda k: prices[k])])  # 10.75
# 如果既想要key又想要value，可以通过使用zip()函数来将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (612.78, 'AAPL')
print(min_price)  # (10.75, 'FB')

# 当涉及（value, key）对的比较时，如果碰巧有多个条目拥有相同的 value 值，那么此时 key 将用来作为判定结果的依据
prices = {
    'AA': 45.23,
    'BB': 45.23
}
print(max(zip(prices.values(), prices.keys())))  # (45.23, 'BB')
print(min(zip(prices.values(), prices.keys())))  # (45.23, 'AA')

# 2. 排序
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)  # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

