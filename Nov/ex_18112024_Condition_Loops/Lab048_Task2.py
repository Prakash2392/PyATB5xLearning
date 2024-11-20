# Write a program that classifies a triangle based on its side lengths. Given three input
# values representing the lengths of the sides, determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

s1, s2, s3 = 60, 30, 60

if s1 == s2 == s3:
    print("It's a equilateral Triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("It's a isosceles Triangle")
else:
    print("It's a scalene Triangle")
