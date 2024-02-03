# Try except


try:
    a =10/0
except ZeroDivisionError as e:
    print(e)

# try except and nested except
try:
        num1 = int(input("Enter a number\n"))
        num2 = int(input('Enter a number\n'))
        result = num1/num2
        #print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("num2 is zero")
else:
    print(f"Result is {result}")
finally:
    print("I will be always executed")


# try except , else and finally