'''n=int(input("enter bnumber"))
list=[]

for i in range(n):
    id=int(input("enter id"))
    nm=input("enter name")
    sj=input("entr subject")
    city=input("enter city")
    l=[id,nm,sj,city]
    list.append(l)

for li in list:
    print(li)
'''



n=int(input("enter n"))
for i in range(0,n,2):
    print(i,i+1)