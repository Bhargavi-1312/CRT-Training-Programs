#4.EMPLOYEE OVERTIME PAY
hours_worked=int(input("Enter the hours :"))
standard_hours=8
overtime_rate=100
if(hours_worked>standard_hours):
    overtime_hours = hours_worked - standard_hours
    overtime_pay = overtime_hours*overtime_rate
    print(f"overtime pay: ₹{overtime_pay}")
else:
    print("no overtime pay")   