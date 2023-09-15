#  Write a Python program to get unique values from a list

l=[]
n=int(input("how many number enter you?:"))
for i in range(n):
    i=int(input("enter number:"))
    if i not in l:
       l.append(i)
print(l)
