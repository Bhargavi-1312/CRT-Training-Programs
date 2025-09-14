#Train Ticket concession

age =  int(input("Enter the age:"))
if age<=5:
    print("Free")
elif age>=5 and age<=12:
    print("HalfTicket")
elif age>=13 and age<=59:
    print("FullTicket")
else:
    print("30% Senior Citizen Discount")        
