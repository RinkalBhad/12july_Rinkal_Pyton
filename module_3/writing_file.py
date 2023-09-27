f1=open("test.txt","w")

f1.write("my name is bhad rinkal\n")
f1.write("i am a python developer")
print("write successfully....")

if f1.writable():
    print("yes")
else:
    print("not")