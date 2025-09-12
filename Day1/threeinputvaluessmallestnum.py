# 9.wpp to read three integer values as input from the user and find the smallest number using both if else and ternary operator
#if-else-elif
num1=int(input('enter the first integer'))
num2=int(input('enter the second integer'))
num3=int(input('enter the third integer'))
if(num1<num2):
    print(f"{num1} is smallest number")
elif(num2<num3):
     print(f"{num2} is smallest number") 
else:
  print(f"{num3} is smallest number")

#ternary operator
smallest = num1 if(num1<num2 and num1<num3) else num2
res=num3 if(num3<num1 and num3<num2) else smallest
print(f"{res} is the smallest number")
