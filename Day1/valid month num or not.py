# 11.write a python program to read the month number as input from the user and check whether it is a valid month number or not

num= int(input('enter a number:'))
if(num>=1 and num<=12):
    print(f"{num} is valid month number")
else:
    print(f"{num} is invalid month number") 