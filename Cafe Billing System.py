#Cafe Billing system
coffee_price = float(input("enter the price of one cofee:"))
coffee_qty = int(input("enter the quantity of coffee:"))
snack_price = float(input("enter the price of one snack:"))
snack_qty= int(input("enter the quantity of snack:"))
total = (coffee_price*coffee_qty) + (snack_price*snack_qty)
bill= total + (total * 0.05)
print(f"total bill amount is :",{bill})

