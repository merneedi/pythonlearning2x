#try except
try:
    a=10/0
except ZeroDivisionError as e:
    print(e)

#try except and nested except
try:
    num1 = int(input("Enter a num\n"))
    num2 = int(input('Enter a num\n'))
    result = num1/num2
except ValueError:
    print("Invalid")
except ZeroDivisionError:
    print('zero division')
else:
    print(f"Result {result}")
finally:#universal exectued
    print("I will be executed!!")