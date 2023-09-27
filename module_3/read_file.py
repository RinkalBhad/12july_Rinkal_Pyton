f=open("test4.txt","r")
#print(f.read())

#print(f.readline()) # return first line

#print(f.readlines()) # return in list and also use slicing

n=1
for i in f:
    #print(i)
    print(f"line:{n}={i}")
    n+=1