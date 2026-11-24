#Implement a Python program that shows a local variable inside a function does not change a global variable with the same name

balance = 1000

def show_balance():
    balance = 500
    print("Local Balance:", balance)

show_balance()

print("Global Balance:", balance)
