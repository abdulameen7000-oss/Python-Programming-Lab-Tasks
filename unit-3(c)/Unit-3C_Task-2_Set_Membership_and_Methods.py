#Implement a Python program to demonstrate set membership testing and methods (add, remove, discard)

# Create a set
s = {10, 20, 30, 40}

print("Original Set:", s)

# Membership testing
print("Is 20 present?", 20 in s)
print("Is 50 present?", 50 in s)

# Add an element
s.add(50)
print("After add:", s)

# Remove an element
s.remove(30)
print("After remove:", s)

# Discard an element
s.discard(40)
print("After discard:", s)