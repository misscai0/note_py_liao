#单个字符：ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('o')
chr(111)

# str字符串 bytes字节
# encode()使str变为bytes
# decode()使bytes变为str
# 内容.函数(转化的形态)
'abc'.encode('ascii')
'我的小熊真可爱'.encode('utf-8')

#len()函数就计算字节数或字符数

#!/usr/bin/env python3
    #告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
    #告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

# 实现格式化: %  format()  f-string
#占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

'hello, %s , you have $ %f' %('Alice',22.98)

# %.nf 保留n位小数点
print('%.2f' % 3.1415926)

## %%以表示%
'growth rate: %d %%' % 7




#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
g1=72
g2=85
r=(g2-g1)*100/g1

'%s\'s grade improved by %.2f%%' %('xiaoming',r)
