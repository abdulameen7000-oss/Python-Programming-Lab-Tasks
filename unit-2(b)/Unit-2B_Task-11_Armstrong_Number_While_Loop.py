#Write a python program to check whether a number is an Armstrong number using while loop (assume the number has 3 digits)


n = int(input("Enter a 3-digit number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")