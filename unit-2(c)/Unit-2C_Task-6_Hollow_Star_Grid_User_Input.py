#Write a python program to print a 5x5 hollow grid of stars (*); generalize the program so the grid size is based on user input

n = int(input("Enter grid size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()