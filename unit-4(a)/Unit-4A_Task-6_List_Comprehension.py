#Implement a Python program that builds squares of 1–10 and even numbers using list comprehension

# Squares of numbers 1 to 10
squares = [x**2 for x in range(1, 11)]

# Even numbers from 1 to 10
even = [x for x in range(1, 11) if x % 2 == 0]

print("Squares:", squares)
print("Even Numbers:", even)