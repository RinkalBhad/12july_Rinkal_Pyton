try:
    s=int(input("enter a:"))
    s1=int(input("enter b:"))
    print("sum is:",s+s1)

except Exception as r:
    print(r)

finally:
    print("this is finally block")