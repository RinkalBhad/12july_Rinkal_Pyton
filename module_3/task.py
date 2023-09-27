import random
x=random.randrange(11111,999999,11111)

class ac:
    balnce=0
    name=''

    def opn(self):
        
        self.name=input("enter name:")
        self.balnce=int(input("accoutng opning balance"))
        if self.balnce>=2500:
          print("your account number is:",x)

          print("1.saving:")
          print("2.currunt:")
          self.type=input("enter type of account:")
          if self.type=="saving":
             print("saving")
          elif self.type=="currunt":
             print("currunt")
        else:
           print("if you want to open accoutt then enter opning balance")
     
        

    def deposite(self):
       self.a=int(input("enter deposit amount"))
       self.balnce+=self.a
       print(self.balnce)

    def withdr(self):
       self.w=int(input("enter amount of withdraw"))
       self.balnce-=self.w
       print(self.balnce)
         

       
    def statemnt(self):
      print(self.name)
      print(x)
      print(self.type)
      print(self.balnce)
   
      
     
    
c=ac()
while True:

   ch=input("enter choice:\n1)A.C open\n2)Deposite\n3)Withdraw\n4)statement\n5)exit::")

   if ch=="1":
       c.opn()

   elif ch=="2":
     c.deposite()

   elif ch=="3":
       c.withdr()

   elif ch=="4":
      c.statemnt()

   elif ch=="5":
      exit()


      
   
   
    