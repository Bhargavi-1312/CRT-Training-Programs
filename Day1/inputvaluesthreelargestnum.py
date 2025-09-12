
# 8.WPP to read three input values as input from the user then find the largest number 
num1=int(input('enter the first integer'))
num2=int(input('enter the second integer'))
num3=int(input('enter the third integer'))
if(num1>num2):
    print(f"{num1} is largest number")
elif(num2>num3):
    print(f"{num2} is largest number") 
else:
    print(f"{num3} is largest number") 

#ternary operator
num1=int(input('enter the first integer'))
num2=int(input('enter the second integer'))
num3=int(input('enter the third integer'))
largest= num1 if(num1>num2 and num1>num3) else num2
res=num3 if(num3>num1 and num3>num2) else largest
print(f"{res} is the largest number")
