import datetime
x=datetime.datetime.now()
f=open("test4.txt","a")

n=int(input("enter number:"))
for i in range(n):
    id=input("enter id:")
    name=input("Enter name:")
    city=input("enter city:")
    
    f.write(f"id:{id}\nname:{name}\ncity:{city}\n{x}\n")