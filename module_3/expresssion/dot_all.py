import re

str="this is pyhton! that is "

x=re.findall("p....n",str)

y=re.findall("this|that",str)
print(x)
print(y)