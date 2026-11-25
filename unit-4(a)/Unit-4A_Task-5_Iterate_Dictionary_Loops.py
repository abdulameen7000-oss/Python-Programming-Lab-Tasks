#Implement a Python program that prints keys, values and items of a subject-marks dictionary using loops

marks = {
    "Maths": 90,
    "Physics": 85,
    "Chemistry": 88
}

print("Keys:")
for key in marks.keys():
    print(key)

print("Values:")
for value in marks.values():
    print(value)

print("Items:")
for key, value in marks.items():
    print(key, ":", value)