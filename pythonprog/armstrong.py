'''n=int(input("enter n"))
sum=0
temp=n   

while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    fd=temp//10

if sum==n:
    print("armstrong number")

else:
    print("not armstrong")'''



'''n=[30,60,50,90,80]
for i in n:
    print(i)
    if n%30==0:
      print("it is 30 table")
    else:
      print("not 30 table")'''

l=["a","e","i","o","u"]
if i in l:
    print("vowel",i)
else:
    print("consonent",i)
    