data=[]
n=int(input("enter number"))
for i in range(n):
    x=input("enter an element")
    data.append(x)

a=tuple(data)
print(type(a))