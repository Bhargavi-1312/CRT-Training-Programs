# 3. program to read an integer as input for user and check it is a two digit num or not a two digit number 
num = int(input('Enter the integer :'))
#if-else
if((num >=10 and num<=99) or (num>=-99 and num<=-10) ):
    print("Two digit number")
else:
    print("not a two digit number")