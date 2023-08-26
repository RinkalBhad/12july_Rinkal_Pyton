l=[50,30,60,70,77,10,33]

''''print(l)
l.insert(1,10)
print(l)
l.append(90)
print(l)
l.pop()
print(l)
l.remove(30)
print(l)
l.sort()
print(l)

l1=["rinkal","bhad"]
print(l1)

l1.extend(l)
print(l1)

print(l[6])
print(l[3::])
print(l[-1::-6])
print(l[::-1])
print(len(l1))
'''

"""if 100 in l:
    print("yes")
else:
    print("no")

print(l.index(70))"""

'''for i in l:
    print(i,l.index(i))
'''
'''n=0
for i in l:
    print(f"{i}-{n}")
    n+=1'''


# nested list________________________________________________________________

'''n=[10,20,30,[40,50],("rinkla","bhad"),{"id":"1","name":"rinkla"}]
print(n)
print(len(n))
print(n[3][1])
print(n[4])
n[3][1]=90
print(n[3])
print(n[4][1])
print(n[5])
print(n[5]['name'])
n[5]["subject"]="python"
print(n)
n[5]["id"]=2
print(n)'''


l=[10,20,30,40,50]
l[4]=90
print(l)