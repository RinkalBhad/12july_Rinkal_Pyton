# Write a Python function to check whether a number is perfect or not

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" Perfect Number")
else:
    print(" not a Perfect Number")