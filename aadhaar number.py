aadhaar = input("Enter your 12-digit Aadhaar number:")
if len(aadhaar)==12 and aadhaar.isdigit():
    hidden = "*" * 8 + aadhaar [-4:]
    print(f"masked aadhaar number:",{hidden})
   