# Write a Python program to remove an empty tuple(s) from a list of tuples.

l1=[(10,20,30),(32,6),(),(49.4),(),()]

for i in l1:
    if i!=():
        print(i)