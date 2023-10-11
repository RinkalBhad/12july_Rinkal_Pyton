import pymysql
import re
try:
    con=pymysql.connect(host="localhost",user="root",password="",database="assesment_2")
    cur=con.cursor()
    print("connected.....")

except Exception as e:
    print(e)

x="create table login(id int primary key auto_increment,username text,password varchar(20),email varchar(20),balance int)"

try:
     cur.execute(x)
     print("table created.....")
except Exception as e:
     print(e)



def registration():
       nm=input("username:")
       pswd=(input("password:"))
      
       email=input("enter email:")
       ptn="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
       r=re.search(ptn,email) 
          
      
       if r:
           x=f"insert into login(username,password,email)values('{nm}','{pswd}','{email}')"
           cur.execute(x)
           con.commit()
           print("Register sucessfull.....")
       else:
            print("enter propoer email...")
            registration()

     
#registration()

def login():
      name=input("enter username:")
      pswd=input("enter password:")

      cur.execute(f"select * from login where username='{name}' and password='{pswd}'")

      data=cur.fetchone()
      if data is not None:
          print("Login successful!")
         
      else:
          print("Invalid username and password.")
          login() 
#login()

def update():
     print("what do you want to update:")
     ch=input("\t1.username\n\t2.password\n\t3.eamil\n")
     if ch=="1":
          print("username")
          username()
     elif ch=="2":
          print("password")
          password()
     elif ch=="3":
          print("email")
          email()
 

def username():
     nm=input("enter your old name:")
    
     cur.execute(f"select username from login where username='{nm}'")
     if cur.fetchone() is not None:
           newnm=input("enter your updated name:")
           cur.execute(f"update login set username='{newnm}' where username='{nm}'")
           con.commit()
           print("update succesfull...")

     else:
          print("invalid username...")


def password():
     nm=input("enter your  username:")
    
     cur.execute(f"select username from login where username='{nm}'")
     if cur.fetchone() is not None:
           newpass=input("enter your password:")
           cur.execute(f"update login set password='{newpass}' where username='{nm}'")
           con.commit()
           print("update succesfull...")

     else:
          print("invalid username...")


def email():
     nm=input("enter your username:")
    
     cur.execute(f"select username from login where username='{nm}'")
     if cur.fetchone() is not None:
           newemail=input("enter your updated email:")
           cur.execute(f"update login set email='{newemail}' where username='{nm}'")
           con.commit()
           print("update succesfull...")

     else:
          print("invalid username...")


def view():
     select="select username,password,email from login"
     try:
          if cur.execute(select):
           data=cur.fetchall()
           for i in data:
              print(i)
          else:
               print("table is empty...")
     except Exception as e:
          print(e)



 
def particulardelete():
     user=input("which id that you want to delete:")
     delete=f"delete from login where id='{user}'"
     try:
        cur.execute(delete)
        con.commit()
        print("deleted...")

     except Exception as e:
        print(e)

def alldelete():
     delet=("delete from login")
     try:
          cur.execute(delet)
          con.commit()
          print("delete all customer succesfully...")
     except Exception as e:
          print(e)


def delete():
     print("what do you want to:")
     ch=input("\t1.delete paticular customer:\n\t2.delete all custoemer:")
   
     if ch=="1":
          particulardelete()
     elif ch=="2":
          alldelete()
     else:
          print("select any operation...")

def witd():
      name=input("enter username:")
      pswd=input("enter password:")

      cur.execute(f"select * from login where username='{name}' and password='{pswd}'")

      data=cur.fetchone()
      if data is not None:                      
          amount=int(input("enter amount that you want to withdraw:"))
          try:
               cur.execute(f"select balance from login where username='{name}'")
               balance=cur.fetchone()[0]
               if balance>amount:
                  update=balance-amount
                  cur.execute(f"update login set balance='{update}' where username='{name}'")
                  con.commit()
                  print("withdraw successfully.......")
               else:
                    print("inceffiecent balance...")
          except Exception as e:
               print(e)  

      else:
           print("invalid username and password...")
           witd()
  


def deposite():   

          name=input("enter username:")
          pswd=input("enter password:")

          cur.execute(f"select * from login where username='{name}' and password='{pswd}'")

          data=cur.fetchone()
          if data is not None:                      
               amount=int(input("enter amount that you want to deposite:"))
               try:
                    cur.execute(f"select balance from login where username='{name}'")
                    balance=cur.fetchone()[0]
               
                    update=balance+amount
                    cur.execute(f"update login set balance='{update}' where username='{name}'")
                    con.commit()
                    print("deposite successfully.......")
               
               except Exception as e:
                    print(e)  

          else:
               print("invalid username and password...")
               deposite()



def viewbalance():

      name=input("enter username:")
      pswd=input("enter password:")

      cur.execute(f"select * from login where username='{name}' and password='{pswd}'")

      data=cur.fetchone()
      if data is not None:
           try:
               show=f"select * from login where balance "
               cur.execute(show)
               data=cur.fetchall()
               for i in data:
                    print(i)   
           except Exception as e:
                print(e)
      else:
           print("invalid username and password...")
           viewbalance()

