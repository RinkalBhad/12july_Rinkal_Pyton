#   Write a Python program to find the repeated items of a tuple

t=(12,34,54,66,78,34,12,90,88,45)
print(t)

for i in t:
   if t.count(i)>1:
    
      print(i)

