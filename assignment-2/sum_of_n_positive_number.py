# Write a python program to sum of the first n positive integers.

num=int(input("enter number "))
s=0
if num>0:
      for i in range(num+1):
            s=s+i
      print(s)
else:
      print("plz enter positive number ")

