import re

str="This is Python ! 4343434"
x=re.findall("[A-Z]",str)
y=re.findall("[a-z]",str)

z=re.findall("[0-9]",str)
r=re.findall("[a-zA-Z]",str)
l=re.findall("[a-zA-Z0-9]",str)

print(x)
print(y)
print(z)
print(r)
print(l)

