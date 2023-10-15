L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# l[n,m] : 索引第n个（含）元素开始到第m个（含）元素
L[0:3]
L[:3]
L[-2:]
L[:]

#在使用［：-1］切片时，会取是第一位到倒数第二位
#也就是说，［：-n］是开口的
#但使用[0:]切片，仍是第0位到最后一位
#也就是说，[n:]是闭口的
#需要注意的是，[n,m]双方仍然是闭口的

# list tuple str..都可以切片
t = (2,3,4,5,6)
t[-3:]

s = 'poiuytrewqq'
s[3:5]
len(s)
s.pop(0)


# exam
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

# -*- coding: utf-8 -*-
def trim(s):
    n = 0
    if n == len(s):
        return s
    while n <= len(s):
        n = n + 1
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-2]
    if s == ' ':
        s = ''
    return s


# 别人的做法。值得借鉴：使用了递归函数
def trim(str):
    if str == '':
        return ''
    elif str[0]==' ':
        return trim(str[1:])
    elif str[-1]==' ':
        return trim(str[:-1])
    return str

def trim(str):
    if str[-1]==' ':
        return trim(str[:-1])
    return str
trim('heloo      ')
def trim(str):
    if str[-1]==' ':
        return trim(str[:-2])
    return str
trim('heloo   ') 
def trim(str):
    if str[-1]==' ':
        return trim(str[:-3])
    return str
trim('heloo  ')

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


