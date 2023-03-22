'''sum=0
i=1
while i <=100:
    sum+=i 
    i+=1
print(f"1-100累加的和是：{sum}")'''

'''i=1
while i<=5:
     print(i)
     i+=1'''
   
'''requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("抱歉，绿椒用完了")
    else:
        print(f"Adding {requested_topping}")
print("\nFinshed making your pizza") '''   

'''name="Ada Lovelace"
print(name.upper())
print(name.lower())'''

'''first_name = "ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}!")'''

#演示while循环的基础应用
'''i=0
while i < 100:
    print("小美，我喜欢你")
    i+=1'''

'''sum=0
i=1
while i <=100:
    sum+=i 
    i+=1
print(f"1-100累加的和是：{sum}")'''

'''i=0
lst = []
while len(lst) < 6:
    lst.append(i)
    i+=1
    print(lst)'''

'''s=0
for i in [1, 2, 3]:
    s+=i
    print(s)


l = [1, 2, 3]  
l = [x * x for x in l]
print (l)'''

'''for idx in range(5):
    print(idx)'''
#定义一个变量，用来统计有几个偶数

#通过for循环来提取100以内的偶数
'''count=0
a=1
for i in range(1,100):
    if i % 2 ==0:
        count +=1
print(f"1到100(不含100本身)范围内，有{count}个偶数") '''

#演示嵌套表白100天，每天都送10朵花
#range
'''i=1
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天，加油")

    #写内层的循环
    for j in range(1,11):
        print(f"给小美送的第{j}朵玫瑰花")

    print("小美我喜欢你")

print(f"第{i}天，表白成功")'''

'''for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break 
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')'''

'''for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue 
    print("Found odd number", num)'''

'''def greet_user(username):

    print(f"\t Добрый вечер, {username.title()}!\n\t Удачного дня!")

greet_user('Мария Боковая')'''

'''import numpy as np
Z=np.zeros(9)
print(Z)
import numpy as np
Z = np.ones(9)
print(Z)
'''
'''import numpy as np
Z = np.array([1,0,0,0,0,0,0,1,0])
print(Z)

import numpy as np
Z = 2*np.ones(9)
print(Z)
import numpy as np  
Z = np.arange(9).reshape(9,1)
print(Z)

import numpy as np
Z=np.random.randint(0,9,(3,3))
print(Z)'''


'''import numpy as np
Z=np.zeros(10)
Z[4]=1
print(Z)'''

'''import numpy as np
Z = np.arange(9).reshape(3,3)
print(Z)'''

'''import numpy as np
Z = np.arange(9).reshape(3,3)
print(Z[0,0])'''

'''import numpy as np
Z = np.diag([1, 2, 3])
print(Z)'''
'''import numpy as np
a = np.arange(16).reshape((4, 4))
print(a )'''


import numpy as np
A = np.random.randint(0, 30, size=(4, 6))
print(A)
B = A[:, ::2]
print(B)
C = A[:, 1::2]
print(C)
