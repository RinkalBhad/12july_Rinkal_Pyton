# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))

if a==b or b==c or a==c:
    print("zero")
else:
    print("sum is",a+b+c)