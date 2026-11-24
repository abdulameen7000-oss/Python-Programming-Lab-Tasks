# Implement a Python program for a simple bank balance: a global balance, a function to deposit (uses global), and a function that uses a local balance to show it does not update the account

balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def local_balance(amount):
    balance = amount
    print("Local Balance:", balance)

deposit(500)
print("Account Balance:", balance)

local_balance(200)
print("Final Account Balance:", balance)