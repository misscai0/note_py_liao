#print 输出
#input 输入

print('hello, llin')

i = 10
print(i*9)
print('20+30','=',20+30)

#在交互环境用input
id = input(20191016366)
print('hello',id)
name = input('please input your name')
print ('hello,',name)


#请利用print()输出1024 * 768 = xxx：
print('1024 * 768 =',1024 * 768)

#整数可以用_来隔开，最终输出的数字仍然是一样的
print(9200)
print(9_2_0_0)

#浮点数，过大或过小时使用en,来替代10的n次方
print(2.4e10)
print(24e9)
print(2.4e-4)
print(2.4e-9)

#字符串，""和''标识
print("小熊")
print('小熊')
#可以用不同的""和''使它们其中的一个出现在输出中，但是使用相同的会报错
print("'xiao'xiong")
print('"xiao"xiong')

# \是转义字符，利用r''可以使\不被转义
print(' I\'m "okay"')
    # I'm "okay"
print(r'ooo\o')
    #ooo\o

#布尔值 Ture False

# = 赋值




#请打印出以下变量的值：
#n = 123
n=123
print(n)

#f = 456.789
f=456.789
print(f)

#s1 = 'Hello, world'
print("'Hello, world'")

#s2 = 'Hello, \'Adam\''
s2 = r"'Hello, \'Adam\''"
print (s2)

#s3 = r'Hello, "Bart"'
s3=  "r'Hello, \"Bart\"'"
print(s3)

#s4 = r'''Hello,
#Lisa!'''

s4 = "r'''Hello,\nLisa!'''"
print(s4)
