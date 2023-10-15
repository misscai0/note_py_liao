# 函数作为返回值
# 高阶函数以把函数作为结果值返回

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1,3,4)
print (f1)
f1()


#闭包

# Python语言特有的作用域搜索顺序导致：子对象可见父对象的所有变量，但，父对象不可见子对象的变量。
# 既然子对象可以读取父对象中的局部变量，那么只要把子对象作为返回值，就可以在父对象外部读取它的内部变量
# 实例：有一个外层函数的局部变量 n，有一个内层函数 f2，f2 里面可以访问到 n 变量，那这f2就是一个闭包。
def f1():
    n=999
    def f2():
        print(n)
    
    return f2

result = f1()
result()
#闭包的作用
# 1 闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁
# 2 将外层函数的变量持久地保存在内存中。

# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
f1()
f2()
f3()
#全部都是9！
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变。
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
f1()
f2()
f3()


# nonlocal
#使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

#但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
def inc():
    x = 0
    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

# 原因是x作为局部变量并没有初始化，直接计算x+1是不行的。
# 但我们其实是想引用inc()函数内部的x，所以需要在fn()函数内部加一个nonlocal x的声明。
# 加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2


# exam
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x=0
    def counter():
        nonlocal x
        x=x+1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
