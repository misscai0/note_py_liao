# list 可变有序量表
my_love = ['xiaoxiong' ,'pupu','lingnabeier']
print(my_love)

# len()可以计算列表的长度 ps之前学习了能够计算字节数/字符数
len(my_love)

#索引 索引以0为第一个，-1为倒数第一个
my_love[0]
my_love[-3]
my_love[len(my_love)-1]

#使用append为量表添加内容.一次只可以加一个
my_love.append('goodbear')

#指定添加的位置 insert(位置, )
my_love.insert(0,'haoxiong')
print(my_love)

#删除指定位置的元素 pop(位置) 不写位置默认删除第一个
my_love.pop()
print(my_love)
my_love.pop(len(my_love)-1)
print(my_love)

#一个复杂的例子。list内可含数字，列表，...
a = [6,'0',['i',2],9.93e2, True]
print(a)


# tuple 不可变量表
emo = ('happy','sad','upset')
print(emo)

#定义只有1个元素的tuple
tuple9 = (1,)
len(tuple9)

#"可变的"tuple 小花招..
emotion = ('happy','sad',['x','y'])
print(emotion)
emotion[2][1]='scrad'
emotion[2][0]='astonished'
print(emotion)




#请用索引取出下面list的指定元素：
# -*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[len(L)-1][2])