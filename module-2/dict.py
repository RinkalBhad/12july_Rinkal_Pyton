'''d={"id":"1",
   "name":"rinkal",
   "city":"Rajkot"
}
print(d)
print(d.keys())
print(d.values())
print(d.items())
'''
'''print(d['name'])
print(d.get('name'))

print(len(d))

if "rinkal" in d.values():
    print("yes")
else:
    print("noo")'''

    
'''if "name" in d:
    print("yes")
else:
    print("no")
'''
'''print(d)
d['id']=2
print(d)
d['subject']="python"
print(d)
d.pop("id")
print(d)
del d['name']
print(d)
d.clear()
print(d)

newdict=d.copy()
print(newdict)'''


#nested dictionart________________________________________



d={
    "abc":{"rno":"1","name":"rinkla","Age":"20"},
    "xyz":{"rno":"10","name":"jkl","Age":"29"},
     "pno":[12345,5874875]
}
print(d)
print(d["pno"])
print(d["pno"][1])
'''print(len(d))
print(d["abc"])
print(d["abc"]["Age"])
print(d["xyz"]["rno"])

d["abc"]["name"]="pqr"
print(d["abc"])
d["abc"]["sub"]="python"
print(d["abc"])

del d["abc"]["Age"]
print(d["abc"])

d={
    "gujrat":["somnath","dwarka","junagadh"],
    "rajstha":["jaipur","udaipurr"]

}
print(d)
print(d["gujrat"])
'''