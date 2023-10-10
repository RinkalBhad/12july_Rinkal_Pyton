import pymysql
try:
  con=pymysql.connect(host="localhost",user="root",password='',database="assesment_2")
  cur=con.cursor()
  #print("connected")

except Exception as e:
  print(e)

class register:
     name=''
     password=''

     def data(self):
       self.nm=input("username:")
       self.pswd=(input("password:"))

       x=f"insert into login(username,password)values('{self.nm}','{self.pswd}')"

       try:
           cur.execute(x)
           con.commit()
           print("Register sucessfull.....")

       except Exception as e:
          print(e)

class log(register):
   def logindata(self):

      nm=input("enter name:")
      psd=input("enter password:")

      x=f"select* from login"
      try:
        cur.execute(x)
        y=cur.fetchall()[0]
        if nm==self.nm and psd==self.pswd :
            print("login successfully....")

        else:
           print("invalid username and password...")
           l=log()
           l.logindata()


      except Exception as e:
         print(e)


class withdraw(log):
    #balance=25000
    def logindata(self):
         return super().logindata()
    def witd(self):
        
       self.amount=int(input("enter amount that you want to withdraw:"))
       try:
          cur.execute("select balance from login where id=1")
          self.balance=cur.fetchone()[0]
          update=self.balance-self.amount
          cur.execute(f"update login set balance='{update}' where id=1")
          con.commit()
          print("withdraw successfully.......")
       except Exception as e:
          print(e)

l=log()
l.logindata()