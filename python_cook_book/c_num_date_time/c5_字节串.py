data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data)
# 转换为数字
# 小端
print(int.from_bytes(data, 'little'))
# 大端
print(int.from_bytes(data, 'big'))
# 转换为字节串
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'little'))
print(x.to_bytes(16, 'big'))

# to_bytes 方法的第一个参数（即字节序列的长度）必须是一个正整数，
# 并且它的值必须与你要转换的整数的位数相匹配。
# 如果字节序列的长度小于整数的位数，将会抛出 OverflowError 异常。
# 如果字节序列的长度大于整数的位数，多余的字节将用 0 填充
x = 523 ** 23
# x.to_bytes(16, 'little') # int too big to convert
x.bit_length()
nbytes, rem = divmod(x.bit_length(), 8)
print(nbytes, rem)
if rem:
    nbytes += 1
print(nbytes)
print(x.to_bytes(nbytes, 'little'))