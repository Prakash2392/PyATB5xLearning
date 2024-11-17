# if age > 18 - allowed to vote
# else - not allowed

user_age = int(input("Enter your age:\n"))

if user_age > 18:
    print("yes you can go Goa and vote")
else:
    print("NO you can't go Goa and vote")

# Using ternary operator 
# print("yes you can go Goa and vote" if  int(input("Enter your age:\n")) > 18 else "NO you can't go Goa and vote")
