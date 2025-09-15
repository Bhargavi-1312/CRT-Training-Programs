#empname, empnum ,designation,salary,deptno
class Employee:
    def __init__(self,empname, empnum ,designation,salary,deptno):
        self.empname=empname
        self.empnum=empnum
        self.designation=designation
        self.salary=salary
        self.deptno=deptno
    def display(self):
        print(f"emp name is: {self.empname}" ) 
        print(f"empnum is: {self.empnum}" )
        print(f"designation is: {self.designation}" )
        print(f"salary is: {self.salary}" )
        print(f"deptno is: {self.deptno}" )
E1=Employee("bhanu", 207, "software",45000,34)
E1.display() 
E2=Employee("tharun", 507, "manager",40000,31)
E2.display()
E3=Employee("teja", 407, "assistant manager",34000,30)
E3.display() 
E4=Employee("tharun", 617, "accountant",35000,31)
E4.display() 
E5=Employee("tharun", 517, "civil engineer",40000,37)
E5.display()         