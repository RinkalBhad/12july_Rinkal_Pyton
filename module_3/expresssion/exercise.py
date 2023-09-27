import re

'''nm=input("enter name:")
ptn="\A[A-Z]+[a-z]+[0-9]$"
x=re.findall(ptn,nm)

if x:
    print(x)
  
else:
    print("invalid..")'''


pswd=input("entere password:")
ptn="^[a-z]+[\.]+[0-9]$"
x1=re.findall(ptn,pswd)
if x1:
        print(pswd)  
        rpswd=input("enter repassword")
        ptn="^[a-z]+[\.]+[0-9]$"
        r=re.findall(ptn,rpswd)
        if r:
               print(r)
               if x1==r:
                      print("okk")
               else:
                        print("passsword and repassword are not match..")
        else:
             print("invlaid")                     
else:
        print("invalid password..")


