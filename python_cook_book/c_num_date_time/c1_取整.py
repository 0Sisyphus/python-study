# 小数位
x = 1.2355
print(round(x, 2))  # 1.24
# 当某个值恰好等于两个整数间的一半时，取整操作会取到离该值最接近的那个偶数上。
print(round(x, 3))  # 1.236

# 格式化输出
print(format(x, '0.2f'))  # 1.24
print(format(x, '0.3f'))  # 1.236

# 十位、百位、千位
a = 1627731
print(round(a, -1))  # 1627730
print(round(a, -2))  # 1627700
print(round(a, -3))  # 1628000
