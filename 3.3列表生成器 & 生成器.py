[x * x for x in range(1, 11)]

[x * x for x in range(1, 11) if x % 2 == 0]

[m + n for m in 'ABC' for n in 'XYZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
     print(k, '=', v)
[k + '=' + v for k, v in d.items()]

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

# if写在for前面，是条件，需要else补充
# if卸载for后面，是筛选，不能加else补充
[x for x in range(1, 11) if x % 2 == 0]
[x if x % 2 == 0 else -x for x in range(1, 11)]


### 练习：使列表中的字符串变为小写。使用lower()
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#但是我认为这个题并不够好，应该小写str同时保留int或float
L3 = [s.lower() if isinstance(s, str)== True else s for s in L1]
print(L3)


#生成器(generator)：在Python中，一边循环一边计算的机制
#创建generator的多种方法。
#  1：把一个列表生成式的[]改成()
g = (x * x for x in range(10))
for n in g:
    print(n)

# 2：yield关键字
# 如果一个函数定义中包含yield关键字，则这个函数就是一个generator函数
##普通函数
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
##generator函数
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# generator函数和普通函数的执行流程不同。
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 用for循环调用generator时，拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#exam
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# -*- coding: utf-8 -*-
def triangles(n): 
    triangles=[1]
    for i in range(1,len[n]-1):
        triangles[i]=triangles[i]+triangles[i-1]
        triangles.append[triangles[i]]
    triangles.append(1)
# 生成前10行杨辉三角
current_row = [1]
for i in range(10):
    print(current_row)
    current_row = triangles(current_row)
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)


if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')