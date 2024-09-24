"""
寻找出现频率最高的元素
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

# 可以给 Counter 对象提供任何可哈希的对象序列作为输入。在底层实现中，Counter 是 一个字典，在元素和它们出现的次数间做了映射

# 也可以手动修改Counter中的内容

morewords = ['why', 'are', 'you', 'not', 'looking', 'in','my', 'eyes']

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])  # 9

# 使用update

word_counts.update(morewords)
print(word_counts['eyes'])  # 10


# Counter之间可以使用算术运算，如下

a = Counter(words)
b = Counter(morewords)

# 合并
c = a + b
print(c)  # Counter({'eyes': 9, 'the': 5, 'look': 4, 'into': 3,'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking':
# 差集
d = a - b
print(d) # Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1})
