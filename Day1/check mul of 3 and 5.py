# 15.wpp to read an integer value as a input value from the user and check whether it is a multiple of three and 5 or not
num=int(input('enter the number:'))
if(num%3==0 and num%5==0):
    print("number is divisible by 3 and 5")
else:
    print('number is not divisible by 3 and 5') 