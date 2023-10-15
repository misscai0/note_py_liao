#调用函数
#函数名其实就是指向一个函数对象的引用。把函数名赋给一个变量，可以通过此变量调用函数
a = abs
a(-1)

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
n11 = hex(n1)
type(n11)
n12 = hex(n2)
type(n12)


# 定义函数 def
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

#检查参数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
a = my_abs('9')

# return多个值时，返回的其实是tuple

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
import math
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax2+bx+c=0 的两个解。
def quadratic(a, b, c):
    z =  b**2-4*a*c
    if z < 0:
        raise TypeError('无解')
    o = isinstance(a,(int, float)) and isinstance(b,(int, float)) and isinstance(c,(int, float))
    if o == False:
        raise TypeError('please input int or float')
    x1 = (-b + math.sqrt(z)) / (2*a)
    x2 = (-b - math.sqrt(z)) / (2*a)
    return x1,x2
import math
q,p = quadratic(2, 3, 1)
print(q,p)
v,w = quadratic(9.7,100,3.2)
print(v,w)
d,e = quadratic(9,0,1)
h,f = quadratic('3',3,2)

# 默认参数 
# n的默认参数为2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2,4))
print(power(2))

#！！！危险！！！默认参数为可变对象
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
# 函数“记住了”上次添加了'END'后的list
# 利用不变对象修改
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
add_end()
add_end()

# 可变参数:传入的参数个数可变  *numbers
#参数前面加了一个*号 : 函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
# *nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
calc(*nums)

def log(*n):
    for x in n:
        return n
print (log())
print (log(3))


# 关键字参数  **kw
#可变参数:传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
#关键字参数:传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('bob',18)

#命名关键字参数  *
# 命名关键字参数需要一个特殊分隔符 *，*后面的参数被视为命名关键字参数。用于限制关键字参数的名字
# 此处city和job就是关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
#此时，加入除规定外的参数会报错
person('Jack', 24, edu='middle school')
#你会惊奇的发现：命名关键字参数不同于关键字参数，如果输入时缺少参数，将会报错。
person('Jack', 24, city='Beijing')

#可变参数后面的命名关键字参数不需要特殊分隔符*
def person(name, age, *, city, job):
    print(name, age, city, job)
person('bob',56)


# 组合
#必选参数、默认参数、可变参数、关键字参数和命名关键字参数
#顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b=0, *args, o, **kw ):
    print('a =', a, 'b =', b, 'args =', args, o ,'kw =', kw)
f1( 1, 2, 3, o=4, z=5)
f1( 1, 2, 3, o=4, z=5)


#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def mul(x, y):
    return x * y
mul(2,3)

# while循环
def mul(x, y=1, *z):
    if len(z) == 0:
        return x * y 
    else:
        n = len(z)
        m = 0
        product = x * y
        while m <= n-1:
                product = product * z[m]
                m = m+1
        return product
# for in循环
def mul(x, y=1, *z):
    if len(z) == 0:
        return x * y 
    else:
        n = len(z)
        product = x * y
        for a in z:
                product = product * a
        return product
print(mul (2,8,2,2))
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 递归函数：函数在内部调用自身本身
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
fact(5)
# 递归调用的次数过多，会导致栈溢出
fact(9999)

# 尾递归优化 可以解决递归调用栈溢出
# 尾递归：函数返回时，调用自身本身，且return语句不能包含表达式
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
fact(4)
# 但实际上py没有对此进行优化，so...
fact(4000000)

#汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)
move(2,'a','b','c')
move(3,'a','b','c')
move(4,'a','b','c')


# f和f()
def foo() :
    return 2

# 函数引用
f
# 函数调用
f(1)

f = foo
ff = foo()


