# 尝试理解输出值为函数
def get_f(n):
    def f(x):
        return x*n
    return f

f2 = get_f(2)
f2(3)
f3 = get_f(3)
f3(3)

# __name__属性，可以拿到函数的名字：
# （注意：是前后各两个下划线）
f2.__name__
f3.__name__

#一个极端例子
def dec(n):
    return 2
@dec  
#把 @dec 放到double()函数的定义处，相当于执行了语句： 
# double = dec(double)
def double(x):
    return 2*x
print(double)
#在这个过程中，由于dec() return了2，因此在@dec的赋值当中，double就被赋值了2
print(double(2))
#error，因为double已经不再是函数了。

# 装饰器 Decorator
# 大多数情况下，是一个输入值和返回值都是函数的函数
import time   #import计时函数
     
def timeit(f):

    def wrapper(x):
        start = time.time()
        ret = f(x)
        print (time.time()-start)
        return ret
    
    return wrapper

@timeit   # my_function = timeit(my_function)
def my_function(s):
    return s**s
print (my_function(5))


##可以传入多个参数
def timeit(f):

    def wrapper(*q,**p):
        start = time.time()
        ret = f(*q,**p)
        print (time.time()-start)
        return ret
    
    return wrapper

@timeit   # add = timeit(add)
def mul(x,y):
    return x*y
print (mul(5,3))

@timeit   # plus = timeit(plus)
def plus(x,y,z):
    return x*y+z
print (plus(5,3,8))

# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log  # now=log(now)
def now():
    print('2015-3-25')
now()


##带参数的 decorator
def log(text):

    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    
    return decorator
#这个3层嵌套的decorator用法如下：
@log('execute') #  now = log('execute')(now)
def now():
    print('2015-3-25')
now()
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。


#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
now.__name__
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#或者针对带参数的decorator：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#functools是导入functools模块。在定义wrapper()的前面加上@functools.wraps(func)即可
import functools

# exam
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        ret = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time()-start))
        return ret
    return wrapper


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def metric(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print ('begin call')
        ret = f(*args, **kw)
        print ('end call')
        return ret
        
    return wrapper

@metric
def f1(x):
    x**x
print(f1(8))


#再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
#又支持：
@log('execute')
def f():
    pass


#开始写的是时候用 log(*n) 尝试，但是失败了。原因是可变参数返回tuple，但 log('execute') 中是str, 判断就要用tuple
import functools
def log(text=None):
    if isinstance(text,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('okay')
                return fn(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('okay')
            return text(*args, **kw)
        return wrapper        


@log
def f():
    pass
#又支持：
@log('execute')
def f():
    pass

#开始写的是时候用 log(*n) 尝试，但是失败了。原因是可变参数返回tuple，但 log('execute') 中是str, 判断就要用tuple
import functools
def log(*n):
    if isinstance(n,tuple):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('okay')
                return fn(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(n)
        def wrapper(*args, **kw):
            print('okay')
            return n(*args, **kw)
        return wrapper        


@log
def f():
    pass
#又支持：
@log('execute')
def f():
    pass


#其实可以不使用isintance，更简单
import functools
def log(*n):
    if n==None:
        @functools.wraps(n)
        def wrapper(*args, **kw):
            print('okay')
            return n(*args, **kw)
        return wrapper  
    else:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('okay')
                return fn(*args, **kw)
            return wrapper
        return decorator      


@log
def f():
    pass
#又支持：
@log('execute')
def f():
    pass
