# Write a Python function that takes two lists and returns true if they have at least one common member

def list(l,l2):
   result=False
   for i in l:
        for j in l2:
            if i==j:
               result=True
               return result
          
print(list([10,20,30,50,80],[22,60,20,99,80]))







    



          