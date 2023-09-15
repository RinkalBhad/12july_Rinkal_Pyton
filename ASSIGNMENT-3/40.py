# Write a Python program to map two lists into a dictionary 

l=["id","name","city"]
l1=["101","rinkal","rajkot"]

def le(l,l1):
   return l+l1

x=map(le,l+l1)
print(tuple(x))