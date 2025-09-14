#Loan Eligibility
salary = int(input("Enter the salary:"))
credit_score = int(input("Enter the credit_score:"))
if salary>=30000 and credit_score>=700:
    print("eligible")
else:
    print("Not eligible")    