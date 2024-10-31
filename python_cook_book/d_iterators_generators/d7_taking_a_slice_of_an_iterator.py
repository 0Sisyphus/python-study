"""
对迭代器做切片操作

迭代器和生成器是没法执行普通的切片操作的，这是因为不知道它们的长度是多少（而 且它们也没有实现索引）。
islice()产生的结果是一个迭代器，它可以产生出所需要的切 片元素，
但这是通过访问并丢弃所有起始索引之前的元素来实现的。
之后的元素会由 islice 对象产生出来，直到到达结束索引为止

"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)

import itertools

for x in itertools.islice(c, 10, 20):
    print(x)
