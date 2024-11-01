"""
合并多个有序序列，再对整个有序序列进行迭代

我们有一组有序序列，想对它们合并在一起之后的有序序列进行迭代。

使用 heapq.merge() 函数。heapq.merge 的迭代性质意味着它对所有提供的序列都不会做一次性读取。
这意味着可以利用它处理非常长的序列，而开销却非常小。

需要重点强调的是， heapq.merge()要求所有的输入序列都是有序的。
特别是，它不会首先将所有的数据读取到堆中，或者预先做任何的排序操作。
它也不会对输入做任何验证，以检查它们是否满足有序的要求。
相反，它只是简单地检查每个输入序列中的第一个元素，将最小的那个发送出去。
然后再从之前选择的序列中读取一个新的元素， 再重复执行这个步骤，直到所有的输入序列都耗尽为止。

"""
# 使用 heapq.merge() 函数的简单示例
import heapq


a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
# 结果
# 1
# 2
# 4

# 使用 heapq.merge() 函数合并文件
import os
import tempfile

# 创建临时目录
temp_dir = tempfile.mkdtemp()
file1_path = os.path.join(temp_dir, 'sorted_file_1')
file2_path = os.path.join(temp_dir, 'sorted_file_2')
merged_path = os.path.join(temp_dir, 'merged_file')

# 创建临时测试文件
with open(file1_path, 'wt') as f1:
    f1.write('1\n3\n5\n7\n')
    
with open(file2_path, 'wt') as f2:
    f2.write('2\n4\n6\n8\n')

# 合并文件
with open(file1_path, 'rt') as file1, \
    open(file2_path, 'rt') as file2, \
    open(merged_path, 'wt') as outf:
    
    for line in heapq.merge(file1, file2):
        outf.write(line)

# 验证结果
with open(merged_path, 'rt') as f:
    print('合并后的文件内容:')
    print(f.read())

# 清理测试文件
import shutil
shutil.rmtree(temp_dir)

