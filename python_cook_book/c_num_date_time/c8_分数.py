# fractions 模块可以用来处理涉及分数的数学计算问题

from fractions import Fraction

a = Fraction(5, 4)  # 5/4
b = Fraction(7, 16)
print(a + b)  # 27/16
print((a + b) == Fraction(27, 16))  # True
print(a * b)  # 35/64

# 获取分子、分母
c = a * b
print(c.numerator)  # 35
print(c.denominator)  # 64

# 转化为浮点数
print(float(c))  # 0.546875

# 限制分母
print(c.limit_denominator(8))  # 7/8

# 转化小数为分数
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)  # 3/4

