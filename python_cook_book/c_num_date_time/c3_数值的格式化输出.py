x = 1234.56789
# 保留小数
print(format(x, '0.2f'))  # 1234.57
print(format(x, '0.3f'))  # 1234.568
# 进行右对齐，总共占据 10 个字符的宽度，其中小数点后保留 1 位数字
print(format(x, '>10.1f'))  # ‘    1234.6’
# 进行左对齐，总共占据 10 个字符的宽度，其中小数点后保留 1 位数字
print(format(x, '<10.1f'))  # ‘1234.6    ’
# 进行居中对齐，总共占据 10 个字符的宽度，其中小数点后保留 1 位数字
print(format(x, '^10.1f'))  # ‘ 1234.6  ’
# 千位分隔符
print(format(x, ','))  # ‘1,234.56789’
print(format(x, '0,.1f'))  # ‘1,234.6’
# 用科学计数法表示
print(format(x, 'e'))  # ‘1.234568e+03’
print(format(x, '0.2E'))  # ‘1.23E+03’
# 百分数
print(format(x, '%'))  # ‘123456.789000%’
