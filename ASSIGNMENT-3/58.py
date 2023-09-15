# Write a Python program to read a random line from a file

import random
f=open("test.txt","r")
y=f.readlines()[::-1]
x=random.choice(y)
print(x)