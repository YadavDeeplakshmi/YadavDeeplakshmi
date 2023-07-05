
'''
print("hello", end="\t")
print("program")
empid = 100
print(empid)
# add program 
num1 = 6
num2 = 4
r = num1 + num2
print(r)
# = -  * / (float) // (int) %
# += -= *= /= //= %=

num3 = 8
num3 += 3
print(num3)
 
 #> < >= <= != == true false
num4 = 5
num5 = 7
print(num4 > num5)

 #and or not
num6 = 5
num7 = 7
print(num6>10 and num7 < 10)
print(num6>10 or num7<10)
print(not(num6>num7))

if False:
    print("true")

n = 10
if n>=10:
    print("num is 10 ")
pin = 190
if pin == 100:
    print("login")
else: 
    print("not login")


user = input("enter username")
if user == "admin":
    password = input("enter password")
    if password == "admin123" :
        print("login")

    else : 
        print("enter right password")
else:
    print("enter right user")
    

user = input = ("enter user & email")
if user == "admin" :
    print("login")
elif user == "admin@gmail.com" :
    print("login")
else :
    print("not login")

print("1")
print("2")
print("3")

#while loop
# 1 2 3 4 5
#start i = 1 end i <= 5

i = 1
T = 4
while i <= 5:
    print(i*T)
    i+=1

i =1
sum8 = 0
while i <= 10:
    if i%2 == 0:
        sum8 = sum8 + i
    i+=1  
    print(sum8)

num = int(input("enter number"))

num = 27384
output = 246


i = 27384
T= 0
while i > 0:
    if i%2 == 0:
        T += 1
    i = i // 10
print(T)

from re import I
'''

n = 27384
d = 0
while n > 0:
    d = n % 10
    if( d%2 == 0 ):
        print(d) 
    n=n//10

'''
# i = 0 , i+=1 , i< 10
from distutils.dist import DistributionMetadata


for num in range(1, 10, 2):
    print( num)

#list[]
Data = [1,5,2,6]
print(Data)

add = 0
for data1 in Data:
    print(data1)
    add = add + data1
print(add)

print(sum(Data))
print(max(Data))
print(min(Data))
print(len(Data))

Data.append(7)
print(Data)
Data.insert(2,5)
print(Data)
Data.pop()
print(Data)

user = ["user1", "user2"]
password = ['123', '456']
while True:
    username = input("Enter Name: ")
    pas = user.index(username)
    if username in user:
        print("login")
        password1 = input("Enter Password : ")
        if password1 == password[pas]:
            print("login")
            break
    else:
        print("not")
'''

user = ["user1", "user2"]
passwordn = ['456', '123']
ide = {
    "user1" : '456',
    "user2" : '123'
}
while True:
    username = input("Enter username: ")
    password = input("Enter Password: ")
    if password in passwordn and username in user :
        if username == ide.keys(): 
            print("Login")
        break
    else:
        print("not")

