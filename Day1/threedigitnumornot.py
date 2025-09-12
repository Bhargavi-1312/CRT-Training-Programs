# 4.WPP to read an integer as input from the user check whether it is a three digit number or not
#ternary operator
num=int(input('enter the integer:'))
res = "three digit number " if((num>=100 and num<=999) or (num>=-999 and num<=-100)) else "not a three digit number"
print(res)  