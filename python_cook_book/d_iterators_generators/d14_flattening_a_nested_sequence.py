"""
扁平化处理嵌套型的序列

我们有一个嵌套型的序列，想将它扁平化处理为一列单独的值。
"""

from collections.abc import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8, [9]]
    for x in flatten(items):
        print(x)

# 结果
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


