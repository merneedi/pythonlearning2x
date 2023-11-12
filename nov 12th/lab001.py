#Division by zero exception

try:
    x = int(input("Enter a Num\n"))
    result = 10/x #Attempting to divide by zero
    print(result)
except ZeroDivisionError as error:
    print('Error: ', error)
except ValueError as error:
    print('Error: ', error)
except NameError as error:
    print('Error: ', error)
finally:
    print("I will be executed any how")
