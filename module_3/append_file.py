f1=open("test3.txt","a")

n=int(input("enter number of students:"))
for i in range(n):
    id=input("enter id")
    name=input("enter name")

    
    f1.write(f"id:{id}\nname:{name}\n")