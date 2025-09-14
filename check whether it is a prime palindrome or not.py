#check whether the user entered integer is a prime palindrome  or not method 1
n=int(input("Enter a number: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    factor=0
    for i in range(1,temp+1):
        if(temp%i)==0:
            factor+=1
    res="prime palindrome" if factor==2 else "not a prime palindrome"
    print(temp,"is",res)