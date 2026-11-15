#Write a python program to find the largest number in a series of N numbers entered by the user using for loop


n = int(input("Enter N: "))

largest = int(input("Enter number: "))

for i in range(n - 1):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)