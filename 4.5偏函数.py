# functools.partial是帮助我们创建一个偏函数的
import functools
int2 = functools.partial(int, base=2)

int2('1000000')

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
# 注意到上面的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
int2('1000000', base=10)

#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
int2('10010')

#相当于：
kw = { 'base': 2 }
int('10010', **kw)

#当传入：
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
#相当于：
args = (10, 5, 6, 7)
max(*args)


# # 定义一个取余函数，默认和2相除；
def mod(x,y=2):
    n = x / y
    return n
# 假设我们要计算和3取余，如果不使用partial()函数，那么我们每次调用mod()函数时，都要写y=3
mod(4,y=3)
mod(6,y=3)
# 使用partial()函数
mod3 = functools.partial(mod, 3)
mod3(4)

# a%b 得到a/b的余数


