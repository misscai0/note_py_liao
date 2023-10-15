# sorted()函数就可以对list进行排序
sorted([36, 5, -12, 9, -21])

# sorted()函数是一个高阶函数，可以接收一个key函数来实现自定义的排序
# 如, 按绝对值大小排序
sorted([36, 5, -12, 9, -21], key=abs)

#对字符串排序:
# 字符串排序是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
sorted(['bob', 'about', 'Zoo', 'Credit'])
#利用key函数把字符串映射为忽略大小写排序
# 实际上就是先把字符串都变成大写（或者都变成小写），再比较。
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

#反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# exam 
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# -*- coding: utf-8 -*-
def by_name(t):
    print(t[0])
    return t[0]
    
by_name(L)
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    print(t[1])
    return t[0]
L2 = sorted(L, key=by_score)
print(L2)

