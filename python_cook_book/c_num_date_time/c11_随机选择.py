import random

values = [1, 2, 3, 4, 5, 6]

# 取一个元素
for i in range(10):
    print(random.choice(values))

# 取多个元素
for i in range(10):
    print(random.sample(values, 3))

# 原地打乱
random.shuffle(values)
print(values)

# 生产随机数
for i in range(10):
    print(random.randint(0, 10))

# 生产0-1的浮点数
for i in range(10):
    print(random.random())

# 生产由N个随机比特位组成的整数
print(random.getrandbits(200))

# random 模块采用马特赛特旋转算法（Mersenne Twister，也称为梅森旋转算法）来计算 随机数。
# 这是一个确定性算法，但是可以通过 random.seed()函数来修改初始的种子值。
random.seed()  # 系统当前时间 or os.urandom()
random.seed(12345)  # 整数
random.seed(b'bytedata')  # 字节串
