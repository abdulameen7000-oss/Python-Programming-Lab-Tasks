#Implement a Python program that uses a global counter and increments it inside a function using the global keyword

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()

print("Counter:", counter)