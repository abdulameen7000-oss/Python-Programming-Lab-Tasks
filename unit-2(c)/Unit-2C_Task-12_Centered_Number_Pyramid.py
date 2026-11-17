#Write a python program to print a centered pyramid pattern of numbers

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()