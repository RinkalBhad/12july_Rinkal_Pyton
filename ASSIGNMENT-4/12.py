#  Write a Python program to copy the contents of a file to another file.  

f=open("li.txt","r")
f1=open("sample.txt","w")


data=f.readlines()
for i in data:
   f1.write(f"{i}")

