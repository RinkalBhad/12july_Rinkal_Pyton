# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

number=int(input("enter number "))

if number%2==0:
    print(f"{number} number is 'even' ")

else:
    print(f"{number} number is 'odd' ")