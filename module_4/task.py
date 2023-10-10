import sqlite3
try:
    con=sqlite3.connect("testdb.db")
    print("connected....")
except Exception as e:
    print(e)



'''tb=input("enter table name:")
row=int(input("enter how many row you want:"))
try:
    l=[]
    for i in range(row):
        l.append(input(f"enter row {i} and datatype:"))
        column_names_str = ", ".join(l)


    con.execute(f"create table {tb}({column_names_str})")
    print("created...")

except Exception as e:
    print(e)

'''
