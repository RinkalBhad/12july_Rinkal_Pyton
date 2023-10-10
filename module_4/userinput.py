import pymysql
con=pymysql.connect(host="localhost",user="root",password='',database="student")

cur=con.cursor()

# insert...................................................
'''n=int(input("enter how many record of student :"))

for i in range(n):
    nm=input("enter name:")
    ct=input("enter city:")
    insert=f"insert into emp (name,city)values('{nm}','{ct}')"
    try:
      cur.execute(insert)
      con.commit()
      print("inserted.....")

    except Exception as e:
       print(e)'''

#updated.................................................
'''
i=input("enter id that update:")

def both():
  nm=input("enter name:")
  ct=input("enter city:")

  update=f"update emp set name='{nm}',city='{ct}' where id='{i}'"
  try:
      cur.execute(update)
      con.commit()
      print("updated...")

  except Exception as e:
       print(e)

def name():
     nm=input("enter name:")
     update=f"update emp set name='{nm}' where id='{i}'"
     try:
        cur.execute(update)
        con.commit()
        print("updated...")

     except Exception as e:
         print(e)


def city():
    ct=input("enter city:")
    update=f"update emp set city='{ct}' where id='{i}'"
    try:
        cur.execute(update)
        con.commit()
        print("updated...")

    except Exception as e:
         print(e)



ch=input("what want to update:\n 1.city\n 2.name\n 3.both::")
if ch=="1":
    city()

elif ch=="2":
    name()

elif ch=="3":
    both()

else:
    print("select any number:")'''

# delete.....................................

user=input("which id that you want to delete:")

delete=f"delete from emp where name='{user}'"
try:
    cur.execute(delete)
    con.commit()
    print("deleted...")

except Exception as e:
    print(e)