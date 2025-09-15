class Student:
    def __init__ (self,name,age,branch,registerno,phoneno,guardian):
        self.stdName=name
        self.age=age
        self.branch=branch
        self.registerno=registerno
        self.phoneno=phoneno
        self.guardian=guardian
S1=Student("bhanu", 20, "MBA","22F213",9087766794,"Nirmala")
print(f"student name is: {S1.stdName}" ) 
print(f"student age is: {S1.age}" )
print(f"student branch is: {S1.branch}" )
print(f"student registerno is: {S1.registerno}" )
print(f"student phoneno is: {S1.phoneno}" )
print(f"student guardian is: {S1.guardian}" )
      
