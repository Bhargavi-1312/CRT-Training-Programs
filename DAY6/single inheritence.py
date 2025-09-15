class Person:
    def __init__(self, name, age, gender):
        print("Person object is created")
        self.name = name
        self.age = age
        self.gender = gender
class Student(Person):
    def __init__(self, name, age, gender, student_id,branch):
        super().__init__(name, age,gender)
        self.student_id = student_id
        self.branch=branch
        print("Student object is created")
s1=Student("Alice", 20, "Female", "S123", "Computer Science")
print(s1.name)  # Output: Alice
print(s1.age)   # Output: 20    
print(s1.gender)  # Output: Female
print(s1.student_id)  # Output: S123
print(s1.branch)  # Output: Computer Science