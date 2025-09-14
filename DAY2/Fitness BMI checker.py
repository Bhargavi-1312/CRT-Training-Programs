#Fitness BMI checker
BMI=int(input("Enter the weight:"))
if BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 and BMI<25:
    print("Normal Weight")
elif BMI >=25 and BMI < 30:
    print("overweight")
else:
    print("obese")            