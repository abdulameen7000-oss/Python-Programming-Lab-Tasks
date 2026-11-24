#	Implement a Python program that defines a function using *args to find the sum of any number of values

def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum:", find_sum(10, 20, 30, 40, 50))