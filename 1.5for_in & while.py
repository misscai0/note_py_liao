# for...in..循环：会依次迭代列表中的元素
name = ['xiaoming','xiaohong','yaoyao']
for a in name:
    print(a)

sum = 0
for a in range(1,3):
    sum = sum + a 
print(sum)

sum = 0
for a in range(101):
    sum = sum + a 
print(sum)

# while 持续循环直至条件不满足循环要求
sum = 0
n = 10
while n > 0 :
    sum = sum + n  
    n = n - 1
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('hello,',a)

# break 中断循环
n = 1
while n <= 100:
    n = n + 1 
    if n >= 10:
        break
print(n)

# continue 跳过本次循环，执行次轮循环
# ! 曾陷入的误区：continue要在执行句的后面。
n = 1
while n <= 100:
    n = n + 1 
    if n >= 10:
        continue
print(n)

# 除7以外的10以内奇数和

#正确范例：
n = 0
sum = 0
while n < 9 :
    n = n + 1
    if n == 7 or n % 2 == 0:
        continue
    sum = n + sum
print(sum)

#错误范例：
n = 0
sum = 0
while n < 9 :
    n = n + 1
    sum = n + sum
    if n == 7 or n % 2 == 0:
        continue
print(sum)
#将 sum = n + sum 这一执行句放在需要中断的句子的前面，他会先加再中断。在continue前后加print观察变化可知。
n = 0
while n < 3 :
    n = n + 1
    b = n
    print('第',b,'次','n1 =',n)
    if n == 2:
        continue
    print('第',b,'次','n2 =',n)
