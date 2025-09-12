#6.wpp to read two integer values as a user find the largest number using if and ternary operator
num1=int(input('enter the first integer:'))
num2=int(input('Enter the second integer:'))
#if-else
if(num1>num2):
    print(f"{num1} is largest number.")
else:
    print(f"{num2} is largest number.")

 #ternary operator

res=num1 if(num1>num2) else num2
print(f"{res} is largest number.")
