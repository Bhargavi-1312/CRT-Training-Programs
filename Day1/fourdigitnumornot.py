# 5.WPP to read an integer as input from the user and check whether it is a four digit or not
num=int(input('enter the integer:'))
res = "four digit number " if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)) else "not a four digit number"
print(res)  

