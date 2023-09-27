'''try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("sum:",a+b)
except:
    print("error")   # this error is user define '''

try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("sum:",a+b)
except Exception as e:   # this error is built in
    print(e) 
else:             # this line execute when try block run succesfully
    print("this is else block")