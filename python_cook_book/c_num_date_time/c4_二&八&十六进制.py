x = 1234
# 二进制
print(bin(x))
# 八进制
print(oct(x))
# 十六进制
print(hex(x))
# 如果不想出现前缀，可以使用format
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
# 字符串形式的整数转换为不同的进制
print(int('4d2', 16))
print(int('10011010010', 2))
# 将 y 转换为 32 位二进制补码形式
y = -1234
binary_str = format(2**32 + y, 'b')
print(binary_str)