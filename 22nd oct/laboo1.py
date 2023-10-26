scale  = int(input("Enter the num\n"))
#grade = None
if scale >=90 and scale <=100:
    print("grade is A")
elif scale <=89 and scale >=80:
    print("grade is B")
elif scale >= 70 and scale <= 79:
    print("grade is C")
elif scale >=60 and scale <=69:
    print("grade is D")
elif scale <=59 and scale >=0:
    print("grade is F")
else:
    print("Invalid")
