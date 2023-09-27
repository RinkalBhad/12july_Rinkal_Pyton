import re

str="my name is Bhad Rinkal! 1234556"

x=re.findall("\w",str)         #match word character...
print(x)

y=re.findall("\W",str)          #match nonword character...
print(y)

d=re.findall("\d",str)     #Matches digits.
print(d)

d1=re.findall("\D",str)    # Matches non digits.
print(d1)

s=re.findall("\s",str)    # Matches whitespaces
print(s)

s2=re.findall("\S",str)   # Matches non whitespaces
print(s2)

a=re.findall("\Amy",str)   #Matches only at the start of the string.
print(a)

e=re.findall("56\Z",str)   # ends with 56
print(e)