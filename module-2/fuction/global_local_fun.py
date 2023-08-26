'''a=10
b=20   #global

def sum():
    global a,b
    a=23
    b=2
    print("sum:",a*b)

print("mul",a*b)

sum()'''
from topspkg.genral import newlib
newlib.hi()