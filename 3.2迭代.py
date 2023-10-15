# 迭代（Iteration）:利用for循环来遍历可迭代对象（list tuple dict str），称为“迭代”
d = {'a':1,'b':2}
for a in d :
    print(a)
for value in d.values() :
    print(value)

# 判断一个对象是否是可迭代对象: collections.abc模块的Iterable类型
from collections.abc import Iterable #引入模块
isinstance('abc', Iterable)


#如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


#练习
#要使用最终想得到的变量（此处为min max）去判断循环。
#如果反过来，会输出倒数第一个比n大，以及倒数第一个比m小的数字
def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for n in L:
            if max > n:
                max = max
            else :
                max = n
        for m in L:
            if min < m:
                min = min
            else:
                min = m
        return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')