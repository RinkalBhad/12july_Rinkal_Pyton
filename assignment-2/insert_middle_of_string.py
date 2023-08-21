# write e a Python function to insert a string in the middle of a string

def middle(str,word):
    print(str[:len(str)//2] + word + str [len(str)//2:])

st=input("enter string ")
word=input("enter middle word ")

middle(st,word)
