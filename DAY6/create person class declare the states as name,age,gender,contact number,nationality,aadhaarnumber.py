class person:
    def __init__(self, name, age, gender, contact_number, nationality, aadhaar_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.nationality = nationality
        self.aadhaar_number = aadhaar_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Nationality: {self.nationality}")
        print(f"Aadhaar Number: {self.aadhaar_number}")

P1 = person("Alice", 30, "Female", "1234567890", "Indian", "1234-5678-9012")
P1.display()
P2 = person("Bob", 25, "Male", "0987654321", "American", "9876-5432-1098")  
P2.display()
P3 = person("Charlie", 28, "Male", "1122334455", "British", "1122-3344-5566")
P3.display()
P4 = person("Diana", 32, "Female", "2233445566", "Canadian", "2233-4455-6677")
P4.display()
P5 = person("Eve", 29, "Female", "3344556677", "Australian", "3344-5566-7788")
P5.display()