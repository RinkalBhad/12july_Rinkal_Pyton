from  func import*

print("WELCOME TO FRUIT MARKET")
print("\t1. Manager")
print("\t2. Customer")

choice()
k=input("enter your choice:")
if k=="1":
   fruit()
   op()
   fruit()

elif k=="2":
   view()
   choice()

elif k=="3":
   find()
   choice()