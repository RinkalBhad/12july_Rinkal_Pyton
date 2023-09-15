#Write a Python program to remove duplicates from a list.

l=[1,2,3,4,5,6,7,2,5,6]
k=[]
print("before:",l)
for i in l:
    if i not in k:
        k.append(i)
print("after:",k)