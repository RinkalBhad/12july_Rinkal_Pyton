fnm=input("enter first name")
lnm=input("enter last name")




if fnm.isupper() and lnm.isupper():
    print("first name is",fnm)
    print("last name is",lnm)
    email=input("enter email id")
    mno=input("enter mno no")   
    if email.islower():
        print("email id is",email)
    else:
        print("enter valid email id")
    if len(mno)==10:
        
            print("mobail number",mno)
            
    else:
            print("eneter valid mobail number")
            
    pswd=input("enter passwod")
    rp=input("enter retype password")  
    if pswd==rp:
        print("password is",pswd)
        print("..................")
        print("first name is",fnm)
        print("last name is",lnm)
        print("email id is",email)
        print("mobail number",mno)
        print("password is",pswd)
    else:
        print("password and retype password are not match")
   
else:
    print("enter valid inforamation")

   