# 使用decimal模块

from decimal import Decimal, localcontext

a = 4.2
b = 2.1
print(a + b)  # 6.300000000000001
print((a + b) == 6.3)  # False

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)  # 6.3
print((a + b) == Decimal('6.3'))  # True

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)  # 0.7647058823529411764705882353

# 控制计算的位数
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)  # 0.765

