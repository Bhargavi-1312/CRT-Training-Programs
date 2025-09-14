n=int(input("Enter a year: "))
leap_years = []
while len(leap_years) < 25:
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        leap_years.append(n)
    n += 1
print("The next 25 leap years are:", leap_years)