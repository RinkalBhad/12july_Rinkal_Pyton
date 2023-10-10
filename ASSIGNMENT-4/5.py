#  Write a Python program to read last n lines of a file



f=open("one.txt","r")
n=int(input("enter number:"))
print(f.readlines()[n:-1])
      