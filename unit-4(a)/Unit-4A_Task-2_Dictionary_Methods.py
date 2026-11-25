#Implement a Python program that uses keys, values, items, get, update and pop on a sample dictionary

student = {"name": "Ameen", "age": 19, "marks": 90}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Get Name:", student.get("name"))

student.update({"grade": "A"})
print("After Update:", student)

student.pop("age")
print("After Pop:", student)