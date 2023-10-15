# if elif else 

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#    低于18.5：过轻
#    18.5-25：正常
#    25-28：过重
#    28-32：肥胖
#    高于32：严重肥胖
#用if-elif判断并打印结果：

height = 1.75
weight = 80.5


#交互..
#要使用float浮点数
h = input('please input your height')
w = input('please input your weight')
h0 = float(h)
print(h0)
w0 = float(w)
bmi = w0/(h0*h0)
print(bmi)

if bmi <= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else :
        print('严重肥胖')

#不交互
height = 1.75
weight = 80.5
bmi = weight/(height**2)
print(bmi)

if bmi <= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else :
        print('严重肥胖')

#小彩蛋
b = input('plese input a number')
x = float(b)
if x < 9 :
    print('hanhan is so cute')
elif x > 10 :
    print('linlin is so cute')
else:
    print ('we are both cute')
