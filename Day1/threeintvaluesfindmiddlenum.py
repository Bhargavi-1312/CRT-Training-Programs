# 10.wpp to read three integer values as input from the user and find the middle number using if else?
num1=int(input('enter the first integer:'))
num2=int(input('enter the second integer:'))
num3=int(input('enter the third integer:'))
if(num1>=num2 and num2<=num3):
    print(f"{num2} is the middle number")
elif(num2>=num3 and num3<=num1):
    print(f"{num3} is the middle number")
else:
    print(f"{num1} is the middle number")