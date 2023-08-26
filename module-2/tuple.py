a=("python","java","android","ruby","c++")
print(a)

print(a[0:-3])
print(a[1:3])
print(len(a))

if "java" in a:
    print("yes")
else:
    print("no")

print(a.index("android"))

for i in a:
    print(f"{a.index(i)}",i)


'''del a
print(a)'''

#nested tuple__________________________________________________

'''print("__________________________________________")
a=(10,20,30,(40,50))
print(a)
print(len(a))
print(a[3][1])
del a
print(a)
'''
b=(10,20,30,40)
print(b)