def choice():
    s=input("select your Role:")

    if s=="1":
        print("\t Fruit Market Manager ")
        print("\t\t1.Add Fruit Stock")
        print("\t\t2.View Fruit Stock")
        print("\t\t3.Update Fruit Stock")
    
    else:
        exit()

def fruit():
    d={}
    keys=["fruit name ","qty (in kg) ","price "]
    for i in range(len(keys)):
        v=input(f"enter {keys[i]}: ")
        d[keys[i]]=v
        f1=open("new.txt","a")
    f1.write(f"fruit{d}\n")

def op():
    x=input("Do you want to perform more operations:press y for yes and n for no:").lower()
    if x=="y":
      fruit()
    else:
      choice()


def view():
    f=open("new.txt","r")
    print(f.read())

def find():
   print("1.fruit name ")
   print("2.qty")
   print("3.price")
   ch=input("what you want to update: ")
   if ch=="1":
      
      k=input("enter name that you want to update:")    #old fruit name  =k
      f=open("new.txt","r")    # file read krse =f
      for i in f:
         if k in i:      # in file old fruit che k nahi te check krse = i
            j=input("Add new fruit name ")
           
            f=open("new.txt","a")
            f.write(f"{i.find(k)}i{i.replace(k,j)}\n\n")
 
   elif ch=="2":
      print("update quantity")
      q1=input("enter which quantity update")   #fruit name enter=q1
      f=open("new.txt","r")

      for i in f:
         if q1 in i:
            q2=input("enter new quantity")   # new quantity
            f=open("new.txt","a")
            f.write(f"{i.find(q1)}i{i.replace(q1,q2)}\n\n")
            print(i.find(q1))

  
   elif ch=="3":
      print("update prrice:")
      q1=input("enter which price")   #fruit name enter=q1
      f=open("new.txt","r")

      for i in f:
         if q1 in i:
            q2=input("enter new price")   # new quantity
            f=open("new.txt","a")
            f.write(f"{i.find(q1)}i{i.replace(q1,q2)}\n\n")
            print(i.find(q1))
    
