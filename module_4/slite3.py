import sqlite3
try:
    con=sqlite3.connect("testdb.db")
    print("connected...")
except Exception as e:
    print(e)


'''cr="create table student(id integer ,name text,sub text)"
try:
    con.execute(cr)
    print("created..")

except Exception as e:
    print(e)
'''
'''
inst="insert into student (id,name,sub)values(2,'abc','c++'),(3,'jkl','c'),(4,'xyz','java')"
try:
    con.execute(inst)
    con.commit()
    print("inserted..")
except Exception as e:
    print(e)'''

'''up="update student set sub='asp' where id=3"
try:
    con.execute(up)
    con.commit()
    print("updated...")
except Exception as e:
    print(e)'''

'''
d="delete from student where id=2"
try:
    con.execute(d)
    con.commit()
    print("deleted...")

except Exception as e:
    print(e)'''

'''c=con.cursor()
s="select* from student"

try: 
      c.execute(s)
      data=c.fetchall()
      #data=c.fetchmany(2)
      #data=c.fetchone()
      print(data)

      for i in data:
           print(i)
      
except Exception as e:
    print(e)
'''
