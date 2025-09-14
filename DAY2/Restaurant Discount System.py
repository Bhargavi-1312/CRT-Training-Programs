# 5.restaurant discount system
bill=float(input("Enter the total bill amount:"))
if bill>1000:
    discount = bill * 0.10 #10%
elif bill>500:
    discount = bill * 0.05
else:
    discount = 0
final_amount= bill - discount
print(f"original Bill: {bill}")
print(f"Discount:{discount}")
print(f"Final Amount to pay:{final_amount}")
