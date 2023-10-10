#  Write a Python program to count the frequency of words in a file.  

'''f=open("fi.txt","w")
f.write("my name is rinkal")
'''
f=open("fi.txt","r")
x=f.read()

c=0
for i in x.split():
     c+=1
print(c)