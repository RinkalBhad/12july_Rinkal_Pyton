# write a Python program to read a file line by line and store it into a list 

l=[]
f=open("one.txt","r")
l=f.readlines()
print(type(l),l)

