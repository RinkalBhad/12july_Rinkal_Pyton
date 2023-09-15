#  Write a Python script to sort (ascending and descending) a dictionary by value. 


di={"abc":74,"xyz":65,"pqr":88,"efg":89}

x=sorted(di.items(),key=lambda x:x[1])
print(x)

