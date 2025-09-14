ages=list(map(int,input("enter the ages of people separated by space:").split()))
total_cost=0
for age in ages:
    if age<=12:
        total_cost+=150
    elif age<=59:
        total_cost+=250
    else:
        total_cost+=200
print(f"the total ticket cost is : {total_cost}")
    