#Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
#我们以内建的sys模块为例，编写一个hello的模块：



#!/usr/bin/env python3                      #让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-                     #表示.py文件本身使用标准UTF-8编码
' a test module '                           #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Michael Liao'                 #使用__author__变量把作者写进去
import sys                                  #导入sys模块:使用sys模块的第一步。导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
def test():
    args = sys.argv
    #sys模块中的argv变量，用list存储了命令行的所有参数。
    # argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
    #运行python3 hello.py获得的sys.argv就是['hello.py']；
    #运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
    # 当我们在命令行运行hello模块文件时，
    # Python解释器把一个特殊变量__name__置为__main__，
    # 而如果在其他地方导入该hello模块时，if判断将失败，
    # 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

$ python3 hello.py

