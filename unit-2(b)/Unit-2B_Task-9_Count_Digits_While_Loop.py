#Write a python program to count the number of digits in a number using while loop


n = int(input("Enter a number: "))
count = 0

while n > 0:
    count = count + 1
    n = n // 10

print("Number of digits:", count)