s1=int(input("Enter mark of student 1: "))
s2=int(input("Enter mark of student 2: "))
s3=int(input("Enter mark of student 3: "))
s4=int(input("Enter mark of student 4: "))

if(s1>=40 and s2>=40 and s3>=40 and s4>=40):
    total=s1+s2+s3+s4
    pr=total/4
    print("the percentage of",pr)
    if pr>=70:
       print("Result Dist..")
    elif pr>=60:
       print("result is first class")
    elif pr>=50:
       print("result is second class")
    elif pr>=40:
        print("Result is pass ")

 

else:
    print("fail")