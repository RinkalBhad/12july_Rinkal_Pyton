import pymysql
try:
   con=pymysql.connect(host="localhost",user="root",password='',database="student")
   cur=con.cursor()
   print("connected...")

except Exception as e:
   print(e)


class data:
   
   balance=0
   amount=0
   pin=''

   def register(self):
      self.pin=input("enter pin:")
      self.balance=int(input("enter balance:"))
      user=f"insert into atm (balance,pin) values('{self.balance}','{self.pin}')"
      try:
         cur.execute(user)
         con.commit()
         print("inserted successfully.....")

      except Exception as e:
         print(e)

class another(data):
    def deposite(self):
       self.amount=int(input("enter how many amount to deposite:"))
       cur.execute("select balance from atm where id=1")
       self.balance = cur.fetchone()[0]
       self.balance+=self.amount
       update=f"update atm set balance='{self.balance}' where id=1"

       try:
          cur.execute(update)
          con.commit()
          print("deposite successufully...")

       except Exception as e:
          print(e)

class withdraw(another):
    def witd(self):
       self.amount=int(input("enter amount that you want to withdraw:"))
       try:
          cur.execute("select balance from atm where id=1")
          self.balance=cur.fetchone()[0]
          update=self.balance-self.amount
          cur.execute(f"update atm set balance='{update}' where id=1")
          con.commit()
          print("withdraw successfully.......")
       except Exception as e:
          print(e)

class show(withdraw):
   def sclt(self):
      try:
         x="select* from atm"
         cur.execute(x)
         y=cur.fetchall()
         print(y)

      except Exception as e:
         print(e)

s=show()

while True:
   ch=input("Helllo would you like to proceed?\n1.create pin\n2.deposite\n3.withdraw\n4.check balance\n5.exit:")
   if ch=="1":
     s.register()

   if ch=="2":
      s.deposite()
      s.sclt()

   if ch=="3":
      s.witd()
      s.sclt()

   if ch=="4":
     s.sclt()

   if ch=="5":
      exit() 