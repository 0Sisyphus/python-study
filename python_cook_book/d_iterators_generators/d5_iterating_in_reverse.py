"""
反向迭代
"""
# 1.使用内建函数 reversed()
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 反向迭代只有在待处理的对象拥有可确定的大小，或者对象实现了__reversed__()特殊 方法时，才能奏效
# 如果上述两个条件都无法满足，则必须将这个对象转换为列表
# 但转换为list可能会占用大量的内存

f = open('../static/秋夜.txt')
for line in reversed(list(f)):
    print(line, end='')


# 可以手动实现__reversed__()方法，自定义反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)


