#  Write a Python program to check multiple keys exists in a dictionary  

di={
    "id":1,
    "name":"rinkal",
    "country":"india"
}

c=0
for i in di.keys():
    c=c+1
if c>2:
    print("yes")
else:
    print("no")