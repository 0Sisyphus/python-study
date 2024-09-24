"""
移除序列重复元素，并保持元素间顺序不变
"""

# 如果是list，使用set()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(set(a)))


# 手动实现（元素可哈希）
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


print(list(dedupe(a)))


# 元素不可hash
# 这里参数 key 的作用是指定一个函数用来将序列中的元素转换为可哈希的类型
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
