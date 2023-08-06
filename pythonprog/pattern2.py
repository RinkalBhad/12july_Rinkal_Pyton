'''
1
2 2
3 3 3 
4 4 4 4
5 5 5 5 

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")

   
    1 2 3 4 5
    1 2 3 4
    1 2 3 
    1 2
    1

for i in range(5,1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

    1
    2 3
    4 5 6
    7 8 9 10
    '''
n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print(" ")