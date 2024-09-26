import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)  # inf
print(b)  # -inf
print(c)  # nan

# 判断
print(math.isinf(a))  # True
print(math.isnan(c))  # True

d = float('nan')
print(d + 23)


c = float('nan')
d = float('nan')
print(c == d) # False
print(c is d) # False