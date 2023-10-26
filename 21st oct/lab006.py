#import math

#radius = float(input("Enter the radius\n"))
#area = math.pi * (radius *2)
#print(area)

a1 = int(input("enter the num1\n"))
a2 = int(input("enter the num2\n"))

sum = "greater" if a1>a2 else "less than" if a1<a2 else "equal"

print(f"{a1} is {sum} {a2}")