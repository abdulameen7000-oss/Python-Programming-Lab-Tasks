#Write a python program to find the sum and average of N numbers using for loop

n = int(input("Enter N: "))
sum = 0

for i in range(n):
    num = int(input("Enter number: "))
    sum = sum + num

average = sum / n

print("Sum =", sum)
print("Average =", average)