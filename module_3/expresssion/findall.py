import re

mystr="This is String This is python programming.."

#x=re.findall("This",mystr)
#x=re.findall("this",mystr)
#x=re.findall("is",mystr)
x=re.findall("N",mystr)

print(x)

if x:
       print("match done..")
else:
    print("error..")


