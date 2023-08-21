# Write a Python function to reverses a string if its length is a multiple of 4

def revese(str):
    if len(str)%4==0:
       print(str[::-1])
    else:
       print("enter valid string")

s=input("enter string ")
revese(s)
