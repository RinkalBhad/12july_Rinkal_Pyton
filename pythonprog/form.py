fnm=input("enter your first name")
lnm=input("enter your last name")

if fnm.isupper() and lnm.isupper():

    email=input("enter email id")
    mno=int(input("enter mobail No."))
    if email.islower():
          if mno<=10:
               print("mobail no is",mno)
          else:
               print("enter valid number and email id")

    pswd=input("enter passoword")
    rpswd=input("enter retype password")
      
    print("first name is ",fnm)
    print("last name is",lnm)
    print("email is",email)
    print("mobail no is",mno)  
    if pswd==rpswd:
           print("your password is",pswd)
    
  
    else:
           print("password and retype password does not match")
    
    

    
  
else:
    print("invalid plz enter valid details")
    
    