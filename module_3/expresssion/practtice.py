import re

'''str="my name is rinkla.!,rinkal@gmail.com"
s="xyz abxc zxyy jkl zxy"
#m=re.search("\.",str)
#m=re.search("[@]",str)0
#m=re.search("is",str)
#m=re.search("^m",str)

#m=re.search("^c",str)
#m=re.search(".com$",str)
#m=re.findall("n..e",str)
#m=re.findall("com|rinkla",str)
#m=re.findall("ri?n",str)
m=re.findall("xy+z",s)

print(m)'''


'''str="python is most power2 @ full idea 2341"

#s=re.findall("\Apy",str)
#s=re.finall("py\B",str)
#s=re.findall("\d",str)
#s=re.findall("\D",str)
#s=re.findall("\s",str)
#s=re.findall("\S",str)
#s=re.findall("\w",str)
#s=re.findall("\w",str)
s=re.findall("1\Z",str)

print(s)
'''

'''s="python programming HRLLO lanngulage 123435hello95405"

#f=re.findall("[prm]",s)  # prm charctter aavse
#f=re.findall("[^prm]",s)  # prm sivay badhu aavse
#f=re.findall("[a-t]",s)  # a thi t sudhi na badha charcter aavse
#f=re.findall("[01234]",s)
#f=re.findall("[0-9]",s)
#f=re.findall("[0-7][0-9]",s)
f=re.findall("[A-Za-z]",s)
print(f)'''

'''s="Rinkla bhad my name is Bhhad"
x=re.findall("[A-Z][a-z]*",s)

print(x)'''

#phone number

'''phn="222-444-8797"

if re.search("\d{3}-\d{3}-\d{4}",phn):
    print("okk")
else:
    print("invlaid")'''

#email...


import re
'''e="rinkal2455@gmail.com"
email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

if re.search(email,e):
    print("right emial",e)
else:
    print("invalid")'''

pn="123456789 0"
if re.search("\d{5}\W\d{5}",pn):
    print("ringht",pn)
else:
    print("invliad")