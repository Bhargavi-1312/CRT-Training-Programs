# sales data analytics
sales = []
for i in range(7):
    sale = float(input(f"Enter sales for day {i+1}: "))
    sales.append(sale)
    total_sales = sum(sales)
    max_sales = max(sales)
print(f"Total sales for the week: {total_sales}") 
print(f"Highest sales: {max_sales}")    