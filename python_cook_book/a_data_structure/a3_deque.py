"""
队列
"""
# deque(maxlen=N)创建了一个固定长度的队列。当有新记录加入而队列已满时会自动移 除最老的那条记录。
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)  # deque([3, 4, 5], maxlen=3)

# 如果不指定队列 的大小，也就得到了一个无界限的队列，可以在两端执行添加和弹出操作
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
q.append(5)
print(q)  # deque([4, 1, 2, 3, 5])
q.pop()
print(q)  # deque([4, 1, 2, 3])
q.popleft()
print(q)  # deque([1, 2, 3])


# 队列在文本匹配中也特别有用
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# 使用匹配函数
if __name__ == '__main__':
    with open('../static/秋夜.txt') as f:
        for line, plines in search(f, '枣树', 3):
            for pline in plines:
                print(pline, end='')
            print(line, end='')
            print('_' * 20)
