def getdata(id,name):
    print("ID:",id)
    print("Name",name)
    
    #static
#getdata(1,"rinkal")

#dynamic
id=input("enter id")
nm=input("enter name")
getdata(id,nm)

n=int(input("enter n"))
for i in range(n):
    getdata()