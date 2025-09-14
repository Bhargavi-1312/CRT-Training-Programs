#Electricity Bill Calculator
units=int(input("Enter the units:"))
if units<=100:
    bill = units*5
elif units<=200:
    bill = units*7
else:
    bill = units * 10
print(f"total bill = {bill}")            