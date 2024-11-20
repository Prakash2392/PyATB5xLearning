# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by
# 100 but not by 400.


year = int(input("Enter the year"))
if year % 4 == 0 and year % 100 != 0:
    leap = True
elif year % 100 == 0 and year % 400 == 0:
    leap = True
else:
    leap = False
    print(f"Entered year {year} is not a leap year")
print("Entered year is leap:", leap)
