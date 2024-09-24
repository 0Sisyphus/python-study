"""
同时对数据做转换和换算
"""

# 使用生成式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# 可以使用map()函数
s = sum(map(lambda x: x * x, nums))
print(s)



