# dict {key:value}
# ps: key为不可变变量，str bytes tuple皆可，但list不可
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

# dict可以通过key放入
d['yaoyao'] = 88
d

# 通过pop(key)删除
d.pop('Bob')
d

#判断key是否存在: in 或 get()
'Michael' in d
'lin' in d

d.get('yaoyao')
# key不存在，且未指定返回value时，无输出结果；key不存在但指定返回value时，输出指定value
d.get('lin')
d.get('lin',0)


# set 无序、无重复元素的集合。重复元素会被忽略
s = set([1,2,3])
s
s = set([1,2,3,3])
s

#通过add(key)放入元素
s.add(4)
s
#通过remove(key)删除元素
s.remove(2)
s

# set可以被当作集合来运算
s1 = set([1,2,3,4])
s2 = set([4,5,6])
s1 & s2
s1 | s2


#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
#我的理解：key可以为tuple，但是tuple内不能含有可变变量（list）。value随意
d01 = {(1, 2, 3):(1, [2, 3])}
d01
d02 = {(1, [2, 3]):(1, 2, 3)}
d02

s01 = set((1, 2, 3))
s01
s02 = set ((1, [2, 3]))
s02