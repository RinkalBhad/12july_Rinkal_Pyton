
from func import*
import random
id=random.randint(1,100)

print("Role 1: user")
print("Role 2: staff")

ch=input("select your Role:")
if ch=="1":
   print("user")
   nm=input("enter name")
   x=nm.upper()
      
   ct=input("enter city")
   sj=input("enter subject")
   
   
   data(id,x,ct,sj)

elif ch=="2":
   print("staff")
   for i in range(5):
     
     staff()