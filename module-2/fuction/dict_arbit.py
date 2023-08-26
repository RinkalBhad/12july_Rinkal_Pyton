def test(value):
    print("id",value['id'])
    print("name",value['name'])
    print("city",value['city'])

#test({"id":"101","name":"rinkal","city":"rajiot"})
i=int(input("enter id"))
n=input("enter name")
c=input("enter city")
x=i,n,c
test(x)