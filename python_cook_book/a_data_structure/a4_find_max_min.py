"""
最大值最小值
"""
# 一、使用heapq中的两个函数：nlargest() 和 nsmallest()
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

# 复杂数据结构可以使用lambda表达式处理
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap) # -4

# 二、使用max()和min()函数
# 找出列表中的最大值和最小值
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(max(nums))  # 输出: 42
print(min(nums))  # 输出: -4

# 使用key参数，根据字符串长度找出最长和最短的字符串
words = ['apple', 'banana', 'cherry', 'date']
print(max(words, key=len))  # 输出: banana
print(min(words, key=len))  # 输出: date

# 可迭代对象为空时，使用default参数
empty_list = []
print(max(empty_list, default='The list is empty'))  # 输出: The list is empty
print(min(empty_list, default='The list is empty'))  # 输出: The list is empty
