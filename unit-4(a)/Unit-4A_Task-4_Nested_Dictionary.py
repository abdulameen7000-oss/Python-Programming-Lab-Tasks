#Implement a Python program that stores students in a nested dictionary and prints name and marks

students = {
    1: {"name": "Ameen", "marks": 90},
    2: {"name": "Krishna", "marks": 85},
    3: {"name": "Rahul", "marks": 88}
}

for roll, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()