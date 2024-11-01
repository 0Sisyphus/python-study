"""
用迭代器取代 while 循环

关于内建函数 iter()，一个少有人知的特性是它可以选择性接受一个无参的可调用对象以及一个哨兵（结束）值作为输入。
当以这种方式使用时，iter()会创建一个迭代器， 然后重复调用用户提供的可调用对象，直到它返回哨兵值为止。

"""

import os
import tempfile

temp_dir = tempfile.mkdtemp()
file_path = os.path.join(temp_dir, 'passwd')  

# 往文件中写入一些数据
with open(file_path, 'wt') as f:
    f.write('root:x:0:0:root:/root:/bin/bash\n')
    f.write('daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n')
    f.write('bin:x:2:2:bin:/bin:/usr/sbin/nologin\n')



# 方案一：使用 while 循环

with open(file_path, 'rt') as f:
    print('迭代器输出结果:')
    while True:
        line = f.readline()
        if line == '':
            break
        print(line)

# 方案二：使用迭代器

with open(file_path, 'rt') as f:
    print('迭代器输出结果:')
    for line in iter(f.readline, ''):
        print(line)


# 清理文件
import shutil
shutil.rmtree(temp_dir)


