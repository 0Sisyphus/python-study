def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# 生成器只会在响应迭代操作时才运作
# 使用这个函数，可以使用for循环对其迭代，或者通过其他可以访问可迭代对象中的元素的函数，如sum()，list()
for n in frange(0, 4, 0.5):
    print(n)

l = list(frange(0, 1, 0.125))
print(l)

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print("Done")

c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
