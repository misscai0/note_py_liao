# map
# map()函数接收两个参数:函数和Iterable（可迭代对象）。
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator（迭代器）返回。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)


# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# reduce接收两个参数，把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])

from functools import reduce
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
reduce(fn, map(char2num, '13579'))


# exam1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def a(n):
    return n[0].upper() + n[1:].lower()
print(list(map(a, ['adam', 'LISA', 'barT'])))

# “TypeError ‘str’ object does not support item assignment”错误
# 直接赋值改变字符串中某个字符的值时遇到。
# 原因：python中字符串是一个不可变类型
#   解决方法：
# （1）把字符串转列表
# （2）改变列表中对应的元素
# （3）把列表转换成新的字符串


# exam2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(x,y):
    return x * y
print(reduce(prod, [3, 5, 7, 9]))

def prod(L):
    def f(x,y):
        return x * y
    return reduce (f,L)
print( prod([3, 5, 7, 9]) )


# exam3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# 先利用map把字符串转换成两段整数
# 再利用reduce把小数点前的数字和后的数字加和
from functools import reduce
def str2float(s):
    s1,s2 = s.split('.')
    print(s1,s2)
    def f(x,y):
        return x*10 + y
    def c(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    t1 = map(c,s1)
    t2 = map(c,s2)
    f1 = reduce( f , t1 )
    f02 = reduce( f , t2 )
    f2 = f02 / (10**len(s2))
    return f1+f2
str2float('123.456')

# index()函数: 用于从序列s中找出某个值第一个出现时的索引位置
o = '882.3'
o.index('.')

# split()函数: 用于通过指定分隔符对字符串进行切片
p = '882.3'
p.split('.')

# n[start:end:step]
# n[起始:结束:步长]
n='2.134'
idx = n.index('.')
n[-1:idx:-1]
