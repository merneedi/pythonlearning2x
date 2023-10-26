scale  = int(input("Enter the num\n"))

match scale:
    case (scale >=90 and scale <=100):
        print("grade is A")
    case scale <=89 and scale >=80:
        print("grade is B")
    case scale >= 70 and scale <= 79:
        print("grade is C")
    case scale >=60 and scale <=69:
        print("grade is D")
    case scale <=59 and scale >=0:
        print("grade is F")
    case _:
        print("Invalid")
