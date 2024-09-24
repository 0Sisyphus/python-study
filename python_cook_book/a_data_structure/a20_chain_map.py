"""
多个字典合并
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c)  # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
# 但取值时，会按照顺序查找
print(c['x'])  # 1
print(c['y'])  # 2
print(c['z'])  # 3
# 长度
print(len(c))  # 3
# 键
print(list(c.keys()))  # ['y', 'z', 'x']
# 值
print(list(c.values()))  # [2, 3, 1]
# 对chainMap的修改也只反应在第一个字典上
c['z'] = 10
c['w'] = 40
del c['x']
print(a)  # {'z': 10, 'w': 40}
print(b)  # {'y': 2, 'z': 4}

values = ChainMap()
values['x'] = 1
# 添加新的映射
values = values.new_child()
values['x'] = 2
# 添加新的映射
values = values.new_child()
values['x'] = 3
print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1}, {})
print(values['x'])  # 3
# 丢弃最后一个映射
values = values.parents
print(values['x'])  # 2
values = values.parents
print(values['x'])  # 1
values = values.parents
print(values)  # ChainMap({})

# 合并字典
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)  # {'y': 2, 'z': 3, 'x': 1}
# 但这种方式会创建一个新的字典，原来的字典不会被修改
