#Write a python program to print a 5x5 grid of stars (*); generalize the program so the grid size is based on user input

n = int(input("Enter grid size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()