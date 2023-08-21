#Write a Python program to get the Fibonacci series of given range

num=int(input("enter number "))
a=0
b=1

for i in range(num):
    c=a+b
    a=b
    b=c

    print(c,end=" ")
