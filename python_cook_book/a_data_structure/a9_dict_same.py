"""
字典的相同点
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 查找相同key
print(a.keys() & b.keys())  # {'x', 'y'}

# 查找不同key
print(a.keys() - b.keys())  # {'z'}

# 查找相同value
print(set(a.values()) & set(b.values()))  # {2}

# 查找不同value
print(set(a.values()) - set(b.values()))  # {3, 1}

# 查找相同key和value
print(a.items() & b.items())  # {('y', 2)}

# 查找不同key和value
print(a.items() - b.items())  # {('z', 3), ('x', 1)}

# 创建一个新字典，移除部分key
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # {'x': 1, 'y': 2}


# 创建一个新字典，包括a和b中的key和value
# 合并字典
d = {**a, **b}
print(d)  # {'x': 11, 'y': 2, 'z': 3, 'w': 10}


