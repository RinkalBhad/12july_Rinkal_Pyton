set1={"A","B","C","D","E","F"}
'''print(set1)

print(len(set1))

if "b" in set1:
    print("yes")
else:
    print("no")

for i in set1:
    print(i)'''

set1.add("G")

set1.update(["J","K","L","M"])
#set1.pop()
#set1.remove("F")

#set1.clear()
print(set1)
#set1.discard("e")
#print(set1)
print(len(set1))
newset={"R","s","T","A","B"}
x=newset.union(set1)
x=set1.intersection(newset)
print(x)

x={"a","b","c","f"}
y={"d","e","f"}
r=y.intersection(x)
print(r)
