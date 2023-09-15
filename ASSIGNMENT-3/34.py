# Write a Python script to check if a given key already exists in a dictionary.


d={"abc":74,"xyz":65,"pqr":88,"efg":89}
n=input("enter key that you check in dictionary:")

if n in d:
    print(f"yes {n} in dictionary")
else:
    print(f"not exist")