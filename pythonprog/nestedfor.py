'''
* * * * *
* * * *
* * *
* *
*
'''

'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print(" ")'''
'''
1 2 3 4 5
1 2 3 4 
1 2 3
1 2 
1
'''
for i in range(6,1,-1):
    for j in range(1,i-1):
        print(i+1,end="")
    print()