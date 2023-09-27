f=open("fun.txt","a")
n=int(input("enter n"))
def data():
    
    
      id=int(input("enter id"))
      name=input("enter name")
      ct=input("enter city")
      f.write(f"id:{id}\nname:{name}\ncity:{ct}\n.......\n")

for i in range(n):
     data()
      

    