from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('../static/秋夜.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if '鸟' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

# 如果打算用除了 for 循环之外的技术来 驱动迭代过程的话，可能需要额外调用一次 iter()
with open('../static/秋夜.txt') as f:
    f = linehistory(f)
    it = iter(f)
    try:
        while True:
            line = next(it)
            if '鸟' in line:
                for lineno, hline in f.history:
                    print('{}:{}'.format(lineno, hline), end='')
    except StopIteration:
        pass
