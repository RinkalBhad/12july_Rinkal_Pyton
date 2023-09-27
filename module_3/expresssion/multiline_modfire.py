import re

str="This is Python!"
x=re.findall("^This",str)

y=re.findall("^[A-Z]",str)
y1=re.findall("[^a-z]",str)  # it is reverse of [a-z]
z=re.findall("on!$",str)

f=re.findall("!$",str)

print(x)

print(y)
print(y1)
print(z)
print(f)