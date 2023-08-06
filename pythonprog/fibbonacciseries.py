'''0,1,1,2,3,5,8,13,21''' 


n=int(input("enter n"))
a=0
b=1
f=0
print(a)
print(b)
for i in range(1,n+1):
    f=a+b
    a=b
    b=f
    print(f)