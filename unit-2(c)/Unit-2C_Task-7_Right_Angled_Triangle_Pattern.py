#Write a python program to print a right-angled triangle pattern; read the number of rows and the symbol to print (e.g. * or 0) from the user

n = int(input("Enter number of rows: "))
s = input("Enter a symbol: ")

for i in range(1, n + 1):
    for j in range(i):
        print(s, end=" ")
    print()