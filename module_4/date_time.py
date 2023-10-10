'''import datetime
x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))'''

import pymysql
import datetime
try:
    x=pymysql.connect(host="localhost",user="root",password="",database="student")
    c=x.cursor()

    c.execute("create table da(date varchar (20))")

except Exception as e:
    print(e)


d=datetime.datetime.now()
dy=d.date()
try:
    inert=f"insert into da (date)values('{dy}')"
    c.execute(inert)
    x.commit()
    print("inserted....")


except Exception as e:
    print(e)

