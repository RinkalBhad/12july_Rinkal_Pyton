import register as r

def choice1():
  while True:
    ch1=input("what operation are you perform:\n\t1.register\n\t2.login\n\t3.update\n\t4.view\n\t5.delete\n\t6.exit:")
    if ch1=="1":
        r.registration()
    elif ch1=="2":
       r.login()
    elif ch1=="3":
        r.update()
    elif ch1=="4":
       r.view()
    elif ch1=="5":
        r.delete()
    elif ch1=="6":
            user=input("do you want to more operation yes for y press no for n:").lower()
            if user=="y":
               choice()
            elif user=="n":
               exit()
            else:
               print("type yes or no:")
    else:
       print("select any operation:")

def choice2():
    while True:
          ch1=input("what operation are you perform:\n\t1.register\n\t2.login\n\t3.withdraw balance\n\t4.deposit balance\n\t5.view\n\t6.exit:")
          if ch1=="1":
             r.registration()
          elif ch1=="2":
            print("login")
            r.login()
          elif ch1=="3":
            print("withdraw balance")
            r.witd()

           
          elif ch1=="4":
            print("deposte balance")
            r.deposite()
          elif ch1=="5":
              print("view")
              r.viewbalance()
          elif ch1=="6":
               user=input("do you want to more operation yes for y press no for n:").lower()
               if user=="y":
                  choice()
               elif user=="n":
                  exit()
               else:
                  print("type yes or no:")
        
          else:
             print("select any operation:")

def choice():
  ch=input("select your role:\n\t1.Banker\n\t2.Customer\n:")

  if ch=="1":
    choice1()

  elif ch=="2":
      choice2()

  else:
      print("'select any roles")
choice()




