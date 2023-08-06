'''name=input("enter your name")
print("good afternoon",name)'''

letter=''' Dear </NAME/>
Greetings from ABC coding house. I am happy  to tell you about  your selection 
You are selected!
Have a greate  day ahead!
Thanks and and regards,
Bill

Date:</DATE/>
'''

name=input("enter your name  \n")
date=input("Enter date")
letter=letter.replace("</NAME/>",name)
letter=letter.replace("</DATE/>",date)
print(letter)