# Write a program to take a user age and let him know if he can go the club.  21


usr_age = int(input("Enter your age:"))
if usr_age >= 21:
    print("You can go to the club")
else:
    print(f"You can't go to the club because of your age is {usr_age}")
