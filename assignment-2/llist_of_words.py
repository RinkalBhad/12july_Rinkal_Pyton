'''l=[]

n=int(input("enter number "))
for i in range(n):
    k=input(f"enter word {i} ")
    l.append(k)

print(l)
res = max(l, key = len)
print(res)'''


l=[]
def length():
    
    n=int(input("enter number "))
    for i in range(n):
       k=input(f"enter word {i} ")
       l.append(k)

length()

print(l)
res = max(l, key = len)
print(res)




