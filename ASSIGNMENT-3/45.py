# Write a Python program to find the highest 3 values in a dictionary  

d={'a': 1, 'r': 5, 'k': 89, 'l': 75, 's': 43, 'g': 87, 'o': 76}

'''x=(sorted (d.values(),reverse=True))

print(x[:3])'''

x=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(x[:3])