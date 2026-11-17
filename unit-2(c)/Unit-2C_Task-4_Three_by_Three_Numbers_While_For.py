#Write a python program to print numbers in a 3x3 grid (as shown in the hint) using while-for nested loop

i = 1
while i <= 3:
    for j in range(1, 4):
        print(j, end=" ")
    print()
    i += 1