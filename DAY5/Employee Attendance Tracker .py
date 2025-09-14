attendance = input("Enter attendance record (P for present, A for absent, L for late): ").upper()
days_absent = attendance.count('A')
late_days = attendance.count('L')
if days_absent >=5 or late_days >= 3:
    print("Employee is not eligible ")
else:
    print("Employee is eligible")    
