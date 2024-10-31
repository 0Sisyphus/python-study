# 定义自定义容器对象，内部有一个列表，列表中元素可以迭代
# 使用__iter__()方法，将迭代请求委托到对象内部持有的容器上
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

# Python的迭代协议要求 __iter__()返回一个特殊的迭代器对象，由该对象实现的 __next__()方法来完成实际的迭代
