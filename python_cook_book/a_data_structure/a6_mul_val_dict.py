"""
在字典中将键映射到多个值上
"""

from collections import defaultdict


# 1.直接创建字典
d = {'a': [1, 2, 3],
     'b': [4, 5]}
print(d)
# 2.使用setdefault()方法
# 列表可重复
d = {}
# d['a'].append(1)
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(3)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(5)
print(d)

# 集合不可重复
s = {}
s.setdefault('a', set()).add(1)
s.setdefault('a', set()).add(2)
s.setdefault('a', set()).add(2)
s.setdefault('a', set()).add(3)
s.setdefault('b', set()).add(4)
s.setdefault('b', set()).add(5)
print(s)

# 3.使用defaultdict()
# 列表可重复
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)

# 集合不可重复
s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['a'].add(2)
s['a'].add(3)
s['a'].add(3)
s['b'].add(4)
s['b'].add(5)
print(s)
