#  Write a Python program to check whether an element exists within a tuple

t=(12,23,22,32,43,54,98,90,54)
print(t)

n=int(input("enter number that you want check :"))
try:
    if n in t:
        print(f"yes {n} exists in tuple")
    else:
        print(f"no {n} not exists in tuple")
        
except Exception as e:
    print(e)