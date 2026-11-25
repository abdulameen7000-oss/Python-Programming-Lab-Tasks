#Implement a Python program that sorts a list of student dictionaries by marks (ascending and descending)

students = [
    {"name": "Ameen", "marks": 85},
    {"name": "Krishna", "marks": 90},
    {"name": "Rahul", "marks": 75},
    {"name": "Arjun", "marks": 95}
]

# Ascending order
ascending = sorted(students, key=lambda x: x["marks"])
print("Ascending Order:")
print(ascending)

# Descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Descending Order:")
print(descending)