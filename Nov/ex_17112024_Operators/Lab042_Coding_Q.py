# Write a Python program to calculate the area of circle given its radius using the formula
# area=pi*r^2 --> take pi=3.14

# Logic building formula

# || step 1 ||
# Figure out the inputs and Output
# input -> r -> data type -> float
# pi = 3.14
# power -> pow or ** --> any
# o/p -> float - area, print area

# || step 2 ||
# rough logic = area = 3.14 * pow (r,2)

# || step 3 ||

radius = float(input("Enter the radius of circle\n"))
print(radius)
area = 3.14 * (radius ** 2)
print("Area of circle is", area)
print(f"Area of the circle is ((Area)):{area:.2f}")

import math
#
# print(math.pi)
# print(math.pow(radius,y:2))
# print("Area of the circle is",area)

print(math.pi)
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))