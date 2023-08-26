'''nm="rinkla"
for i in range(10):
    print("rinkal")'''

#a=int(input("how many element are you add"))

'''for i in range(a):
    nm=input("enter your name")
print(nm[0:-1])'''

'''x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)
'''
#_________________________________________________________________________________
'''x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)'''
'''
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break'''
#_________________________________________________________________________________
'''for num in range(-2,-5,-1):
    print(num, end=", ")'''

'''numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:  
  for y in items:
    print(x, y)'''

'''x = 0
while (x < 100):
  x+=2
print(x)
'''
 #___________________________________________________________________________________
'''for num in range(2,-5,-1):
    print(num, end=", ")

a, b = 12, 5.6
if a + b:
    print(True)
else:
  print(False)
'''
'''x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)'''
#__________________________________________________________________________________
'''var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

'''
#_________________________________________________________________________

'''# Python program to print pairs of numbers from 0 to n
n = int(input("Enter a number: ")) # get the maximum limit from the user
for i in range(0, n,2): # loop from 0 to n with a step of 2
    print(i,i+1) # print the current number and the next number

# Python program to print pairs of numbers from 0 to n using while loop
n = int(input("Enter a number: ")) # get the maximum limit from the user
i = 0 # initialize a counter variable
while i <= n: # loop until the counter reaches n
    print(i, i+1) # print the current number and the next number
    i = i + 2 # increment the counter by 2
'''
#_____________________________________________________________________________________________

'''l=[1,2,3]
l.reverse()
print(l)

l1=[12, 35, 9, 56, 24]
f=l1.pop(0)
last = l1.pop(-1)
print(l1)
l1.insert(0,last)
l1.append(12)
print(l1)
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)
print(len(l1))
c=0
for i in l1:
    c=c+1
print(c)'''
#__________________________________________________________________________________

'''str="my name is bhad rinkla"
l=[]

s = str.split()[::-1]
for i in s:
     l.append(i)

print(" ".join(l))

'''
'''print(ord('A'))

str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count("is", 4))

str = "My salary is 7000";
print(str.isalnum())

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

l = [None] * 10
print(len(l))

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)'''

'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
k=(list1[0]+list2[0])+ (list1[1]+list2[1])+ (list1[2]+list2[2])+(list1[3]+list2[3])
print(k)

print(k.isalnum())
'''

'''numbers = [1, 2, 3, 4, 5, 6, 7]
res=[]
for i in numbers:
    
    res.append(i**2)
print(res)
'''

'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res=[]
for i in list1:
    for j in list2:
        c=i+j
        res.append(c)
print(res)'''


'''list1 = [5, 10, 15, 20, 25, 50, 20]

k=list1.index(20)
list1[k]=200
print(list1)'''

'''l=[10,20,30]
l.append(40)
l.remove(30)
l.reverse()
l.extend("rinkal")
l.pop()
l.remove(20)
print(l)

l=[10,20,30]
k=["rinkla","bhad"]
l.extend(k)
print(l)
print("-------------------'''

'''marks=[80,90,40]
name=["abc","xyz","jkl"]
k=zip(marks,name)
for i in k:
    print(i)
#print(dict(k))
#print(set(k))
#print(list(k))
'''
'''
list1 = [12, -7, 5, 64, -14]
k=[]
for i in list1:
    if i<0:
        k.append(i)
print(k)'''

'''n=0
p=0
for i in range(-4,12):
    if i<=0:
       
        n=n+1
    if i>=0:
       
        p=p+1
print(n)
print("toal number is",p)'''


'''l=[30,50,60,70,90]
for i in l:
   if i%2==0:
     l.remove(i)
print(l)
'''

'''list1 = [11, 5, 17, 18, 23, 50]
del list1[1:5]
print(list1)
'''
'''tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
tuples = list(filter(lambda x: len(x) > 0, tuples))
print(tuples)'''

'''list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
s=set(list)
print(s)'''


'''lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
	if i not in x:
		x.append(i)
for i in x:
	if lis.count(i) > 1:
		y.append(i)
print(y)
'''

'''a="my name is bhad rinkal"

k=len(a)//2

res = a[:k] + a[k:].upper()
 
print(res)'''

'''n="This is a python language"
i=n.split(" ")
for s in i:
  if len(s)%2==0:
    print(s)
'''
'''a="welcome2ourcountry34"
b="stringwithoutnum"
print(a.isalnum())
print(b.isdigit())'''
'''s=1
t=(2,5,7, 8)
for i in t:
 
    print(i)
    i=i*s'''

'''l=["rinkla","bhad","how","are","you"]
x=l.pop()
y=l.insert(0,x)
k=l.pop(1)
r=l.append(k)
print(l)'''

'''str=("my name is rinkal")
x=str.split()
print(str[::-1])
y=(x[::-1])
print(" ".join(y))
'''

'''c=0
l=0
str="MY name is rinkla"
for i in str:
    if  i.isupper():
        c=c+1
       
    elif i.islower():
        l=l+1
print("upper is",c)
print("lower is",l)'''

'''str="geeksforgeeks "
s=[]
for i in str:
    if i not in s:
       s.append(i)
print("".join(s))

s1="geeks for geeks"
s2="geeks"'''

'''if s2 in s1:
   print("yes")
else:
   print("no")'''

'''test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
 
print("The original string is : " + str(test_str))
 

res = {key: test_str.count(key) for key in test_str.split()}

print("The words frequency : " + str(res))      
'''

'''str = "hello geeks for geeks is computer science portal"
length=2

if len(str)<length:
    print(" all words that are of length more than k.")
else:
    print("not grater")'''

str="rinkla"
print(str.upper())

str=input("enter string")
print(str.upper())

