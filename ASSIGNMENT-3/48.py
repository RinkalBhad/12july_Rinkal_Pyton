#  Write a Python function to calculate the factorial of a number (a nonnegative integer) 



def fact(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    print("factorial number is:",f)

n=int(input("enter number:"))
fact(n)