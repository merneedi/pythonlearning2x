#function scope
#In python it executes line by line code so it is a intrepeter
#here it executes line 4 first and goes to 5 and jmp to call op
num = 20

def multiply(n):
    n *= 10
    num = n
    print('Value of num inside the function', num)
    return n

op = multiply(num)
print(op)
print("val of num outside fun:", num)