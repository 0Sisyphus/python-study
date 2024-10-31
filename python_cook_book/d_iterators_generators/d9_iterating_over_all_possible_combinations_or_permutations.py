"""
迭代所有可能的组合或排列
"""

# 1.itertools.permutations
# 它接受一个元素集合，将其中所有的元素重排列为所有可能的情况，并以元组序 列的形式返回（即，将元素之间的顺序打乱成所有可能的情况）
items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
    print(p)
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')


# 如果想得到指定长度的所有排列，可 以给它传递一个可选的长度参数
for p in permutations(items, 2):
    print(p)

# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')

# 2.itertools.combinations
# 可产生输入序列中所有元素的全部组合形式
# 对于 combinations()来说，元素之间的实际顺序是不予考虑的。
# 也就是说，组合('a', 'b') 和组合('b', 'a')被认为是相同的组合形式（因此只会产生出其中一种）。
from itertools import combinations
for c in combinations(items, 3):
    print(c)
# ('a', 'b', 'c')

for c in combinations(items, 2):
    print(c)
# ('a', 'b')
# ('a', 'c')
# ('b', 'c')

# 3.itertools.combinations_with_replacement
# 允许相同的元素得到多次选择
from itertools import combinations_with_replacement

for c in combinations_with_replacement(items, 3):
    print(c)
# ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')