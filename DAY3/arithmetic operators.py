a=int(input("enter the first intger:"))
b=int(input("enter the second integer:"))
while(True):
    print("----------------> operations menu----------->")
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if(choice==1):
        print(f"summation of {a},{b} is {a+b}")
        print()
    elif(choice==2):
        print(f"Difference of {a},{b} is {a-b}")
        print()
    elif(choice==3):
        print(f" product of {a},{b} is {a*b}")
        print()
    elif(choice==4):
        print(f"Quotient of {a},{b} is {a/b}")
        print()
    elif(choice==5):
        print(f"Thanks for using the operations menu")
        break

