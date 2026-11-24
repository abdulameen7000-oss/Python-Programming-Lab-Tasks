#Implement a Python program that defines a function to calculate simple interest with parameters principal, time, and rate (default rate = 5); call it using the default rate and also with an explicit rate

def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Using default rate
print("Simple Interest (Default Rate):", simple_interest(1000, 2))

# Using explicit rate
print("Simple Interest (Explicit Rate):", simple_interest(1000, 2, 10))