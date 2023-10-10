#  Write python program that user to enter only odd numbers, else will raise an exception


try:
   n=int(input("enter number:"))

   if n%2==0:
     raise ValueError
   print(n)

except ValueError:
   print("enter only odd number:")
    