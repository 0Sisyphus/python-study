"""
创建数据处理管道 - 展示两种不同的处理方案
"""

# 生成器函数可以用来创建处理管道
def gen_find_files(filepat, top):
    """
    在目录树中查找与模式匹配的文件名
    """
    import os
    import fnmatch
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    """
    打开一系列文件
    """
    for filename in filenames:
        with open(filename, 'rt') as f:
            yield f

def gen_concatenate(iterators):
    """
    链接一系列迭代器
    """
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    """
    在行序列中查找正则表达式匹配
    """
    import re
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

def process_files_v1(test_dir):
    """
    方案一：先链接后处理
    优点：代码简单直观，处理流程清晰
    缺点：处理灵活性较低，难以并行化
    """
    lognames = gen_find_files('access-log*', test_dir)
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    return pylines

def process_single_file(file):
    """处理单个文件中的内容"""
    return gen_grep('(?i)python', file)

def process_files_v2(test_dir):
    """
    方案二：先处理后链接
    优点：
    1. 可以并行处理文件
    2. 更灵活，可以对不同文件使用不同处理逻辑
    3. 可以提前过滤无用数据
    缺点：代码稍微复杂一些
    """
    lognames = gen_find_files('access-log*', test_dir)
    files = gen_opener(lognames)
    processed_files = map(process_single_file, files)
    return gen_concatenate(processed_files)

# 方案二的高级用法示例
def advanced_process_files_v2(test_dir):
    """展示方案二的灵活性"""
    lognames = gen_find_files('access-log*', test_dir)
    files = gen_opener(lognames)
    
    def complex_file_processor(file):
        # 步骤1：找到Python相关的行
        python_lines = gen_grep('(?i)python', file)
        # 步骤2：只保留2023年的记录
        year_filtered = gen_grep('2023', python_lines)
        # 步骤3：添加更多处理...
        return year_filtered
    
    processed_files = map(complex_file_processor, files)
    return gen_concatenate(processed_files)

if __name__ == '__main__':
    # 创建测试文件
    import tempfile
    import os
    
    # 创建临时目录
    test_dir = tempfile.mkdtemp()
    
    # 创建测试日志文件
    log_contents = [
        "2023-01-01 Python request received\n",
        "2023-01-01 Java request received\n", 
        "2023-01-02 python script executed\n",
        "2023-01-02 PHP request received\n"
    ]
    
    # 写入测试文件
    with open(os.path.join(test_dir, "access-log1"), "w") as f:
        f.writelines(log_contents[:2])
    with open(os.path.join(test_dir, "access-log2"), "w") as f:
        f.writelines(log_contents[2:])
        
    # 测试方案一
    print("方案一结果:")
    for line in process_files_v1(test_dir):
        print(line.strip())
        
    print("\n方案二结果:")
    for line in process_files_v2(test_dir):
        print(line.strip())
        
    # 清理测试文件
    import shutil
    shutil.rmtree(test_dir)

