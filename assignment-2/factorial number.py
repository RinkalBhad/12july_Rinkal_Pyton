# Write a Python program to get the Factorial number of given number

number=int(input("enter number "))

fact=1

for i in range(number,0,-1):
    fact=fact*i
print(f"{number} number factorial is",fact)