#check whether the user entered integer is a prime number or not method 1
num=int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
#check whether the user entered integer is a prime number or not method 2
num=int(input("Enter a number: "))
factor=0
for i in range(1,num+1):
    if(num%i)==0:
        factor+=1
res="prime number" if factor==2 else "not a prime number"
print(num,"is",res)        