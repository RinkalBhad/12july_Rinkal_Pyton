'''f=open("t.txt","w")
f.write("my name is bhad rinkla i am a python developerr \ntwinkal twinkal little star how are you wonder what you are")

f=open("t.txt","r")
t=f.read()
if "twinkal" in t:
    print("yes")
else:
    print("not")'''

'''def game():
    return 646

s=game()
f=open("t.txt","r")
h=int(f.read())

if h<s:
    f=open("t.txt","w")
    f.write(str(s))'''

'''f=open("t.txt","w")
for i in range(2,21):
    for j in range(10):
        f.write(f"{i}x{j}={i*j}\n\n")
        if j!=10:
            f.write("\n")

'''

'''f=open("t.txt","r")
c=f.read()
c=c.replace("donkey","@@@@@")

f=open("t.txt","w")
f.write(c)'''


'''f=open("t.txt","r")
t=f.read()
f1=open("copy.txt","w")
f1.write(f"{t}")'''


'''
f=open("t.txt","r")
t=f.read()


f=open("copy.txt","r")
t1=f.read()

if t==t1:
    print("identical")
else:
    print("not identical")'''

'''def data(id,nm):
    f=open("t.txt","w")
    f.write(f"{id}{nm}")
    
id=input("enter id")
nm=input("enter name")  


data(id,nm)
'''
'''n=int(input("enter n"))
def hi():
    id=input("enter id")
    nm=input("enter name")
    f=open("t.txt","a")
    f.write(f"id:{id}\nname:{nm}\n.....")

for i in range(n):
    hi()
'''
'''
try:
    i=int(input("enter number:"))
    if i%2==0:
        print("even")
    else:
        print("odd")

except Exception as e:
    print(e)'''


'''import time
n=int(input("enter time:"))
for i in range(0,n):
  second=i%60
  min=int(i/60)%60
  hous=int(i/3600)
  print(f"{hous:02}:{min:02}:{second:02}")
  
  print(i)
  
  time.sleep(1)
print("time's up")'''

'''import random
f=open("one.txt","r")
x=f.readlines()[::-1]
y=random.choice(x)
print(y)'''
'''
txt = "Hello My Name Is PETER"
x = txt.swapcase()'''
'''print(x)

print(txt[-4:])
print(txt[:4])


def myfunc(a):
    a = a + 2
    a = a * 2
    return a
 
print (myfunc(2))
print(3*1**3)'''
'''print ('{0:.2}'.format(1.0 / 3))
print ('cd'.partition('cd'))
print ('abcefd'.replace('c''d', '12'))'''

''''

from tkinter import*
from tkinter import messagebox as mb
f=open("ti.txt",'a')
def accept():
    x=e.get()
    y=e1.get() 
    
    f.write(f"{x}\n")
    f.write(f"{y}\n")
    mb.showinfo("hi","inserted")   

top=Tk()
top.geometry("600x500")

l=Label(top,text="Enter Name")
e=Entry(top)
l.pack()
e.pack()

l1=Label(top,text="Enter Email")
e1=Entry(top)
l1.pack()
e1.pack()

b=Button(top,text="submit",command=accept)
b.pack()


top.mainloop()

'''

'''f=open("ti.txt","a")

class student:
    id=0
    name=''

    def accept(self):
        self.id=input("enter  id:")
        self.name=input("enter name:")
        f.write(self.id)
        f.write(self.name)

class otherstudent(student):
    
    def accept(self):
        return super().accept() 

s=student()
s.accept()

o=otherstudent()
o.accept()'''

'''import random
a="abcdefghijklmnopqrstuvwxyz123456780!@#$%^&*()"
legth=int(input("enter length"))
passwrd=""
for i in  range(legth):
  passwrd+=random.choice(a)
print(passwrd)'''
''''from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print(Counter(one)==Counter(two))

e=enumerate(one,1)
print(dict(e))'''

                                                                                     
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


l=[]
# x=[]
for i in list:
    if i not in l:
        l.append(i)
    else:
        x.append(i)
print(l)
print(x)
