"""
在不同的容器中进行迭代

我们需要对许多对象执行相同的操作，但是这些对象包含在不同的容器内，而我们希 望可以避免写出嵌套的循环处理，保持代码的可读性。

itertools.chain()函数常见的用途是想一次性对所有的元素执行某项特定的操作，但是这些 元素分散在不同的集合中。
它接受一系列可迭代对象作为输入并返回 一个迭代器，这个迭代器能够有效地掩盖一个事实—你实际上是在对多个容器进行迭代。

"""
from itertools import chain

# 使用chain()函数将多个序列合并成一个迭代器
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
# 输出:
# 1
# 2
# 3
# 4
# x
# y
# z



