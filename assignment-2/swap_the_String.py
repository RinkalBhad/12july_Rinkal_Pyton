# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

str=input("enter first string ")
str2=input("enter second string ")

print(str+("\t"),str2)

print(str.replace(str[0:2],str2[0:2]))
print(str2.replace(str2[0:2],str[0:2]))