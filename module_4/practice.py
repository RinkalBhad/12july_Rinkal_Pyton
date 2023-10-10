from getpass import getpass
import sqlite3
con=sqlite3.connect("testdb.db")
cur=con.cursor()
try:
  log=input("enter username:")
  pswd=getpass("enter password:")
  cur.execute(f"SELECT name from data WHERE name='{log}' AND Password = '{pswd}'")
  if not cur.fetchone():  # An empty result evaluates to False.
     print("Login failed")
  else:
     print("Welcome")

except Exception as e:
  print(e)
