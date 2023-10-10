#  Write a Python program to write a list to a file.  

l=[10,20,30,40,50]

f=open("li.txt","w")
f.write(f"{l}")
print("write sucessfull..")