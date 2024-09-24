"""
命名元组
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('EMAIL', '2012-10-19')
print(sub)

# 可以像使用对象一样使用命名元组
print(sub.addr)
print(sub.joined)

# 但它仍是元组，支持元组的所有操作
print(len(sub))
addr, joined = sub
print(addr, joined)

# 应用：可以将数据封装到元组中，避免使用下标访问
# 如下从数据库中查询记录，封装到命名元组中，像对象一样访问
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 但元组不支持修改元素，所以如果需要修改元素，需要使用命名元组的_replace()方法
# 该方法会创建一个全新的命名元组，并对相应的值做替换
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
print(s)

# 也可以使用通过命名元组的_replace()方法来创建新的实例
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# 原型
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
