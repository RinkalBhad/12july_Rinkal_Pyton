# Write a Python program to replace last value of tuples in a list

l=[88,(12,32,44,56,65,89),(10,20,40,30,50),(23,12)]


print("before:",l)
l[0],l[-1]=l[-1],l[0]
print("after:",l)

