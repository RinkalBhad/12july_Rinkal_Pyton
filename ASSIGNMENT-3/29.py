 # Write a Python program to unzip a list of tuples into individual lists.


l=[(12,34,"r"),(78,34,"i"),(43,90,"n")]

for i in  l:
    if i!=():
        l=list(i)
        print(l)
