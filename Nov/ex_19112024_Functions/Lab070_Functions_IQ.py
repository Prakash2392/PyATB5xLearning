# Create a program to sum of three  number of user input,
# if user doesn't enter any number, use default 100,200,300

def sum_of_three(n1=100,n2=200,n3=300):
    return n1+n2+n3

num1 = int(input("Enter the 1st value \n"))
num2 = int(input("Enter the 2nd value \n"))
num3 = int(input("Enter the 3rd value \n"))

res = sum_of_three(num1,num2,num3)
print(res)
print(sum_of_three())
