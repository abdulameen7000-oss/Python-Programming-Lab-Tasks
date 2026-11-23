#Implement a Python program to remove duplicates from a list using sets

# Create a list
my_list = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", my_list)

# Remove duplicates using set
new_list = list(set(my_list))

# Display the result
print("List after removing duplicates:", new_list)