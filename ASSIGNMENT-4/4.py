# Write a Python program to read first n lines of a file. 



f=open("one.txt","r")
n=int(input("enter numberr:"))
print(f.readlines()[0:n])
      