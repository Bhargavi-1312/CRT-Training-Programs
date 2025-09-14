string=input("Enter the string:")
alphabet,digit,specialchar=0,0,0
for char in string:
    if char.isalpha():
        alphabet+=1
    elif char.isdigit():
        digit+=1
    else:
        specialchar+=1
print(f"count of Alphabetic characters is :",{alphabet})
print(f"count of digits is :",{digit})
print(f"count of special characters is :",{specialchar})