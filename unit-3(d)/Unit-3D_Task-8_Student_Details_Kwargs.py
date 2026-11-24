#Implement a Python program that defines a function using **kwargs to display a student's name and subject marks

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(Name="Ameen", Maths=90, Physics=85, Chemistry=88)