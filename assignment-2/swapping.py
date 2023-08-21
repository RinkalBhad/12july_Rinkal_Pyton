#  Write python program that swap two number with temp variable and without temp variable.

a=int(input("enter a "))
b=int(input("enter b "))

print("before swap a:",a)
print("before swap b:",b)

temp=a
a=b
b=temp

print("After swapping a:",a)
print("After swapping: b",b)

#____________________________________________________________________________________

a=int(input("enter a "))
b=int(input("enter b "))

print("before a:",a)
print("before b:",b)

a,b=b,a

print("after swap::",a)
print("after swap::",b)