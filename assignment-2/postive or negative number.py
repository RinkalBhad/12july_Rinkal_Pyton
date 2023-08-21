#Write a Python program to check if a number is positive, negative or  zero.

number=int(input("enter any number that you want "))

if number>0:
    print(f"{number} is postive number")
elif number<0:
    print(f"{number} is negative number")
else:
    print("number is zero")