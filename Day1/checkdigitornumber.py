# 2. program to read an integer value and check whether it is a digit or number
num = int(input('Enter the integer:'))
#if-else
if(num>=-9 and num<=9):
    print("Digit")
else:
    print("Number")
#ternary operator second method
res="Digit" if(num>=-9 and num<=9) else "Number"
print(res) 