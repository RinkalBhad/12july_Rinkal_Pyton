# Write a Python program to count the number of lines in a text file.  

f=open("one.txt","r")
x=f.readlines()
#print(len(x))
s=0
for i in x:
    s+=1
print(s)
