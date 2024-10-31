"""
以索引-值对的形式迭代序列
"""

# enumerate
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 可以传起始位置
for idx, val in enumerate(my_list, 1):
    print(idx, val)


with open('../static/秋夜.txt') as f:
    for lineno, line in enumerate(f, 1):
        try:
            print(line)
        except ValueError as e:
            print('Line {}: Parse error: {}'.format(lineno, e))



