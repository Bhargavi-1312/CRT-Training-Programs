class Student:
    def __init__(self):
        print()
        print(f"student object created")
        print()
#mutator or setter method
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_branch(self, branch):
        self._branch = branch

 #accessor or getter method           

    def get_name(self):
        print(f"student name is: {self._name}")

    def get_age(self):
        print(f"student age is: {self._age}")

    def get_branch(self):
        print(f"student branch is: {self._branch}")


s1 = Student()
s1.set_name("Alice")
s1.set_age(20)
s1.set_branch("Computer Science")
s1.get_name()
s1.get_age()        
s1.get_branch()