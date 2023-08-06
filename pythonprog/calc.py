choice=input("enter your choice")

print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

a=int(input("enter a"))
b=int(input("enter b"))

if choice=="1":
    print(a+b)

elif choice=="2":
    print(a-b)
elif choice=="3":
    print(a*b)
else:
    print(a/b)