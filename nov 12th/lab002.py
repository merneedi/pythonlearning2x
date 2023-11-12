#Division by zero exception

try:
    x = int(input("Enter a Num\n"))
    result = 10/x #Attempting to divide by zero
    print(result)
except Exception as error:
    print('Parent exception: ', error)
finally: #its not mandatory
    print("I will be executed any how")
