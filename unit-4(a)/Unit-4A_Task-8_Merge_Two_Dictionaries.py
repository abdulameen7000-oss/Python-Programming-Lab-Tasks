#Implement a Python program that merges two dictionaries with update() without changing the original

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Create a copy of original dictionary
merged = dict1.copy()

# Merge using update()
merged.update(dict2)

print("Original Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)