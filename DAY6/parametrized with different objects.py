class Student:
    def __init__ (self,name,age,branch):
        self.stdName=name
        self.age=age
        self.branch=branch
    def display(self):
        print(f"student name is: {self.stdName}" ) 
        print(f"student age is: {self.age}" )
        print(f"student branch is: {self.branch}" )
S1=Student("bhanu", 20, "MBA")
S1.display()
S2=Student("manu", 10, "b.tech")
S2.display()        
