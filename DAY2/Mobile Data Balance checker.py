#Mobile data balance checker

data =  int(input("Enter the data balance:"))
if data==0:
    print("Recharge Required")
elif data<=100:
    print("Low data Warning")
else:
    print("sufficient data available")        