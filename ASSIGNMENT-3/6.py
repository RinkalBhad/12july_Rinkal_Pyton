# Write a Python program to count the number of strings where the string length is 2 or more and 
#the first and last character are same from a given list of strings. 

s=["my","name","is","arinkla"]
for i in s:
    if len(i)>2 and i[0]==i[-1]:
          print(f"length of {i} is:",len(i))
    


    
       
