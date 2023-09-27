import re

email="rinkla245@gmail.com"

patrn="^[a-z|0-9]+[@]+[a-z]+[\.]+[a-z]{2,3}$"

x=re.findall(patrn,email)

if x:
    print(x)
else:
    print("invalid email...")