import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password='',database="student")
    print("connected")

except Exception  as e:
    print(e)


cur=con.cursor()
'''create="create table emp(id int primary key auto_increment,name text,city text)"
try:
    cur.execute(create)
    con.commit()
    print("table created...")

except Exception as e:
    print(e)'''

'''
insert="insert into emp(name ,city)values('xyz','baroda'),('abc','surat'),('jkl','ahemdabad')"
try:
    cur.execute(insert)
    con.commit()
    print("inserted")

except Exception as e:
    print(e)'''


'''update="update emp set name='aaa' where id=2"
try:
    cur.execute(update)
    con.commit()
    print("updated")

except Exception as e:
    print(e)'''


select="select * from emp"
try:
    cur.execute(select)
    #d=cur.fetchall()
    #d=cur.fetchmany(2)
    d=cur.fetchone()
    print(d)

except Exception as e:
    print(e)