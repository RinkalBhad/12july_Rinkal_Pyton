import pymysql
import re
try:
    con=pymysql.connect(host="localhost",user="root",password="",database="assesment_2")
    cur=con.cursor()
    print("connected.....")

except Exception as e:
    print(e)

x="create table login1(id int primary key auto_increment,username text,password varchar(20),email varchar(20),balance int)"

try:
     cur.execute(x)
     print("table created.....")
except Exception as e:
     print(e)


class login:
     nm=''
     pswd=''
     email=''
     r=''
     def registration(self):
        self.nm=input("username:")
        self.pswd=(input("password:"))
      
        self.email=input("enter email:")
        ptn="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        self.r=re.search(ptn,self.email) 

     def printdata(self):

        if self.r:
           x=f"insert into login1(username,password,email)values('{self.nm}','{self.pswd}','{self.email}')"
           cur.execute(x)
           con.commit()
           print("Register sucessfull.....")
        else:
            print("enter propoer email...")
           # l.registration()
            #l.printdata()

class loginn(login):

      def registration(self):
          return super().registration()
      
      def pritdata(self):
        cur.execute(f"select * from login1 where username='{self.nm}' and password='{self.pswd}'")

        data=cur.fetchone()
        if data is not None:
            print("Login successful!")
            print(data)
         
        else:
            print("Invalid username and password.")
            l.registration()
            l.pritdata()
    
l=loginn()
l.registration()
l.pritdata()

         
         