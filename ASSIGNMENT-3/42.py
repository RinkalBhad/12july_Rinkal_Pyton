#  Write a Python program to print all unique values in a dictionary.  

list1 = [{'name1':'robert'},{'name2':'john'},{'name3':'jim'},
         {'name4':'robert'}]
list2 = []
for i in list1:
    for j in i.values():
        if j not in list2:
            list2.append(j)
print(list2)