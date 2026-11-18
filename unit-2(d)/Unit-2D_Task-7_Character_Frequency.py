#Implement a Python program to count the frequency of each character in a string

s = input("Enter a string: ")

for ch in s:
    if ch not in "":
        print(ch, ":", s.count(ch))
        s = s.replace(ch, "", s.count(ch))