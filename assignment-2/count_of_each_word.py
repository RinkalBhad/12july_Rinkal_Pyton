#Write a Python program to count the occurrences of each word in a given sentence

str= input("Enter a sentence: ")
words = str.split()
c= {}
for word in words:
    if word in c:
        c[word] += 1
    else:
        c[word] = 1
for word, count in c.items():
    print(f"{word}: {count}")




